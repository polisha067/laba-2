# импорт всех команд и создание их словаря для дальнейшего вызова

from .cat import cat_komanda
from .cd import cd_komanda
from .cp import cp_komanda
from .ls import ls_komanda
from .mv import mv_komanda
from .rm import rm_komanda



KOMANDY = {
    'ls': ls_komanda,
    'cd': cd_komanda,
    'cat': cat_komanda,
    'cp': cp_komanda,
    'mv': mv_komanda,
    'rm': rm_komanda,
}


