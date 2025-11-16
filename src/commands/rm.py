# удаляет файл или директорию

import os 
import shutil
from pathlib import Path
from loggg import zapisat_fold, zapisat_log, zapisat_predosterezhenie
from const import FORBID_RATHS

def rm_komanda(argumenty):

    # проверяем, что указан объект для удаления
    if not argumenty:
        soobsh = "rm: не указан объект для удаления"
        print(soobsh)
        zapisat_fold(soobsh)
        return
    
    put_str = argumenty[0]
    
    try:
        # преобразуем путь в Path
        put = Path(put_str).resolve()
        
        # защита от случайного удаления важных путей
        # проверяем, не является ли путь одним из запрещенных
        put_str_normalized = str(put).replace('\\', '/')  # Нормализуем разделители
        
        # проверяем запрещенные пути
        for forbidden in FORBID_RATHS:
            if put_str_normalized == forbidden or put_str_normalized.endswith('/' + forbidden):
                soobsh = f"rm: запрещено удалять '{put_str}' (системный путь)"
                print(soobsh)
                zapisat_fold(soobsh)
                return
        
        
        # обрабатываем
        if put.is_dir():
            # если это директория, спрашиваем подтверждение
            otvet = input(f"rm: удалить папку '{put_str}'? (y/n): ")
            
            if otvet.lower() != 'y':
                # отмена операции
                zapisat_predosterezhenie(f"rm {put_str} отменено пользователем")
                return
            
            # удаляем директорию рекурсивно
            shutil.rmtree(put)
            
        else:
            #если это файл удаляем без подтверждения
            os.remove(put)
        
        # логируем выполнение
        zapisat_log(f"rm {put_str}")
    
    except FileNotFoundError:
        
        soobsh = f"rm: {put_str}: нет такого файла или каталога"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except PermissionError:

        soobsh = f"rm: {put_str}: отказано в доступе"
        print(soobsh)
        zapisat_fold(soobsh)
        
    except Exception as e:

        soobsh = f"rm: {put_str}: {e}"
        print(soobsh)
        zapisat_fold(soobsh)
    

