from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

'''def get_requiremet(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements'''

   
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "mongodb_connector"
PKG_NAME= "MongoDB-Connect"
AUTHOR_USER_NAME = "sunnysavita10"
AUTHOR_EMAIL = "sunny.savita@ineuron.ai"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    
    
)