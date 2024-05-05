"""
In my opinion the better way to solve this task is to use the pathlib module.
I not sure that we need this module here, 
but without this module command "Run code" in output doesnt work.
"""

from pathlib import Path


def total_salary(file_path: Path) -> tuple[int, int]:
    try:
        with file_path.open('r', encoding='utf-8') as file:
            transformed_data = file.read().strip().split('\n')
            total_inner = 0
            for item in transformed_data:
                total_inner += int(item.split(',')[1])
            return (total_inner, total_inner // len(transformed_data))
    except FileNotFoundError:
        return ("File not found", '')
    except ValueError:
        return ("Value error", '')


path = Path('goit-pycore-hw-04/task1/data.txt')

total, average = total_salary(path)

if isinstance(total, int):
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print(total)
