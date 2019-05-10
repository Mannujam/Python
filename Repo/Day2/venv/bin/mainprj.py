#import Way1 - type 1
import mymodule # just including module doesnt work. create variable 'PYTHONPATH' in env variable with value of 'lib' folder of virtual environment
#import Way1 - type 2
import mymodule as m
print (m.msg)
#import Way1 - type 3
from mymodule import msg,add        # list of all function to be imported or use * for all functions
print(msg)

#packaging
#import Way2 - type 1
import project.net.mymodule

import sys

#print(sys.path)
#if module path is not present
#sys.path.append ('C:\Chetan\Repo\Day2\venv\Lib')

#print(mymodule.msg)
#print(mymodule.add(20,21))

print(project.net.mymodule.msg)