import shutil

shutil.copy("intro_ai.pdf", "ai_intro.pdf")
# this function copies the file , if the destination location already exist, original file will be over wriiten

# copy() used for file and copytree() used for folder/ entire directory

# shutil.copy2()
# similar to copy() but it also preserves more metadatas about the original file, such as the timestamps


# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
# Recursively copy an entire directory tree rooted at src to a directory named dst and return the destination directory. All intermediate directories needed to contain dst will also be created by default.


# shutil.move(src, dst, copy_function=copy2)
# Recursively move a file or directory (src) to another location and return the destination.

# shutil.rmtree(src) 
# delete directory/ folder  can't delete file using shutil module, we can do it using os module( os.remove() )




