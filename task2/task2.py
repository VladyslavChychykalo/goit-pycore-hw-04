# Variant 1
# def get_cats_info(file_path):
#     with open(file_path, "r") as file:
#         transformed_cat_data = []
#         cats_inner_info = file.read().strip().split("\n")

#         for cat in cats_inner_info:
#             cat = cat.split(",")
#             transformed_cat_data.append(
#                 {"name": cat[0], "breed": cat[1], "age": cat[2]})

#         return transformed_cat_data


# cats_info = get_cats_info("./data.txt")
# print(cats_info)


# Variant 2

from pathlib import Path


def get_cats_info(file_path: Path) -> list[dict[str, str]]:
    with file_path.open("r", encoding='utf-8') as file:
        cats_inner_info = file.readlines()
        cats_inner_info = [cat.strip().split(",") for cat in cats_inner_info]
        cats_inner_info = [{"name": cat[0], "breed": cat[1], "age": cat[2]}
                           for cat in cats_inner_info]
        return cats_inner_info


path = Path('goit-pycore-hw-04/task2/data.txt')

cats_info = get_cats_info(path)
print(cats_info)
