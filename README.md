# Github Replica
It's a web based application that forks it's own repository into user's repositories list using only one button as interactive element in the user interface.

Application uses OAuth to request permission for interactions with user's GitHub repositories and forks actual app repository. The application itself doesn't ask for any password and doesn't require access to  user's private repositories, however user should provide the password for Github authentication tool.

When user authenticates himself using GitHub authentication tool, Replica app gets Github access token that has additional permissions for creating, editing and forking repositories. 
Using this token Replica forks repository with it's source code like it could do the user himself.
User can review the results via URL that application provides in the end of it's work. 

## Stack
This application is built using Django framework, Bootstrap and OAuth.

## Requirements
1. User should have GitHub account.
2. Github Replica uses python language version 3.4 or above. You can install it using this [article](https://realpython.com/installing-python/). 
Also user already should have installed [pip](https://github.com/pypa/pip), [virtualenv](https://github.com/pypa/virtualenv) and  [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) in order to deploy application locally.

## Installation
Please follow these step if you want to run the local copy of the app:

I. Create a folder to fetch application source code. Like this:
```
$ cd ~ && mkdir github_replica && cd github_replica
```
II. Fetch application repo in the current folder:
```
$ git clone https://github.com/bddh/github_replica.git
```
III. Create virtual environment to isolate application specific dependencies. Please keep in mind that this instruction will not work for windows user. If you are using windows try to find another way to install virtual environment with python 3.4 or above.
```
$ virtualenv venv -p /usr/bin/python3
```
IV.  Enable virtual environment
```
$ source venv/bin/activate
```
V. Install application dependencies it the isolated environment
```
$ cd github_replica && pip install -r requirements.txt
```
VI. Create necessarry database tables:
```
$ python manage.py migrate
```
VII. Run application's local server:
```
$ python manage.py runserver
```
## Usage
If you are done with installation process, you can visit [http://localhost:8000/](http://localhost:8000/) url and see Github Replica working.
