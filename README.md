# website-watcher-script

### Introduction

This script will watch a website, save its contents to a specified text file, compares this file's contents to the website contents at the next visit and send an e-mail if there are differences.Written as a modification of code by user <a href="https://github.com/n1try">@nitry</a>. 

### Usage

- In the script file, add the following details:

```python3
#################################################
# Login details of any *gmail* account
bot_mail = '' # email account used to send notification mail
password = '' # password of the sender account
target_mail = '' # target address for notification
#################################################
```

- Run the script :

```python3 <PATH_TO_SCRIPT>watcher.py <URL_TO_WATCH> <TOLERANCE (optional)>```

- Here, ```URL_TO_WATCH``` would be the website you want to watch for changes.
- ```TOLERANCE``` is a value that indicates # of characters changed. A default value of 100 is taken, unless specified. Different websites may need different tolerance levels, depending on the kind of content they serve, and the kind of changes you are looking for.
- 
- To create a cronjob : `crontab -e` and add ```@hourly python3 <PATH_TO_SCRIPT>watcher.py <URL_TO_WATCH> <TOLERANCE (optional)>```, for hourly visiting the said URL, ignoring changes less than the TOLERANCE specified.