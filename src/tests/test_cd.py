# тесты для команды cd

import os
import tempfile
from pathlib import Path
import sys
from commands.cd import *

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# без аргументов
def test_cd_komanda_no_args(capsys):

    original_cwd = os.getcwd()
    try:
        cd_komanda([])
        captured = capsys.readouterr()
        assert "пропущен аргумент" in captured.out
    finally:
        os.chdir(original_cwd)


#смена директории
def test_cd_komanda_change_directory(capsys):

    original_cwd = os.getcwd()
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = Path(tmpdir)
            subdir = test_dir / "subdir"
            subdir.mkdir()
            
            os.chdir(test_dir)
            cd_komanda([str(subdir)])
            assert os.getcwd() == str(subdir.resolve())
    finally:
        os.chdir(original_cwd)


#несуществующий путь
def test_cd_komanda_nonexistent_path(capsys):

    original_cwd = os.getcwd()
    try:
        cd_komanda(["nonexistent_path_12345"])
        captured = capsys.readouterr()
        assert "нет такого файла или каталога" in captured.out
    finally:
        os.chdir(original_cwd)


#файл вместо директории
def test_cd_komanda_file_instead_of_dir(capsys):

    original_cwd = os.getcwd()
    try:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            temp_path = f.name
        try:
            cd_komanda([temp_path])
            captured = capsys.readouterr()
            assert "это не каталог" in captured.out
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    finally:
        os.chdir(original_cwd)

