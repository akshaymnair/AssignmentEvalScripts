#!/usr/bin/python
# python 3
# author: Akshay - amurale1@asu.edu TA - CSE100
# Usage: copy this script file outside the folder which contain the downloaded submission files from blackboard
import os 
import shutil

# create individual folder for each student
# copy all files of each student's submission into individual folder

def main(): 
        #remove Assignment6 prefix from the file names
        for filename in os.listdir("test"):
                 
                dst =filename[12:]
                src ="test/"+ filename 
                dst ="test/"+dst 
                
                # rename() function will 
                # rename all the files 
                os.rename(src, dst) 
       
        dest = "test/"
        files = os.listdir('test')
        # print(files)
        for f in files:
                # create new folder for each student with the first 7 charater of student id
                os.makedirs(dest+f[:7],exist_ok=True)
                # move individual student's files to individual folders
                if (f.startswith(f[:7])):
                        shutil.move(dest+f, dest+f[:7])

        print("copied all submissions into individual folders!!")
        # for f in files:
        #         print(f)

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 