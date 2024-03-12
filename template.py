import os
from pathlib import Path
import logging # because I want to log all the information during run time as well that is why i am using logging
# creating logging string 
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]:%(message)s:')

project_name = "textSummarizer"
# mentioning all the files that are going to be processed or being used
list_of_files = [
    ".github/workflows/.gitkeep", #will use this in deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockrfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    

]

for filepath in list_of_files:
    filepath =  Path(filepath) # it will provide the file filepath ny ignoring // rules
    filedir, filename = os.path.split(filepath) # it will provide the directory and filename of the current and also split the path
    
    #lets check if the file directory is not empty 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # if the file directory is not empty then it will create the directory
        logging.info(f"Creating directory: {filedir} for the file : {filename}")

#now folder creation is done, lets create the files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
         with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"The file: {filepath} already exists")    