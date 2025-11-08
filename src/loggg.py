#логгирование
#все команды и ошибки записываются в  sell.log

import logging
import sys
from const import LOG_FILE



#настройка логгирования
logging.basicConfig(
    filename=LOG_FILE,           # файл, где идет запись логгов
    level=logging.INFO,          # уровень логгирования
    format='[%(asctime)s] %(levelname)s: %(message)s',  # формат записи
    datefmt='%Y-%m-%d %H:%M:%S',  # дата фремя
    encoding='utf-8'              # поддержка алф
)


# вывод в консоль для ошибок
console_handler = logging.StreamHandler(sys.stderr)
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('[%(asctime)s] ERROR: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger().addHandler(console_handler)


#запись сообщения в лог-файл, логгирование успешных команд
def zapisat_log(mess):
    logging.info(mess)


#запись ошибки в лог-файл
def zapisat_fold(mess):
    logging.error(f"ERROR: {mess}")


#запись предупреждение в лог-файл
def zapisat_predosterezhenie(mess):
    logging.warning(f"WARNING: {mess}")
