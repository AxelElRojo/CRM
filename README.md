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
Before installing, make sure `~/.local/bin/` is in your PATH.

To install it simply run this:
```shell
git clone https://github.com/AxelElRojo/CRM/
cd CRM/
sudo chmod +x install.sh && ./install.sh
```
The script will ask you if you want to delete the cloned folder, if you say yes, it should be deleted automatically and then send you to your ~/ .
## How does the *config.py* work?
Have you ever used suckless's programs? It's the same principle, there are some variables in the config file and setting them to different values changes the program's behaviour, obviously, suckless's programs have much more configuration options, but since this program is more limited, it doesn't have as many options.
### What do the variables mean?
There are comments explaining their meaning and use, but I'll explain them with more detail here:
* bar: Dictionary whose variables control the bar appearance:
 * char: This variable is the character used to fill the bars.
 * usedColor: Color for the characters that represent used resources (ie: left side of the bar).
 * freeColor: The opposite of usedColor.
* updateInterval: Time that takes to update the info.
* fillChar: Characters used to center the titles.
* titles: Set to True to enable titles, False to disable them.
* CPU/MEM/TEMP_BAR: Set to True to enable the desired bar, False to disable it.
* CPU/MEM/TEMP_INFO: Set to True to enable all information on the selected variable, False to disable it.
