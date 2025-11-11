# главный файл запуска программы 

import os 
from pathlib import Path
from loggg import zapisat_predosterezhenie,zapisat_log,zapisat_fold
from commands import KOMANDY

def zapustit_obolochku():

    print()
    print("привет, пользователь")
    print("я могу: ls, cd, cat, cp, mv, rm")
    print("для выхода напиши'exit' или нажми Ctrl+C")
    print()
    
    while True:
        try:
            # получаем текущую рабочую директорию
            tekushaya_dir = Path.cwd()
            
            # приглашение к вводу(формат: C:\путь\к\директории $) 
            print(f"{tekushaya_dir} $ ", end="", flush=True)
            
            # читаем команду пользователя
            vvod = input().strip()
            
            # пропускаем пустые строки
            if not vvod:
                continue
            
            # команда выхода из оболочки
            if vvod == "exit":

                print("выход из оболочки. пока-пока")
                zapisat_log("exit")
                break
            
            # Разбиваем ввод на части
            chast = vvod.split()
            name = chast[0]  # первое слово - имя команды
            args = chast[1:]  # остальные слова - аргументы команды
            
            # провереряем команду в словаре
            if name in KOMANDY:

                # команда найдена, вызываем функцию
                try:
                    KOMANDY[name](args)
                except KeyboardInterrupt:

                    # если команда была прервана пользователем (Ctrl+C)
                    print("\nКоманда прервана пользователем")
                    zapisat_predosterezhenie(f"Команда '{name}' прервана пользователем")
                except Exception as e:

                    # если команда вызвала необработанную ошибку
                    soobsh = f"Ошибка выполнения команды '{name}': {e}"
                    print(soobsh)
                    zapisat_fold(soobsh)
            else:

                soobsh = f"неизвестная команда: {name}"
                print(soobsh)
                zapisat_fold(soobsh)
        
        except (KeyboardInterrupt, EOFError):
            # обработка прерывания (Ctrl+C) или конца файла
            # происходит, когда пользователь нажимает Ctrl+C или Ctrl+Z
            print("\nВыход из оболочки. пока-пока")
            zapisat_log("exit (прервано пользователем)")
            break
        
        except Exception as e:
            # обработка любых других неожиданных ошибок
            soobsh = f"внутренняя ошибка оболочки: {e}"
            print(soobsh)
            zapisat_fold(soobsh)


# точка входа в программу

if __name__ == "__main__":
    zapustit_obolochku()
