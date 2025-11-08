#логгирование
#все команды и ошибки записываются в  sell.log

import logging
import sys

#настройка логгирования
logging.basicConfig(
    
)



#запись сообщения в лог-файл, логгирование успешных команд
def zapisat_log(mess):
    logging.info(mess)


#запись ошибки в лог-файл
def zapisat_fold(mess):
    logging.error(f"ERROR: {mess}")


#запись предупреждение в лог-файл
def zapisat_predosterezhenie(mess):
    logging.warning(f"WARNING: {mess}")
