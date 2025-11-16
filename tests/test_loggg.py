# тесты для логирования

import os
import sys
from pathlib import Path
from src.loggg import zapisat_fold,zapisat_log,zapisat_predosterezhenie
from src.const import LOG_FILE

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#тест функции zapisat_log
def test_zapisat_log(capsys):

    message = "test message"

    # очищаем лог-файл перед тестом, если он существует
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    zapisat_log(message)
    
    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        assert message in content
        # проверяем, что есть уровень INFO в формате лога
        assert "INFO" in content
            

#тест функции zapisat_fold
def test_zapisat_fold(capsys):

    error_message = "test error"

    # очищаем лог-файл перед тестом, если он существует
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    zapisat_fold(error_message)
    
    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        assert error_message in content
        # проверяем, что есть уровень ERROR в формате лога
        assert "ERROR" in content
        # проверяем, что сообщение содержит "ERROR: " перед текстом ошибки (из функции)
        # формат: [дата время] ERROR: ERROR: сообщение
        assert "ERROR:" in content
    
    # проверяем, что ошибка также выводится в stderr (консоль)
    captured = capsys.readouterr()
    assert "ERROR" in captured.err
    assert error_message in captured.err


#тест функции zapisat_predosterezhenie
def test_zapisat_predosterezhenie(capsys):

    warning_message = "test warning"

        # очищаем лог-файл перед тестом, если он существует
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    zapisat_predosterezhenie(warning_message)
    
    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        assert warning_message in content
        # проверяем, что есть уровень WARNING в формате лога
        assert "WARNING" in content
        # проверяем, что сообщение содержит "WARNING: " перед текстом предупреждения (из функции)
        # формат: [дата время] WARNING: WARNING: сообщение
        assert "WARNING:" in content



