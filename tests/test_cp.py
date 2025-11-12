# тесты для команды cp

import os
import tempfile
from pathlib import Path
import sys
from src.commands.cp import cp_komanda

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# без аргументов
def test_cp_komanda_no_args(capsys):

    cp_komanda([])
    captured = capsys.readouterr()
    assert "не хватает аргументов" in captured.out


#копрование файла
def test_cp_komanda_copy_file(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source.txt"
        dest = Path(tmpdir) / "dest.txt"
        source.write_text("test content")
        
        cp_komanda([str(source), str(dest)])
        
        assert dest.exists()
        assert dest.read_text() == "test content"


#несуществующий файл
def test_cp_komanda_nonexistent_source(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        dest = Path(tmpdir) / "dest.txt"
        cp_komanda(["nonexistent.txt", str(dest)])
        captured = capsys.readouterr()
        assert "нет такого файла или каталога" in captured.out

