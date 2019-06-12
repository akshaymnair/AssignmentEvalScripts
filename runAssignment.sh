#!/bin/bash
# author: Akshay - amurale1@asu.edu TA - CSE100
# usage: Copy this script file inside the folder where individual students folders are created
for folder in */; do 
    [ -d $folder ] && cd "$folder" && echo "Entering into $folder " 
    # remove student details and rename files
    mv *.cpp lab10.cpp
	
    for file in *.*; do
        # echo "$file"    
        # save runtime outputs
        # exec &> logfile.txt
        exec 3>&1 4>&2 1>errorLog.log 2>&1
        # compile the files
        g++ -o prog *.cpp
        # test the program with all the given testcases
        for ((i=1;i<=4;i++)); do
            # save outputs for individual testcases
            ./prog < ../../input$i* > output$i.txt
        done
        exec 1>&3 2>&4
    done  
    cd ../
    echo >&2 "Done with testing for student- $folder !! "
done 