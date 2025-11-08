#команда вывдит содержимое файла

from pathlib import Path
from const import *
from loggg import *

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
        
        # проверяем, что файл существует
        if not fayl_absolyutny.exists():
            soobsh = f"cat: {fayl_str}: нет такого файла или каталога"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # проверяем, что это не директория
        if fayl_absolyutny.is_dir():
            soobsh = f"cat: {fayl_str}: это каталог"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # проверяем, что это файл
        if not fayl_absolyutny.is_file():
            soobsh = f"cat: {fayl_str}: это не файл"
            print(soobsh)
            zapisat_fold(soobsh)
            return

        try:
            with open(fayl_absolyutny, 'r', encoding=FILE_ENCOD, errors='replace') as f:
                soderzhimoe = f.read()

                print(soderzhimoe, end='')

        except UnicodeDecodeError:

            soobsh = f"cat: {fayl_str}: не удалось прочитать файл"
            print(soobsh)
            zapisat_fold(soobsh)
            return
        
        # логируем выполнение
        zapisat_log(f"cat {fayl_str}")
        
    except PermissionError:

        soobsh = f"cat: {fayl_str}: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"cat: {fayl_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)