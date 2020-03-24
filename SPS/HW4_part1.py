# Connor Easton 11557902

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    return opstack.pop()
    
    # opPop should return the opped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    try:
        for num in value:
            opstack.append(num)
    except TypeError:
        opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    # dictPush pushes the dictionary ‘d’ to the dictstack. 
    # Note that, your interpreter will call dictPush only when Postscript 
    # “begin” operator is called. “begin” should pop the empty dictionary from 
    # the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    tmp = dictPop()
    tmp[name] = value
    dictPush(tmp)
    pass
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    tmplist = []
    for i in range(len(dictstack)):
        tmplist.insert(0,dictPop())

    for d in tmplist:
        dictPush(d)
    
    tmplist.reverse()


    searchName = '/' + name
    for d in tmplist:
        if d.get(searchName) is not None:
            return d.get(searchName)
    print("No value found")

    
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            #print("Error: add - one of the operands is not a numerical value") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: add expects 2 operands")
        pass

def sub():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1 - op2)
        else:
            #print("Error: sub - one of the operands is not a numerical value") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: sub expects 2 operands")
        pass

def mul():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op2 * op1)
        else:
            #print("Error: mul - one of the operands is not a numerical value") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: mul expects 2 operands")
        pass

def eq():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if(op1 is op2):
            opPush(True)
        else:
            opPush(False)
    else:
        #print("Error: eq expects 2 operands")
        pass

def lt():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1,int) and isinstance(op2,int)):
            if (op1 < op2):
                opPush(True)
            else:
                opPush(False)
        else:
            #print("Error:  - one of the operands is not a numerical value") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: gt expects 2 operands")
        pass


def gt():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1,int) and isinstance(op2,int)):
            if (op1 > op2):
                opPush(True)
            else:
                opPush(False)
        else:
            #print("Error:  - one of the operands is not a numerical value") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: gt expects 2 operands")
        pass

def psAnd():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1,bool) and isinstance(op2,bool)):
            if op1 == True and op2 == True:
                opPush(True)
            else:
                opPush(False)
        else:
            #print("Error: psAnd - variables are not Boolean") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: psNot expects 2 operands")
        pass

def psOr():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1,bool) and isinstance(op2,bool)):
            if op1 == True or op2 == True:
                opPush(True)
            else:
                opPush(False)
        else:
            #print("Error: psOr - variables are not Boolean") 
            opPush(op1)
            opPush(op2)
    else:
        #print("Error: psNot expects 2 operands")
        pass

def psNot():
    if len(opstack) > 0: 
        op1 = opPop()
        if (isinstance(op1,bool)):
                opPush(not op1)
        elif (isinstance(op1,int)):
            opPush(-op1)
    else:
        #print("Error: psNot expects 1 operand")
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
# Define the stack manipulation and #print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
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
