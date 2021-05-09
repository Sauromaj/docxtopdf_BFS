from docx2pdf import convert #converting library
import os
from pathlib import Path
from collections import deque
names = []
print("Hello welcome to the docxtopdf converter. Please specify the names of the files that you would like to make into pdfs without the .docx extension./n")
num_files = int(input("Enter the number of files to convert: "))
#get input from the user
for i in range(num_files):
    name =input("File %d:" %(i+1))
    names.append(name + '.docx')

cwdfull = os.getcwd()
os.system('mkdir Allpdfs')
home = str(Path.home())
frontier = deque()
frontier.append(home)
#BFS algorithm to search through the direcotry tree
while (frontier):
    current = frontier.popleft()
    if(os.path.isfile(current)):
        if (any(fname in current for fname in names)):
            command = 'cp' + ' ' + current + ' ' + cwdfull
            os.system(command)
            
    else:
        os.chdir(current)
        pathuptillnow = current
        
        for i in os.listdir():
            if(("Desktop" in (pathuptillnow +i)) or ("Documents" in (pathuptillnow + i)) or ("Downloads"in (pathuptillnow + i))):
                frontier.append(pathuptillnow + '/' + i)
            if(current!=home):
                 os.chdir('..')

#convert each of the files to pdfs if they exist in the cwd
os.chdir(cwdfull)  
for i in names:
    if os.path.isfile(i):
        convert(i)
    else:
        print("could not convert a file, check name")
os.system('mv'+ ' ' + '*.pdf' + ' ' +  'Allpdfs')




