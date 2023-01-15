import os
import pathlib
import shutil
import zipfile
from data import data
import create_tree
dir_name = create_tree.create_forlders()


work_path = pathlib.Path().resolve()
delivery_path = str(work_path)+'\livraison'
ibis_to_rename_dir = str(work_path)+'\pre-livraison\ibis_to_rename'
zip_path = str(work_path)+str('\pre-livraison\ZIP')

for dir in os.listdir(ibis_to_rename_dir):
    dir_path = str(ibis_to_rename_dir)+str('\\')+str(dir)
    for sub_dir in os.listdir(dir_path):
        old_file_path = str(dir_path)+str('\\')+str(sub_dir)+str("\old_files")
        new_file_path = str(dir_path)+str('\\')+str(sub_dir)+str("\\new_files")
        for file in os.listdir(old_file_path):
            for item in data:
                for p in item["package"]:
                    if p in file and file.index(p) + len(p) == file.index('.') and sub_dir == item["internal_name"] and dir == item['family']:
                         new_file_name = file.replace(item["old_name"], item["new_name"])
                         if new_file_name != file:
                              try:
                                  os.rename(old_file_path+str('\\')+file, old_file_path+str('\\')+new_file_name)
                                  shutil.move(old_file_path + str('\\') + new_file_name, new_file_path)
                                  new_file = new_file_path+ str('\\') + new_file_name

                              except WindowsError:
                                  # RESET
                                  print("Error RENAME or MOVE FILE ==> ", file)

                         # print(item['family']+str('\\')+item["internal_name"],"*** ",file,"===>", new_file_name)
        print("_____________________________________")

for dir in os.listdir(delivery_path):
    os.remove(delivery_path+str('\\')+dir)

print("_____________________________________")

for dir in os.listdir(str(work_path)):
    if dir != "pre-livraison" and dir != "livraison":
        os.remove(dir)

for dir in os.listdir(zip_path):
    if(".zip" in dir):
        zip_file_path = zip_path + str("\\") + dir
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(zip_path)
        os.remove(zip_file_path)
print("_____________________________")
for dir in os.listdir(ibis_to_rename_dir):
    dir_path = str(ibis_to_rename_dir)+str('\\')+str(dir)
    for sub_dir in os.listdir(dir_path):
        new_file_path = str(dir_path)+str('\\')+str(sub_dir)+str("\\new_files")
        for file in os.listdir(new_file_path):
            for zip_dir in os.listdir(zip_path):
                if dir.upper() in zip_dir.upper():
                    shutil.move(new_file_path + str('\\') + file, zip_path+str('\\')+zip_dir)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

for zip_dir in os.listdir(zip_path):
    if (".zip" not in zip_dir):
        with zipfile.ZipFile(delivery_path+str('\\') +zip_dir+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(zip_path+str('\\') +zip_dir, zipf)
# DEFAULT ZIP NAME: en.stm32g0_ibis REPLACE g0 , c0 , etc
