import os
import tarfile

#### Configure your settings here ... ####
directory = "./0Lv5/archives"
##########################################

extracted_dir = os.path.join(directory, "extracted")
unzippedDirExists = os.path.exists(extracted_dir)
if not unzippedDirExists:
    os.makedirs(extracted_dir)
    print("Extracted directory {} is created!".format(extracted_dir))
    
for file in os.listdir(directory):
    if file.endswith(".tgz"):
        tar = tarfile.open(os.path.join(directory, file), 'r')
        for item in tar:
            tar.extract(item, extracted_dir)
        continue    
