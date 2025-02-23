from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
# The -e . in requirement will automatically trigger this setup.py file


def get_requirements(filepath: str):
    '''This function will return a list of requirements'''
    requirements = []
    print("Setup is running")
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove spaces/newlines
    
    # Ensure no empty strings or unwanted dependencies like warnings
    requirements = [req for req in requirements if req and req != '-e .']

    print("Requirements are:", requirements)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Rudresh',
    author_email='rudreshdharkar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')  # Ensure file name matches
)