'''input: File name(s) specified by user without .docx extension
   desc: This module converts file(s) specified by the user in .docx
   format to .pdf format into a folder Allpdfs in the cwd and also 
   copies the .docx file to the cwd as well'''
import os
from pathlib import Path
from collections import deque
from docx2pdf import convert #converting library

names = [] #list for the .docx files
print("Hello welcome to the docxtopdf converter.")
print("Please specify the names of the files", end=' ')
print("that you would like to make into pdfs without the .docx extension.", end='/n')
num_files = int(input("Enter the number of files to convert: "))

#get input from the user
for i in range(num_files):
    name =input("File %d:" %(i+1))
    names.append(name + '.docx')

cwdfull = os.getcwd()
os.system('mkdir Allpdfs')
home = str(Path.home())
#Queue to store the absolute paths as the BFS algorithm navigates the file system
frontier = deque() 
frontier.append(home)
#BFS algorithm to search through the direcotry tree
while frontier:
    current = frontier.popleft()
    if os.path.isfile(current):
        if any(fname in current for fname in names):
            command = 'cp' + ' ' + current + ' ' + cwdfull
            os.system(command)         
    else:
        os.chdir(current)
        pathuptillnow = current       
        for i in os.listdir():
            #only look in Desktop, Documents and Downloads for files
            if(("Desktop" in pathuptillnow+i) or ("Documents" in pathuptillnow + i) or ("Downloads"in pathuptillnow + i)):
                frontier.append(pathuptillnow + '/' + i)
            if current!=home:
                os.chdir('..')

#convert each of the files to pdfs if they exist in the cwd
os.chdir(cwdfull)  
for i in names:
    if os.path.isfile(i):
        convert(i)
    else:
        print("could not convert a file, check name")
os.system('mv'+ ' ' + '*.pdf' + ' ' +  'Allpdfs')
