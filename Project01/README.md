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
 ###  Track URL
* Description: Track a given url and if there were any changes since the last visit, the new changes will be emailed to the specified address.
* Execution: TBA

## Custom Feature 2:

### Movie Search
* Description: Given a movie title, if there is more than one match the script will return the list of matches for the user to choose from and if not, the user will be given a synopsis of the movie form the Internet Movie DataBase [IMDB](imdb.com)
* Execution: TBA

## Quit
By choosing this feature, the user exits the program.
