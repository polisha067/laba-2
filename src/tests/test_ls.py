# тесты для команды ls

import os
import tempfile
import sys
from pathlib import Path
from commands.ls import *

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


# без аргументов
def test_ls_komanda_no_args(capsys):

    original_cwd = os.getcwd()
    try:
        with tempfile.TemporaryDirectory() as tmpdir:

            os.chdir(tmpdir)
            test_file = Path(tmpdir) / "test.txt"
            test_file.write_text("test")
            
            ls_komanda([])
            captured = capsys.readouterr()
            assert "test.txt" in captured.out
    finally:
        os.chdir(original_cwd)


# с указанием пути
def test_ls_komanda_with_path(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:

        test_dir = Path(tmpdir)
        test_file = test_dir / "file.txt"
        test_file.write_text("test")
        
        ls_komanda([str(test_dir)])
        captured = capsys.readouterr()
        assert "file.txt" in captured.out


# несуществующий файл
def test_ls_komanda_nonexistent_path(capsys):

    ls_komanda(["nonexistent_path_12345"])
    captured = capsys.readouterr()
    assert "нет такого файла или каталога" in captured.out


# файл вместо директории
def test_ls_komanda_file_instead_of_dir(capsys):

    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name
    try:
        ls_komanda([temp_path])
        captured = capsys.readouterr()
        assert "это не каталог" in captured.out
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)