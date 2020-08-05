import os,shutil
try:
    path = "E:\\Sehari-hari\\Proyek\\Python\\fileOrganizer"
    for (path,dirs,files) in os.walk(path):
        for file in files:
           extension = file.split('.')[1]
           if os.path.exists(r"E:\\Sehari-hari\\Proyek\\Python\\fileOrganizer\\"+extension):
               if file.endswith(extension):
                   shutil.move(file,"E:\\Sehari-hari\\Proyek\\Python\\fileOrganizer\\"+extension)
           else:
               os.system('mkdir '+ extension)
               shutil.move(file,"E:\\Sehari-hari\\Proyek\\Python\\fileOrganizer\\"+extension)
except :
    print("task done")