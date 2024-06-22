# import os

# if not os.path.exists("C:\\Users\\heman\\Python_CWH\\JPG_FILE"):
#     os.mkdir("C:\\Users\\heman\\Python_CWH\\JPG_FILE")

# files = os.listdir("C:\\Users\\heman\\Python_CWH\\JPG_FILE")
# num_files = len([f for f in files if os.path.isfile(os.path.join("C:\\Users\\heman\\Python_CWH\\JPG_FILE", f))])
# print("Number of files:",num_files)

# for i, filename in enumerate(os.listdir("C:\\Users\\heman\\Python_CWH\\JPG_FILE"), start=1):
#     if os.path.isfile(os.path.join("C:\\Users\\heman\\Python_CWH\\JPG_FILE", filename)):
#         new_filename = str(i) + ".jpg"
#         os.rename(os.path.join("C:\\Users\\heman\\Python_CWH\\JPG_FILE", filename), os.path.join("C:\\Users\\heman\\Python_CWH\\JPG_FILE", new_filename))
#         print(f'Renamed: {filename} to {new_filename}')


import os

files = os.listdir("JPG_FILE")

for index, file in enumerate(files, start=1):
    if file.endswith(".jpg"):
        os.rename(f"JPG_FILE/{file}", f"JPG_FILE/{index}.jpg") 

