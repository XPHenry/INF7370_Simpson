import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)


# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'a')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt

for pathAndFilename in glob.iglob(os.path.join(current_dir+"/Images/008", "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write("./Images/008/" + title + '.jpg' + "\n")

for pathAndFilename2 in glob.iglob(os.path.join(current_dir+"/Test", "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename2))
    file_test.write("./Test/" + title + '.jpg' + "\n")
