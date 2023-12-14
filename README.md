# Connect BASH to GitHub
## Create Github Account

## Install Git
In Ubuntu:
```bash
sudo apt-get install git
```
In Fedora:
```bash
sudo dnf install git
```
In Windows WSL:
Assume that the WSL is debian based, then:
```bash
sudo apt-get install git
```
## Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "
```
## Create SSH Key
```bash
ssh-keygen -t rsa -b 4096 -C "
```

## Add SSH Key to GitHub
```bash
cat ~/.ssh/id_rsa.pub
```
Copy the output and paste it to GitHub SSH Key

## Create Repository
You can create your local repository by:
```bash
mkdir ~/git
cd ~/git
mkdir <repo_name>
cd <repo_name>
git init
```

## Clone Repository
Alternatively, you can clone a repository from GitHub:
```bash
git clone <repo_url>
```

# Git Commands
## Add Files
```bash
git add <file_name>
```
## Commit Changes
```bash
git commit -m "commit message"
```
## Push Changes
```bash
git push
```
## Pull Changes
```bash
git pull
```
## Check Status
```bash
git status
```
## Check Log
```bash
git log
```