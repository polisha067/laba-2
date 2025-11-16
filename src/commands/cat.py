#команда вывдит содержимое файла

from pathlib import Path
from const import FILE_ENCOD
from loggg import zapisat_fold, zapisat_log

def cat_komanda(argumenty):

    # проверяем, что указан файл
    if not argumenty:
        soobsh = "cat: не указан файл"
        print(soobsh)
        zapisat_fold(soobsh)
        return
    
    # получаем путь к файлу (первый аргумент)
    fayl_str = argumenty[0]
    
    try:
        # преобразуем строку пути в Path
        fayl = Path(fayl_str)

        fayl_absolyutny = fayl.resolve()

            
        with open(fayl_absolyutny, 'r', encoding=FILE_ENCOD, errors='replace') as f:
            soderzhimoe = f.read()

            print(soderzhimoe, end='')

        # логируем выполнение
        zapisat_log(f"cat {fayl_str}")
    
    except FileNotFoundError:
        soobsh = f"cat: {fayl_str}: нет такого файла или каталога"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except IsADirectoryError:
        soobsh = f"cat: {fayl_str}: это каталог"
        print(soobsh)
        zapisat_fold(soobsh)  
    except PermissionError:

        soobsh = f"cat: {fayl_str}: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"cat: {fayl_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)