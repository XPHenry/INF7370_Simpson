import os

path1 = "Images/010/"
name1 = "krusty_"



for filename in os.listdir(path1):
    pic, src = filename.split("_")
    dst = path1 + name1 + src
    filename = path1 + filename

    os.rename(filename, dst)