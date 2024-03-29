# Local Installation

## Check that you have git installed

* Open up your favorite terminal - PowerShell (Win-R powershell) on Windows 10 example here

```Powershell
PS C:\Users\vsaules\Github> git --version
git version 2.41.0.windows.3
```
* Above shows the most current version for summer of 2023.
* Any git version above 2.23 should be fine
* `C:\Users\vsaules\Github` is user specific could be `D:\Users\Alice\MyDocuments` if your user name is Alice and you store your documents in D drive

### If you do not have git, install it from: https://git-scm.com/

* For windows installation choose 64 bit installer and choose default options
* You might need to restart your terminal to see changes

## Check that your current directory is not under git version control

**It is crucial that you clone this (and any other) git project into a directory that is currently not under git version control.**
This is the most common mistake I've seen students make when using git for checking out external projects.
```Powershell
PS C:\Users\vsaules\Github> git status
fatal: not a git repository (or any of the parent directories): .git
```
* Above fatal message is what you want to see - means there is no git in current folder.

* If you have many projects that you clone from github it is useful to name directory that holds these different projects something like Github here - name is not super important it could be My_Github_Projects or anything else
* If you see a different message (something like On branch main) you need to go up to a folder that is not under git version control.

## Cloning project

Enter the following command to clone the project into current folder

```Powershell
PS C:\Users\vsaules\Github> git clone https://github.com/ValRCS/BSSDH_2023_workshop.git
Cloning into 'BSSDH_2023_workshop'...
remote: Enumerating objects: 155, done.
remote: Counting objects: 100% (155/155), done.
remote: Compressing objects: 100% (129/129), done.
remote: Total 155 (delta 95), reused 59 (delta 25), pack-reused 0
Receiving objects: 100% (155/155), 48.97 KiB | 1.06 MiB/s, done.
Resolving deltas: 100% (95/95), done.
```
Exact numbers will likely differ but you should be seeing many done messages like above.
If you see `fatal: destination path 'BSSDH_2023_workshop' already exists and is not an empty directory.` this means that you already cloned this project or have a BSSDH_2023_workshop folder already in your current folder.

### Alternatives to cloning from command line

*  You could have used Visual Studio Code built in git support and chosen Clone Git Repository
*  PyCharm has similar functionality for cloning git projects
*  You could have used external graphical git tool, such as Github Desktop or any other tool from: https://git-scm.com/download/gui/windows

## Navigate to project folder

```Powershell
PS C:\Users\vsaules\Github> cd .\BSSDH_2023_workshop\
```
### Alternative open BSSDH_2023 folder in your IDE

You can also open BSSDH_2023 folder in your favorite editor/IDE such as Visual Studio Code
Once your project is opened, open a terminal window inside IDE (it is functionally the same as external terminal window)

## Check that you are in the correct directory/folder

