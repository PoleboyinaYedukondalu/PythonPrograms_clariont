#File handling concepts 
#written by Yedukondalu

# to cut and past the file into one location to another location with the name changing of that file : 
import os
import shutil

#Createing a new folder :
os.mkdir("d:\\FilecopyYD")

#Current Working Directory :
os.chdir("d:\\FilecopyYD")

srcPath = "d:\\\FileConcept1.pdf"
destpath= "d:\\FilecopyYD\\FileHandling.pdf"
os.rename(srcPath,destpath)