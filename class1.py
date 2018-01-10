from collections import Counter
#from json1 import data

class class1(object):
    """description of class"""
    def __init__(self):
        self.data = []

    i = 1234

    def f (othervalue):
        #print(self.value)
        print(othervalue)

hello = class1.f(othervalue = 'hello')
print(hello, class1.i)

c = Counter() 
c = Counter('sdkfjiwjeoifeifeiewfimwfomnoirewfgmnirewgreoigreg').most_common(3)
print(c)
#print(data)

def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print ("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test', 'brent')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key,value))
 
greet_me(name="yasoob", hellof ='brent')

def foo(bar=2, baz=5):
    print (bar, baz)

def proxy(x, *args, **kwargs): # reqire parameter x and accept any number of additional arguments
    print (x)
    foo(*args, **kwargs) # applies the "non-x" parameter to foo

proxy(23, 54, baz='foo2') # calls foo with bar=5 and baz=foo
proxy(6)# calls foo with its default arguments
proxy(7, bar='asdas') # calls foo with bar='asdas' and leave baz default argument


