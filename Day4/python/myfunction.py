#! /bin/python

from secondfile import MyClass;

def func():
    print("Hello from Python!!!")
    print(__name__)

if __name__ == "__main__":
    func()
    obj = MyClass()
    obj.secondFunction()
    
