import os
import shutil
from os import listdir
from pathlib import Path
import git
from os import walk


def delete_directories(root_dir):
    dir = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]
    filenames = next(walk(root_dir), (None, None, []))[2]
    print(filenames)
    print(dir)
    for f in filenames:
        path = os.path.join(f)
        print("Path ",path)
        shutil.rmtree(path)
    for d in dir:
        path = os.path.join(root_dir, d)
        print(path)
        try:
            shutil.rmtree(path)
            print("Directory '% s' has been removed successfully" % d)
        except OSError as error:
            print(error)
            print("Directory '% s' cannot be removed" % d)


try:
    dir_name = "tsd-cli"

    if Path(dir_name).exists():
        #delete_directories(dir_name)
        shutil.rmtree(dir_name, ignore_errors=True)

    Path(dir_name).mkdir(parents=True)
    os.chdir(dir_name)

    print("Cloning... TSD-Prod")
    git.Repo.clone_from('ssh://git@vmlnxatlstash.lowes.com:42000/~3984268/tsd-fork.git', '.', branch='prod')
    print("Cloning... TSD-src")
    git.Repo.clone_from('ssh://git@vmlnxatlstash.lowes.com:42000/~3984268/tsd-fork.git', 'src', branch='src')
    print("Cloning... TSD-config")
    git.Repo.clone_from('ssh://git@vmlnxatlstash.lowes.com:42000/~3984268/tsd-configs-fork.git', 'config',
                        branch='prod')
    print("Cloning... REG-config")
    git.Repo.clone_from('ssh://git@vmlnxatlstash.lowes.com:42000/~3984268/tsd-register-config-fork.git',
                        'register-config-bitbucket', branch='prod')
except Exception as e:
    print(e)
