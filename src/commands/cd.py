# команда меняет текущую дерикторию

import os
from pathlib import Path
from loggg import *

def cd_komanda(argumenty):

    if not argumenty:
        soobsh = "cd: пропущен аргумент"
        print(soobsh)
        zapisat_fold(soobsh)
        return
    
    tsel_str = argumenty[0]
    
    try:
        # Раскрываем ~ в путь к домашней директории
        rasshirenny_put = os.path.expanduser(tsel_str)
        
        # преобразуем в Path объект для проверки
        tsel = Path(rasshirenny_put)
        
        # проверяем, что путь существует
        if not tsel.exists():
            soobsh = f"cd: {tsel_str}: нет такого файла или каталога"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # проверяем, что это директория
        if not tsel.is_dir():
            soobsh = f"cd: {tsel_str}: это не каталог"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # меняем текущую директорию
        os.chdir(tsel)
        
        # логируем выполнение
        zapisat_log(f"cd {tsel_str} -> {tsel.resolve()}")
        
    except PermissionError:

        soobsh = f"cd: {tsel_str}: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"cd: {tsel_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)