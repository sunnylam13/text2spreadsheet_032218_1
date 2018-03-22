# Scratch Notes and Log

## Thursday, March 22, 2018 12:45 PM

`readlines()` File object method to return list of strings

one string per line in the file

first file output to column 1, row 1

second line to column 1, row 2, etc

next file read with `readlines()` should be output to column 2...

etc...

## Thursday, March 22, 2018 12:55 PM

for data on file reading, see this project

	file:///Users/sunnyair/Dropbox/python_projects/selective_copy_021818_1/

## Thursday, March 22, 2018 1:09 PM

Still need to create a bunch of files in a folder for testing...

Put it in the `/tests` folder...

	tests/testFolder1

	../tests/testFolder1 # one `.` is cwd, `..` is into the project root

## Thursday, March 22, 2018 2:55 PM

[Python 3 readlines()](https://www.tutorialspoint.com/python3/file_readlines.htm)

This method returns a list containing the lines.

--------------------------------

EXAMPLE:  The following example shows the usage of readlines() method.

Assuming that 'foo.txt' file contains following text:

This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line

	#!/usr/bin/python3

	# Open a file
	fo = open("foo.txt", "r+")
	print ("Name of the file: ", fo.name)

	line = fo.readlines()
	print ("Read Line: %s" % (line))

	line = fo.readlines(2)
	print ("Read Line: %s" % (line))

	# Close opened file
	fo.close()

result

	Name of the file:  foo.txt
	Read Line: ['This is 1st line\n', 'This is 2nd line\n', 
	   'This is 3rd line\n', 'This is 4th line\n', 'This is 5th line\n']
	Read Line: 

this generates a list of strings if only readlines() is used with no args

it produces a specific string if a number arg is used...

--------------------------------

### Searches

https://www.google.ca/search?q=readlines()+python+3&oq=readlines()&aqs=chrome.2.69i57j0l5.2824j0j7&sourceid=chrome&ie=UTF-8


