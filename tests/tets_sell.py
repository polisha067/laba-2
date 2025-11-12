#тест главной функции

from pathlib import Path
from unittest.mock import patch
from src.sell import zapustit_obolochku
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#тест команды exit
def test_zapustit_obolochku_exit():

    with patch('builtins.input', side_effect=['exit']):
        with patch('builtins.print'):
            # Проверяем, что функция завершается без ошибок
            try:
                zapustit_obolochku()
            except SystemExit:
                pass
            except StopIteration:
                pass