```Powershell
PS C:\Users\vsaules\Github\BSSDH_2023_workshop> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
Above message means your project is current with Github version. You are now ready to setup Python!

## Check that you can access Python and its package manager from command line

```Powershell
PS C:\Users\vsaules\Github\BSSDH_2023_workshop> python --version
Python 3.11.4
PS C:\Users\vsaules\Github\BSSDH_2023_workshop> pip --version
pip 23.1.2 from C:\Program Files\Python311\Lib\site-packages\pip (python 3.11)
```
Version numbers should be:
* at least 3.9. for python 
* pip any version from 22 onwards

### Python not found
If you get error for `python --version`
You either have no Python or your operating system does not know where it is.

#### Install Python if you do not have it
* install Python from https://www.python.org/ - choose 64 bit installer, also choose option to add to System Path when installing

#### You know you installed Python - but python --version does not work
You know you have Python somewhere on your computer.
If it is recent Python, there is no need to install it again.

Main thing is that you figure out where python.exe file is found it is most likely in a folder such as `C:\Program Files\Python311\`
Similarly pip.exe should be found a in folder such as `C:\Program Files\Python311\Scripts`

#### If you do NOT know where you installed Python you can find out by Search

* Win-E -> opens File Explorer -> choose disk drive such as C: -> enter python.exe in Search in upper right corner and wait a few minutes for Windows to find python.exe
* It is possible that search finds multiple copies of python.exe (it is a small 100-500kb file)
* Note which python.exe file is most recent most likely it will have Python310 or Python311 in the folder name
* Now check the subfolder Scripts of the folder where python.exe was found.
* Scripts subfolder should contain pip.exe 

* Note the full path names of these folders (one with Python311 at end , one with Python311/Scripts at the end)

#### Update System Environment with Python and pip paths 
* Find System Enviroment variables (Win-S system env) -> Edit the system enviroment variables
* You will see System Properties navigate to Advanced
* Click on Environment Variables button
* In Environment Variables window navigate to Path in the System Variable sub-window, click on Edit
* Click New button and create a new entry for your python path such as `C:\Program Files\Python311`
* Similarly make another entry for pip path such as `C:\Program Files\Python311\Scripts`

Close (OK) all System enviroment variables windows.
Restart your terminal and check `python --version` and `pip --version` again .

### Create Virtual Environment for this project

It is a good practice to setup separate environments for different Python projects.
That can help avoid version conflicts for external libraries.

```Powershell
PS C:\Users\vsaules\Github\BSSDH_2023_workshop> python -m venv venv
```
The above command will create a venv folder (with subfolders) in your current folder, could take some seconds, but should be less than minute.

### Activate virtual envirnoment

Powershell example (there are other activate scripts for bash terminal and others)
```Powershell
PS C:\Users\vsaules\Github\BSSDH_2023_workshop> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop>
```
You should be seeing (venv) prefix before your current path.

### Check your virtual environment

```Powershell
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop> python --version
Python 3.11.4
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop> pip --version
pip 23.1.2 from C:\Users\vsaules\Github\BSSDH_2023_workshop\venv\Lib\site-packages\pip (python 3.11)
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop> pip list
Package    Version
---------- -------
pip        23.1.2
setuptools 65.5.0
```
Version numbers are not super important but should be close to what is shown above. (current for summer of 2023)

### Installing libraries from requirements.txt

There is a requirements.txt plaintext file in main folder of the project. It holds information on external libraries.
Let's install ALL libraries from this file at once.

WARNING: This will take 5-30 minutes depending on how fast your computer is and how fast your SSD is.
Installation will take up around 1GB of drive space

```Powershell
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop> pip install -r requirements.txt
```
Go grab a coffee or tea or your favorite beverage as pip works hard to download and install required packages/libraries and install their dependencies(other libraries) automatically.

### Anaconda conda alternative to pip

If you have been using Anaconda distribution, it is most likely that most libraries are already installed.

You can also set up virtual environments with conda instead of pip and install libraries with conda.
Advantage of conda is that it has better tested packages but not every package will be the latest one.
Conda use is beyond scope of this tutorial but you can check tutorial: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

## Verifying that installation was successful

Run 
```Powershell
(venv) PS C:\Users\vsaules\Github\BSSDH_2023_workshop> python .\scripts\test_python_libraries.py
Current date and time: 2023-07-19 15:33:45.625281
Python version 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
Pandas version 2.0.3
Numpy version 1.24.4
Requests version 2.31.0
Gensim version 4.3.1
Scikit-learn version 1.3.0
Plotly version 5.15.0
spaCy version 3.6.0
Imports finished at: 2023-07-19 15:33:48.192709
```
If the script runs without errors you are good to go!

### Verifying that Jupyter notebook enviroment works

If you are using Visual Studio Code you might want to check that you can run local notebooks

* Open VS Code in BSSDH_2023_workshop folder, and open test_python_setup.ipynb in notebooks subfolder

* You can now run the notebook, but you might be asked which python kernel to use. 
* There might be `Detecting kernels` message in the upper right corner you can click on that one and select correct kernel.
* Select one that is located in venv folder of BSSDH_2023_workshop parent folder

If notebook runs without error you are super ready to go! Congratulations!











