"""
Instead of creating project structure by manually, we will use template.py to create it. Inside this file we will write 
a pythonic way to create the folder structure and logging mechanism.

"""



import os
from pathlib import Path
import logging

#Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)

#setting the configuration of logging mechanism
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


"""
Project Structure is as follows:
1. Create folder "Src"(Source), inside source it will contain our project_name as folder.
2. .github/workflows to generate file for executing CI/CD pipeline deployment via a "yml" file
"""
project_name = "Text_Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #this file will be used for CI/CD deployment yml file
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    #based on the operating system it's been running on it will adjust the '/'(forward or backward)
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path) #output file directory and file name separately
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory:{file_dir} for the file {file_name}")

    #if my file path doe not exist or it's size is 0 then only we will create the file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
            logging.info(f'Creating an empty file:{file_path}')

    else:
        logging.info(f"{file_name} already exists!")
