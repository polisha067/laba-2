# перемещает или переименовывает файл или директорию

import shutil
import os
from pathlib import Path
from loggg import zapisat_fold, zapisat_log

def mv_komanda(argumenty):

    # проверяем, что указаны оба аргумента
    if len(argumenty) < 2:
        soobsh = "mv: не хватает аргументов"
        print(soobsh)
        zapisat_fold(soobsh)
        return
    
    istochnik_str = argumenty[0]  # источник
    naznachenie_str = argumenty[1]  # назначение
    
    try:
        # преобразуем пути в Path
        istochnik = Path(istochnik_str).resolve()
        naznachenie = Path(naznachenie_str)
        

        # если назначение - существующая директория, перемещаем в неё с исходным именем
        if naznachenie.exists() and naznachenie.is_dir():
            naznachenie = naznachenie / istochnik.name
        
        naznachenie = naznachenie.resolve()
        
        # проверяем, что не пытаемся переместить файл/директорию в саму себя
        if istochnik.samefile(naznachenie):
            soobsh = f"mv: {istochnik_str} и {naznachenie_str} - это один и тот же файл"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # перемещаем файл или директорию
        shutil.move(str(istochnik), str(naznachenie))
        
        # логируем выполнение
        zapisat_log(f"mv {istochnik_str} -> {naznachenie_str}")
        

        
    except FileNotFoundError:

        soobsh = f"mv: {istochnik_str}: нет такого файла или каталога"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except PermissionError:

        soobsh = f"mv: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"mv: {istochnik_str} -> {naznachenie_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)
