# Orgnice
Orgnice is a Python script that can monitor a specified directory for changes and new files. When a new file is detected, the program creates a folder with the same name as the file's extension and moves the file to that folder. Additionally, the program can take a configuration YAML file in which the user can define common groups for similar types of files. For example, all videos in MP4, MKV, and other formats can be grouped together in a "Video" folder, regardless of their individual extensions. This helps keep your files organized in a more intuitive and meaningful way. You can specify the directory to monitor, the extensions to group, and the common groups in the configuration file. The program runs in the background and requires no interaction, making it an ideal solution for those who need to manage large numbers of files regularly.

* Requirement is Python WatchDog Library and PyYAML Library.

    `pip3 install watchdog`
    `pip3 install pyyaml'

Steps:

1. clone repository in a directory.
2. Copy config.yml file to $HOME/.config/orgnice/
3. Copy downloaded orgnice executable from dist/ directory to $HOME/.local/bin/ or /usr/bin/
4. (optional) To run it as a background process everytime when you login, just add "orgnice" command to the autostart.sh file (comes in Windows Managers) or by taking steps specific to you DE.

NOTE :
* It need a config.yml file to run.
* By default it will use the config located under you $HOME/.config/orgnice/
* In case of bug create an Issue.
* It ignores dotfiles.

FLAGS :

-c  : (stands for config) To specify configuration file

-o  : (stands for 'once') To run it once. i.e. when you don't want to run it as a background process.


# Define a config file in which with syntax
* The config file is a YAML file.
* The three main necessary keys are 
    - dirs : Under this key you can define the directories to watch for changes
    - groups : Under this key you can define other key value pairs which signify groups you want to have instead of using extension name as the directory name
    - ignore : This key under groups key is special as it ignores the files with specified extensions.

* Example of config.yml
[Link](https://github.com/Ethan0456/orgnice/blob/main/config.yml)
