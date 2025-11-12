# тесты для логирования

import os
import sys
from pathlib import Path
from src.loggg import zapisat_fold,zapisat_log,zapisat_predosterezhenie
from src.const import LOG_FILE

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

#тест функции zapisat_log
def test_zapisat_log():

    message = "test message"
    zapisat_log(message)
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            assert message in content
            

#тест функции zapisat_fold
def test_zapisat_fold():

    error_message = "test error"
    zapisat_fold(error_message)
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            assert error_message in content
            assert "ERROR" in content.upper()


#тест функции zapisat_predosterezhenie
def test_zapisat_predosterezhenie():

    warning_message = "test warning"
    zapisat_predosterezhenie(warning_message)
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            assert warning_message in content
            assert "WARNING" in content.upper()



