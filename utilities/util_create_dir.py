from pathlib import Path

"""
1. Check if Certs folder exist
2. Check if 802 and SOAP folder exists under Certs
3. Create folder based on Store number - read it form a list
"""


def make_directory(root, dir_name):
    Path(f"{root}/{dir_name}").mkdir(parents=True, exist_ok=True)


def check_if_exists(path):
    return Path(path).exists()


def create_folder_structure(root_folder):
    if not check_if_exists(root_folder):
        make_directory(root_folder)
    if not check_if_exists(f"{root_folder}/802"):
        make_directory(root_folder, "802")
    if not check_if_exists(f"{root_folder}/SOAP"):
        make_directory(root_folder, "SOAP")


def main():
    create_folder_structure("Certs")
    make_directory("Certs/SOAP", 1680)
    # TODO for each store - check if folder already exist and check for 3 files


if __name__ == '__main__':
    main()