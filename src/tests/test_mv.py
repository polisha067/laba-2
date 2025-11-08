# тесты для команды mv

import tempfile
from pathlib import Path
import sys
from commands.mv import *

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#без аргументов
def test_mv_komanda_no_args(capsys):

    mv_komanda([])
    captured = capsys.readouterr()
    assert "не хватает аргументов" in captured.out


#перемещение файлов
def test_mv_komanda_move_file(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source.txt"
        dest = Path(tmpdir) / "dest.txt"
        source.write_text("test content")
        
        mv_komanda([str(source), str(dest)])
        
        assert not source.exists()
        assert dest.exists()
        assert dest.read_text() == "test content"


# тест с несуществующим источником
def test_mv_komanda_nonexistent_source(capsys):

    with tempfile.TemporaryDirectory() as tmpdir:
        dest = Path(tmpdir) / "dest.txt"
        mv_komanda(["nonexistent.txt", str(dest)])
        captured = capsys.readouterr()
        assert "нет такого файла или каталога" in captured.out

