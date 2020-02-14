#  CS 1XA3 Project01
This project involves working with bash scripts and functions via user prompted input.

 ## Contents 
 1. Requirements
 2. Installation
 3. Usage
 4. Features
 
## Requirements
Bash is required on your local machine.
## Installation
Clone the repository and follow the instructions in the Usage section.
## Usage

Execute this script from project root with:

`chmod +x CS1XA3/Project01/project_analyze.sh`
`./CS1XA3/Project01/project_analyze.sh`
 
 When executed the user will be presented with a menu, from which they can select whichever function they'd like to call by entering the corresponding number (and NOT the name of the function). 
 ```
 ~ ./project_analyze.sh
 # The user is running the script and this is what it should look like.
 1) FIXME Log
 2) File Size List
 3) File Type Count
 4) Quit
 Please choose what you want to do:
 ```
 ## Features
 These are the features that have been implemented in the script.
## Feature 1 - Interactive Script
* Description: This feature provides a menu of the features for the user to use and is implemented by the select statement.
* Execution: This feature is executed when the program is run.
* Reference: Some code was taken from [Select Loop](https://bash.cyberciti.biz/guide/Select_loop)

## Feature 2 - FIXME Log

* Description: Creates the file **fixme.log**   in the Project 01 directory
	finds every line in the repo that contains the word **"#FIXME"**
	Puts the list of file names separated by a newline in **fixme.log**
* Execution: This feature is executed by selecting it from the menu.
* Reference: Got help from one of the TA's (Sharon).

## Feature 3 - File Size List
* Description: Lists all files and their sizes in the repo in a human readable format. (i.e KB, MB, GB, etc) in descending order.
* Execution: Choose number 2 at first and all your files including
the hidden files will be listed.
* Reference: Some code was taken from [List Files]( https://www.tecmint.com/list-files-ordered-by-size-in-linux/)

## Feature 4 - File Type Count
* Description: Prompts the user for an extension that they want to look for 
in their repo. The output is the number of files with that extension in their repo.
* Execution: Choose number 3 and give the script any extension that
you want to know the number of.

## Custom Feature 1:

### Find movies 
* Description: This feature is used when you want to find a movie or an episode of a tv show when you don't remember the name or just remember part of the name. Suppose you want to watch a movie that contains the word **her**. Give it to the script and it will show all the videos on your disk which contain **her**. 
## Custom Feature 2:
###  Organize downloads
* Description: In order to keep your downloads organized this script will sort your files by type into corresponding folders/directories periodically. If the target directory is not available the user will be asked if they want it to be created or not. (e.g all jpg files will be moved to a folder named jpg. )
## Quit
By choosing this feature, the user exits the program.
