# What is SSH

#### Secure Shell - 

#### USes Private and Public Key

#### Private stored on your computer local in server

#### Uses private key to decode, very safe way to encrypt data as peoople cant crack in as it would take a long time
#### also its super difficult
#### properly automate things
#### rm -rf .ssh1 to force delete things

#### go into .ssh folder -> make an SSH key pair -> ssh-keygen -t rsa -b 4096 -C "dchukwurah@live.com" ->
#### generates a key 
#### run an agent using eval `ssh-agent`
#### agent PID = processid
#### ssh-add ~/.ssh/github_test
#### ssh -T git@github.com


[.gitignore](..%2Fvenv%2F.gitignore)