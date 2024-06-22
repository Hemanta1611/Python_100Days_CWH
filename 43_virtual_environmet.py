'''
A virtual environment is a tool used to isolate specific python environments on a single machine, allowing you to work
on multiple projects with different dependencies and packages without conflicts. This can be especially useful when 
working on projects that have conflicting package versions or packages that are not compatible with each other.

'''


"""
# Create a virtual environmet ( "myenv" is virtual environment name, we can give any name to this: )
python -m venv myenv

# Activate the virtual environment (Linux / macOs)
source myenv/bin/Activate

# Activate the virtual environment (Windows)
myenv\Scripts\Activate.bat  # use .ps1  if we are using power shell

# Deactivate the virtual environment
deactivate

# to create a python file using command line 
New-Item -ItemType File -Name hello.py

# pip freeze :   give all the detail of package versions
# pip freeze > requirement.txt :  it will generate .txt file where these detail will be stored
# pip install -r requirement.txt :  it will install all package with that version written in requirement.txt


"""