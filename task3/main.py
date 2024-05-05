import sys
from pathlib import Path
from colorama import Fore


def parse_file(file_path: Path, level=0) -> list[dict[str, str]]:
    indent = ' ' * 2 * level
    for el in file_path.iterdir():
        if el.is_dir():
            print(Fore.BLUE + indent + el.name)
            parse_file(el, level + 1)
        else:
            print(Fore.GREEN + indent + el.name)


path = Path(sys.argv[1])
parse_file(path)
