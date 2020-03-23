# WRITE YOUR NAME and YOUR COLLABORATORS HERE

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    pass
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    pass

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    pass
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    pass
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    pass
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    pass
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    pass

def sub():
    pass

def mul():
    pass

def eq():
    pass

def lt():
    pass

def gt():
    pass

def psAnd():
    pass

def psOr():
    pass

def psNot():
    pass

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    pass

def get():
    pass

def getinterval():
    pass

def put():
    pass

def putinterval():
    pass

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    pass

def copy():
    pass

def count():
    pass

def pop():
    pass

def clear():
    pass

def exch():
    pass

def mark():
    pass

def cleartomark():
    pass

def counttomark():
    pass

def stack():
    pass

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    pass

def begin():
    pass

def end():
    pass

def psDef():
    pass
