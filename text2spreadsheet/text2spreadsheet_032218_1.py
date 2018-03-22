# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 text2spreadsheet_032218_1.py FOLDERPATH

import openpyxl, sys, os

try:
	from openpyxl.cell import column_index_from_string,get_column_letter
except ImportError:
	from openpyxl.utils import column_index_from_string,get_column_letter

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# PARSE COMMAND LINE
#####################################

# get the folder name / folder path containing the text files that will be put into the spreadsheet

folder_to_process = sys.argv[1] # this should be the filename/file path

#####################################
# END PARSE COMMAND LINE
#####################################

#####################################
# SCAN FOLDERS/FILES
#####################################

# analyze the folder
# build a list of all the text files in the folder
# construct the list so that it is file paths to each text file

# get the absolute file path of the current working directory of program
abs_cwd_file_path = os.path.abspath('.') # set the destination file path to be the current working directory or cwd

# a list of all folders and subfolders to be analyzed
folder_path_list = [] # a list to hold all finalized folder paths (not folder names)

# a list of all files to be analyzed
file_path_list = [] # a list to hold all finalized folder paths (not folder names)

def scanFolder(foldername_path):
	# this function scans the parent folder and subfolders
	# it then adds them to a list so that its files can be scanned individually

	# `foldername_path` should actually be a string path to folder
	# `dirPath` - the directory path leading up to the folder's name (yet not including it), should be an absolute path I'd say
	
	# as we get deeper and deeper into subfolders it should add onto the folder's path string that we pass to it so accuracy should be maintained

	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isdir(new_path): #if the file is a folder
			folder_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def scanFile(foldername_path):
	# the file scanner that gets all of the files and pushes them into a list after we get the full string path to it
	
	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isfile(new_path): #if the file is a folder
			file_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def generate_targets(user_folder_input):
	# run an initial scan of the upper level main folder tree
	# find subfolders if any
	scanFolder(user_folder_input)
	# find matching files or just files
	scanFile(user_folder_input)

	# then scan all the sub folders by cycling through folder_path_list until no more subfolders are added
	# this should keep going until no more subfolders are analyzed
	# then scan all the files by cycling through folder_path_list until no more subfolders are added/left
	for subfolder in folder_path_list:
		scanFolder(subfolder)
		scanFile(subfolder)

	logging.debug('folder_path_list is now:  ')
	logging.debug(folder_path_list)
	logging.debug('file_path_list is now:  ')
	logging.debug(file_path_list)

generate_targets(folder_to_process) # create paths to all files we want to process

#####################################
# END SCAN FOLDERS/FILES
#####################################

#####################################
# CREATE SPREADSHEET
#####################################

# analyze the files now stored in `file_path_list`
# the function should go through a list of text files (i.e. text file paths)
# then write them to a spreadsheet

def text2spreadsheet_generator(file_path_list):
	pass



#####################################
# END CREATE SPREADSHEET
#####################################


#####################################
# EXECUTION
#####################################



#####################################
# END EXECUTION
#####################################



