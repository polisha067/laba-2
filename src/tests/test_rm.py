# тесты для команды rm

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
from commands.rm import *

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#без аргументов
def test_rm_komanda_no_args(capsys):

    rm_komanda([])
    captured = capsys.readouterr()
    assert "не указан объект для удаления" in captured.out


#удаление файлов
def test_rm_komanda_delete_file(capsys):

    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name
        f.write(b"test")
    
    try:
        rm_komanda([temp_path])
        assert not os.path.exists(temp_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


#с несуществуюшим файлом
def test_rm_komanda_nonexistent_file(capsys):

    rm_komanda(["nonexistent_file_12345.txt"])
    captured = capsys.readouterr()
    assert "нет такого файла или каталога" in captured.out


#удаление директории
def test_rm_komanda_delete_directory(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir) / "test_dir"
        test_dir.mkdir()
        
        with patch('builtins.input', return_value='y'):
            rm_komanda([str(test_dir)])
        
        assert not test_dir.exists()

