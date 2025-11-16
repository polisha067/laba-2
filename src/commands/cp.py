#  копирует файл или директорию

import os
import shutil
from pathlib import Path
from loggg import  zapisat_fold, zapisat_log

def cp_komanda(argumenty):
    if len(argumenty) < 2:
        soobsh = "cp: не хватает аргументов"
        print(soobsh)
        zapisat_fold(soobsh)
        return
    
    istochnik_str = argumenty[0]  # источник
    naznachenie_str = argumenty[1]  # назначение
    
    try:
        # преобразуем пути в Path
        istochnik = Path(istochnik_str).resolve()
        naznachenie = Path(naznachenie_str)
        
        # если назначение - существующая директория, копируем в неё с исходным именем
        if naznachenie.exists() and naznachenie.is_dir():
            naznachenie = naznachenie / istochnik.name

        naznachenie = naznachenie.resolve()

        # проверяем, что не пытаемся скопировать директорию в саму себя
        if istochnik.is_dir() and naznachenie.exists():
            if str(naznachenie).startswith(str(istochnik) + os.sep):
                soobsh = f"cp: {istochnik_str}: невозможно скопировать директорию в саму себя"
                print(soobsh)
                zapisat_fold(soobsh)
                return

        naznachenie = naznachenie.resolve()
        
        # копируем
        if istochnik.is_dir():
            # если источник - директория, копируем рекурсивно
            shutil.copytree(istochnik, naznachenie, dirs_exist_ok=True)
        else:
            # если источник - файл, копируем файл
            shutil.copy2(istochnik, naznachenie)
        
        # логируем выполнение
        zapisat_log(f"cp {istochnik_str} -> {naznachenie_str}")
    

    except FileNotFoundError:
        soobsh = f"cp: {istochnik_str}: нет такого файла или каталога"
        print(soobsh)
        zapisat_fold(soobsh)


    except PermissionError:

        soobsh = f"cp: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except shutil.SameFileError:

        soobsh = f"cp: {istochnik_str} и {naznachenie_str} - это один и тот же файл"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"cp: {istochnik_str} -> {naznachenie_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)
