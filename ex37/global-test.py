something = "this is global"

def hello():
    something = "cool"
    print something

hello()
print something

def whatever():
    print something

whatever()
