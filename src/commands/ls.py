import os
from pathlib import Path
from datetime import datetime
from loggg import zapisat_fold, zapisat_log

#команда показвыает список файлов и папок в указанной дериктории
def ls_komanda(argumenty):

    # определяем, есть ли флаг подробного вывода
    detalno = "-l" in argumenty
    
    # убираем флаг -l из аргументов, чтобы найти путь, если флаг есть, он будет удален, останется только путь
    args_bez_flaga = [arg for arg in argumenty if arg != "-l"]
    
    # определяем путь: если есть аргумент, используем его, иначе текущая директория
    if args_bez_flaga:
        put_str = args_bez_flaga[0]
    else:
        put_str = "."
    
    try:
        # преобразуем строку пути в Path
        put = Path(put_str).resolve()

        #получаем список файлов и папок в указанной дир
        spisok = os.listdir(put)

        #сортируем список
        spisok.sort()

    
        
        # выводим каждый элемент
        for imya_fayla in spisok:
            # cоздаем путь
            polny_put = put / imya_fayla
            
            if detalno:
            
                try:
                    # получаем информацию о файле через os.stat()
                    stat_info = os.stat(polny_put)

                    razmer = stat_info.st_size

                    data_vremya = datetime.fromtimestamp(stat_info.st_mtime)
                    data_str = data_vremya.strftime('%Y-%m-%d %H:%M')
                    
                    prava = oct(stat_info.st_mode)[-3:]

                    tip = "d" if polny_put.is_dir() else "-"

                    print(f"{tip}{prava} {razmer:>10} {data_str} {imya_fayla}")
                    
                except OSError as e:
                    # если не удалось получить информацию о файле
                    print(f"ls: {imya_fayla}: не удалось получить информацию")
                    zapisat_fold(f"ls: {imya_fayla}: {e}")
            else:
                print(imya_fayla)
        
        # логируем выполнение
        komanda_str = f"ls {' '.join(argumenty)}"
        zapisat_log(komanda_str)

    except FileNotFoundError:

        soobsh = f"ls: {put_str}: нет такого файла или каталога"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except NotADirectoryError:
        
        soobsh = f"ls: {put_str}: это не каталог"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except PermissionError:
    
        soobsh = f"ls: {put_str}: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"ls: {put_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)
