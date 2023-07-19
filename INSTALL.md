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
```
