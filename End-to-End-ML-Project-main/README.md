# End-to-End-ML-Project

# Step 1: Set Up Git in VS Code
1. Install Git

    Download from: https://git-scm.com/downloads

    Install with default settings (keep "Add Git to PATH" selected).

2. Install VS Code

    Download from: https://code.visualstudio.com/

    Install it and open your project folder.

3. Verify Git Installation

    Open VS Code → Terminal (Ctrl + `).

    Type:

        git --version


    You should see something like:
    git version 2.xx.x

4. Configure Git (First-Time Setup)

    Set your username and email (used in commits):

        git config --global user.name "Your Name"
        git config --global user.email "youremail@example.com"

5. Link Local Repo to GitHub

    In VS Code terminal:

        git remote add origin https://github.com/username/repository-name.git


    Push your code:

        git branch -M main
        git push -u origin main


1.create one folder like 'House price'
2.creat a one file name 'setup.py'

#setup file
  requirements to setup for author details, and packages 

## Common Commands to Use with setup.py

Install the package (recommended if you're just setting it up):

        python setup.py install


Develop mode (editable install) – Good for ongoing development:

        pip install -e .


(or)

        python setup.py develop

New packages install in house_price
Logger
Exception handling