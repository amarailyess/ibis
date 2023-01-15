import os
import pathlib
from datetime import date

def create(dirname):
    try:
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print(os.path.basename(dirname), "Folder Already exists!")
    else:
        print(os.path.basename(dirname), " Folder was created successfully")

def create_forlders():
    curr_date = date.today()
    dir_name = str(curr_date.day) + '_' + str(curr_date.month) + '_' + str(curr_date.year)
    root_path = pathlib.Path().resolve()
    create(dir_name)
    os.chdir(dir_name)
    create("pre-livraison")
    create("livraison")

    os.chdir("pre-livraison")
    create("ZIP")
    create("ibis_to_rename")

    os.chdir("ibis_to_rename")
    create("STM32C0")
    create("STM32G0")

    os.chdir("STM32C0")
    create("443_C0_Spider")
    create("453_C0_Spider_Big")

    os.chdir("../STM32G0")
    create("456_OrcaZeroMax")
    create("467_Orca_Zero_512")
    os.chdir("..")
    for dir in os.listdir(pathlib.Path().resolve()):
        path_dir = str(pathlib.Path().resolve())+str("\\")+str(dir)
        for sub_dir in os.listdir(path_dir):
            create(str(dir)+str("\\")+str(sub_dir)+str("\\")+str("old_files"))
            create(str(dir)+str("\\")+str(sub_dir) + str("\\") + str("new_files"))
    print("***TREE***")
    list_files(str(root_path)+str("\\")+dir_name,dir_name)
    os.chdir("../..")

    return dir_name


def list_files(startpath,dir_name):
    for root, dirs, files in os.walk(startpath):

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 7 * (level)
        if os.path.basename(root) == dir_name:
            print('{}{}/'.format(indent, os.path.basename(root)))
        else:
            print('{}|__{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 7 * (level + 1)
        for f in files:
            print('{}|_{}'.format(subindent, f))


