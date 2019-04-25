import os

path1 = "Images/008/"
name1 = "milhouse_"



for filename in os.listdir(path1):
    pic, src = filename.split("_")
    dst = path1 + name1 + src
    filename = path1 + filename

    os.rename(filename, dst)