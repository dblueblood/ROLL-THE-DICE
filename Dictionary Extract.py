"""
Author: Ayo Asekun
Date Created: Oct 18th, 2019
Last Date Modified: Oct 19th, 2019
Program Description: Extracting & Analyzing a python dictionary
PsuedoCode:
<START PROGRAM>
INPUTS: Using provided files; Extract source files & save data to reachable directory
        "path" = file path of data on OS HD

    Variables:
          path = location of file in directory
            MC = Python readable format
           ext = print out of file

PROCESS: 3 Main actions performed in Analysis
            POINT 1:  Using os import to access files, print file to view for easy access
            POINT 2: 'if' & 'else' loops:
                 + Determine length of file
                    - lines & Characters
                 + Determine if lowercase 'a' in file
                 + Determine if uppercase 'A' in file
                 + Determine if uppercase 'a' not in file
            POINT 3:  Determine the file name

OUTPUTS:  (1) Full readable file in Python terminal
          (2) Count of lines/Newlines in File
          (3) Count of total noo. of characters in file
          (4) Result of request if 'a' in File
          (5) Result of request if 'A' in File
          (6) Result of request if 'a' not in File
          (7) Directory/Host Name of File

<END PROGRAM>:  End of Pay-roll


"""
import os

# Import Library
path = "C:\\Users\\ayoas_spsqm2u\\PycharmProjects\\morsecode.py"
MC = open(path, "r")
ext = MC.read()
print("=========== FILE IMPORT TO BE ANALYZED ===========")
print(ext)
print("===================================================")
# To print the number of lines in imported file
MC = open(path, "r")
print("No. of lines in File")
print(len(MC.readlines()))
print("===================================================")
# To print total no. of elements in in imported file
print("No. of characters in File")
MC = open(path, "r")
print(len(MC.read()))
print("===================================================")
# To confirm if lowercase 'a' is in imported file
MC = open(path, "r")
print("If lowercase 'a' in file, it will print")
x = "a"
if x in MC.read():
    print("Value "+x+" is present")
else:
    print("No Value")
print("===================================================")
# To confirm if uppercase 'A' is in imported file
MC = open(path, "r")
print("If capital letter 'A' in file, show below")
x = "A"
if x in MC.read():
    print(x)
else:
    print("*Value Unavailable*")
print("===================================================")
# To confirm if lowercase 'a'( or any value required) is not in imported file
MC = open(path, "r")
x = "a"
print("Is '" + x + "' in the file; True/False")
if x not in MC.read():
    x = False
    print(x)
else:
    x = True
    print(x)
print("===================================================")
# Pulling the name of above file from the directory
MC = open(path, "r")
path2 = os.path.basename("C:\\Users\\ayoas_spsqm2u\\PycharmProjects\\morsecode.py")
print("Name of file being worked on: " + path2.upper())

MC.close()


















