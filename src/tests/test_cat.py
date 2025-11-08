# тесты для команды cat

import sys
from pathlib import Path
import tempfile
from commands.cat import *

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#без аргументов
def test_cat_komanda_no_args(capsys):

    cat_komanda([])
    captured = capsys.readouterr()
    assert "не указан файл" in captured.out

#чтение файла
def test_cat_komanda_read_file(capsys):

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
        f.write("test content")
        temp_path = f.name
    
    try:
        cat_komanda([temp_path])
        captured = capsys.readouterr()
        assert "test content" in captured.out
    finally:
        if Path(temp_path).exists():
            Path(temp_path).unlink()


#несуществующий файл
def test_cat_komanda_nonexistent_file(capsys):

    cat_komanda(["nonexistent_file_12345.txt"])
    captured = capsys.readouterr()
    assert "нет такого файла или каталога" in captured.out


#директория вместо файла
def test_cat_komanda_directory_instead_of_file(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        cat_komanda([tmpdir])
        captured = capsys.readouterr()
        assert "это каталог" in captured.out

