# Crappy Resource Monitor
___
This is the page of CRM, a resource monitor I've been working on, it doesn't have much features yet, I hope it doesn't end like the rest of repos in my account.

My idea for this script is doing something similar to htop, but without the process list, just a few numbers and bars that tell you how much of your system's resources you've been using. In short, a resource monitor (sort of) aligned with the UNIX philosophy.

Things that CRM does:
* Show CPU frequency.
* Show CPU utilization percentage.
* Show how many processes are running.
* Show how much RAM is being used.
* Show the temperature of the system.

Things that CRM does **not** do:
* Show CPU frequency per core.
* Show CPU utilization per core.
* Show GPU data.
* Work on Windows.
* Show each process.
## Sounds craptastic! How do I join?
___
To install it simply run this:
```shell
git clone https://github.com/AxelElRojo/CRM/
cd CRM/
sudo chmod +x install.sh && ./install.sh
```
The script will ask you if you want to delete the cloned folder, if you say yes, it should be deleted automatically and then send you to your ~/ .
