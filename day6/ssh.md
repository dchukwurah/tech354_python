
# Creating SSH keys and Pushing to a new Github REPO

# 1. Creating your .ssh folder


#### Starting in terminal you will need to go to the home directory by using cd ~
#### In here you will need to check if you have a .ssh folder. It will be hidden so will need to use ``` ls -a ```
#### It should appear near the top of the list as it is a hidden file.
#### If there is no file you can create one using ```mkdir .ssh```

# 2. Creating SSH Key!
[![Screenshot 2023-09-26 at 09.55.13.png](..%2F..%2F..%2FDesktop%2FScreenshot%202023-09-26%20at%2009.55.13.png)Screenshot 2023-09-26 at 09.55.13.png](..%2F..%2F..%2FDesktop%2FScreenshot%202023-09-26%20at%2009.55.13.png)
#### To  create your key pairs, to do this you need to use the following command. ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
#### -t rsa sets the type of keygen you require (rsa is default)
#### -b 4096 determines the byte length
####  -C "your_smail@example.com comments the end of the key with a note (commonly your email)
#### Once you run this command you should see the following response:
#### Generating public/private rsa key pair.
#### Enter file in which to save the key (/c/Users/dchukwurah/.ssh/id_rsa):
#### Enter passphrase (empty for no passphrase):
#### Enter same passphrase again:
#### Your identification has been saved in /c/Users/dchukwurah/.ssh/id_rsa
#### Your public key has been saved in /c/Users/dchukwurah/.ssh/id_rsa.pub
#### The key fingerprint is:
#### ********************************************** dchukwurah@live.com
```The key's randomart image is:
+---[RSA 4096]----+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+----[******]-----+
```
#### You can enter the name of the file to which you want your ssh key to be saved (leave blank by pressing enter and the default "id_rsa" will be the name)
#### Enter passphrase, enter the passphrase you want (recommended to just leave blank and press enter)
#### In place of ******* will be where your public key is generated as well as a randomart image found inside the square
#### Once you've done this, do ls to check that two files have been generated in. (One should have .pub referring to the public key, the other is your private)
#### Do not share your private ssh key or your file name


# 3. Connecting your SSH key to GitHub
#### On github go to your profile and click on settings 

![Screenshot 2023-09-26 at 10.17.34.png](..%2F..%2F..%2FDesktop%2FScreenshot%202023-09-26%20at%2010.17.34.png)
#### Go into your SSH and GPG keys tab and click on New SSH key 

![Screenshot 2023-09-26 at 10.18.40.png](..%2F..%2F..%2FDesktop%2FScreenshot%202023-09-26%20at%2010.18.40.png)
#### When added a new key, give the key a title, set the type to Authentication (default) and enter your PUBLIC key in the key section
#### To copy over your public key use the following in terminal ```cat ~/.ssh/id_rsa.pub | pbcopy``` This will copy your Public key in the correct format (replace id_rsa.pub with your public key)
#### Click Add SSH Key to confirm.

![Screenshot 2023-09-26 at 10.11.48.png](..%2F..%2F..%2FDesktop%2FScreenshot%202023-09-26%20at%2010.11.48.png)
# 4. Connecting PyCharm to GitHub
#### In the terminal in PyCharm, enter the directory which your repo is, start by entering
#### eval `ssh-agent` (Output: Agent pid ***)
#### Add in your private key to connect with ```ssh-add ~/.ssh/id_rsa```
#### Allow access for Github to connect with your ssh key ```ssh -T git@github.com```
#### Setting your pycharm git repo as your origin link to the GitHub repo ```git remote add origin git@github.com:dchukwurah/github_SSH.git```
#### Check that the connection is complete with ```git remote -v```
#### Expected Output:
#### origin  git@github.com:dchukwurah/github_SSH.git (fetch)
#### origin  git@github.com:dchukwurah/github_SSH.git (push)
#### Save your files and pushing your local repo to GitHub with ```git add .```  -> ```git commit -m "comment here"``` -> ```git push -u origin main```