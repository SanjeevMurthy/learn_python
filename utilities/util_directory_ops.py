import os
import shutil
from pathlib import Path



def delete_directories(root_dir):
    dir = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]
    print(dir)

    for d in dir:
        path = os.path.join(root_dir, d)
        print(path)
        try:
            shutil.rmtree(path)
            print("Directory '% s' has been removed successfully" % d)
        except OSError as error:
            print(error)
            print("Directory '% s' can not be removed" % d)


def make_directory(root, dir_name):
    Path(f"{root}/{dir_name}").mkdir(parents=True, exist_ok=True)

ROOT_DIR = "./certs"
delete_directories(ROOT_DIR)
make_directory(ROOT_DIR, "802")
make_directory(ROOT_DIR, "SOAP")