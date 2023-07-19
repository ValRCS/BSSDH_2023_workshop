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
* Note which python.exe file is most recent most likely it will have Python310 or Python311 in the name
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












