import os
from config import path_users_directory

def get_all_files_from_users_directory():
    # Путь к директории users в корневой папке
    users_directory = os.path.join(os.getcwd(), path_users_directory)

    all_files = []
    for root, dirs, files in os.walk(users_directory):
        for file in files:
            all_files.append(os.path.join(root, file))



    return all_files


def first_power():
    files = get_all_files_from_users_directory()
    dict_user = dict()
    for file in files:
        base_name = os.path.basename(file)
        # Отделяем имя файла от расширения
        file_name, _ = os.path.splitext(base_name)
        dict_user[file_name] = Users(file_name, file)

    return dict_user