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
    if (value == '['):
        opstack.append('-mark-')
    elif (value == ']'):
        opstack.append(cleartomark())
    elif (isinstance(value,str)) and (value[0] != '/'):
        if(value != "-mark-"):
            opstack.append(lookup(value))
        else:
            opstack.append("-mark-")
    else:
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
    try:
        mydict = dictPop()
        mydict[name] = value
        dictPush(mydict)
    except IndexError:
        dictPush({})
        mydict = dictPop()
        mydict[name] = value
        dictPush(mydict)
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    dictstack.reverse()
    searchName = '/' + name
    for d in dictstack:
        if d.get(searchName) is not None:
            val = d.get(searchName)
            break
    dictstack.reverse()
    try:
        return val
    except:
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
        print("Error: add expects 2 operands")

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
        print("Error: sub expects 2 operands")
        

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
        print("Error: mul expects 2 operands")
        

def eq():
    if len(opstack) > 1: 
        op2 = opPop()
        op1 = opPop()
        if(op1 is op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

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
        print("Error: gt expects 2 operands")


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
        print("Error: gt expects 2 operands")

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
        print("Error: psNot expects 2 operands")

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
        print("Error: psNot expects 2 operands")

def psNot():
    if len(opstack) > 0: 
        op1 = opPop()
        if (isinstance(op1,bool)):
                opPush(not op1)
        elif (isinstance(op1,int)):
            opPush(-op1)
    else:
        print("Error: psNot expects 1 operand")


#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length(): # pops an array from stack, returns it's length
    val = opPop()
    if type(val) is list:
        opPush(len(val))
    else:
        print("Value not a list")

def get(): # <array> <index> get(), get value at index and push to stack
    index = opPop()
    arr = opPop()
    if (type(arr) is list) and (type(index) is int):
        try:
            opPush(arr[index])
        except IndexError:
            print("Index out of range in array")
    else:
        print("types are not list and int")

def getinterval(): # <array> <index> <count> getinterval()
    count = opPop()
    index = opPop()
    arr = opPop()

    if (type(arr) is list) and (type(index) is int):
        l = []
        try:
            for i in range(count):
               l.append(arr[index + i])
        except IndexError:
            print("index out of range")
        print(l)
        opPush(l)
    else:
        print("types are not list and int")


def put(): # <array> <index> <value> put(), repalces a value in an array
    val = opPop()
    index = opPop()
    arr = opPop()
    if(type(arr) is list) and (type(index) is int):
        try:
            arr[index] = val
        except IndexError:
            print("Index out of range in array")
    else:
        print("types are not list and int")

def putinterval():
    arr2 = opPop()
    index = opPop()
    arr1 = opPop()
    if(type(arr1) is list) and (type(index) is int) and (type(arr2) is list):
        try:
            arr1[index:(len(arr2) + index)] = arr2[:]
        except IndexError:
            print("Index out of range in array")
    else:
        print("types are not list and int")

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and #print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    val = opPop()
    opPush(val)
    opPush(val)

def copy():
    count = opPop()
    opStackCopy = opstack[:]
    if count < len(opStackCopy):
        while count > 0:
            opPush(opStackCopy[-count])
            count -= 1
    else:
        opPush(count)
        print("Error: copy count is larger than list")

def count():
    opPush(len(opstack))


def pop(): 
    return opPop()

def clear():
    opstack.clear()

def exch():
    tmp = opstack[-1]
    opstack[-1] = opstack[-2]
    opstack[-2] = tmp

def mark():
    opPush("-mark-")

def cleartomark():
    if "-mark-" in opstack:
        l = []
        val = None
        while val != "-mark-":
            l.append(opPop())
            val = l[-1]
        return l
    else:
        print("No -mark- ins stack")

def counttomark():
    if "-mark-" in opstack:
        count = 0
        opstack.reverse()
        for val in opstack:
            if val == "-mark-":
                break
            else:
                count += 1
        opstack.reverse()
        opPush(count)
    else:
        print("Error: counttomark() - no mark in stack")


def stack():
    opstack.reverse()
    for val in opstack:
        print(val)
    opstack.reverse()

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    opPop()
    opPush({})

def begin():
    newdict = opPop()
    if type(newdict) is dict:
        dictPush(newdict)
    else:
        opPush(newdict)
        print("Error: begin - popped val is not dict")

def end():
    try:
        dictPop()
    except IndexError:
        print("ERROR: end() - no dicts to pop")

def psDef():
    val1 = opPop()
    val2 = opPop()
    if isinstance(val1, str):
        define(val1, val2)
    elif isinstance(val2, str):
        define(val2, val1)
    else:
        opPush(val2)
        opPush(val1)
        print("Error: psDef() - No variable and value pair")