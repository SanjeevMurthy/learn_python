# Python program to explain os.rmdir() method

# importing os module
import os
import shutil

# Directory name
directory = "0297"

# Parent Directory
parent = "SOAP"

path = os.path.join(parent, directory)

try:
	shutil.rmtree(path)
	print("Directory '% s' has been removed successfully" % directory)
except OSError as error:
	print(error)
	print("Directory '% s' can not be removed" % directory)
