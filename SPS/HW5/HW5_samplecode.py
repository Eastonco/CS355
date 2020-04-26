# Connor Easton 11557902
import re
import copy
# Part 1 code -----------------------------------------------------------------------------------
opstack = []  #assuming top of the stack is the end of the list

def opPop():
    return opstack.pop()

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


dictstack = []  #assuming top of the stack is the end of the list

def dictPop():
    return dictstack.pop()

def dictPush(d): # TODO:Add scope
    dictstack.append(d)

def define(name, value): # TODO: Add scope
    try:
        mydict = dictPop()
        mydict[name] = value
        dictPush(mydict)
    except IndexError:
        dictPush({})
        mydict = dictPop()
        mydict[name] = value
        dictPush(mydict)


def lookup(name): # TODO: add scope 
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

def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            print("Error: add - one of the operands is not a numerical value") 
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
            print("Error: sub - one of the operands is not a numerical value") 
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
            print("Error: mul - one of the operands is not a numerical value") 
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
            print("Error:  - one of the operands is not a numerical value") 
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
            print("Error:  - one of the operands is not a numerical value") 
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
            print("Error: psAnd - variables are not Boolean") 
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
            print("Error: psOr - variables are not Boolean") 
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


def length(): # pops an array from stack, returns it's length
    val = opPop()
    if type(val) is list:
        opPush(len(val))
    else:
        opPush(val)
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
        opPush(arr)
        opPush(index)
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
        opPush(l)
    else:
        opPush(arr)
        opPush(index)
        opPush(count)
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
        opPush(arr)
        opPush(index)
        opPush(val)
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
        opPush(arr1)
        opPush(index)
        opPush(arr2)
        print("types are not list and int")


def dup():
    val = opPop()
    opPush(val)
    opPush(val)

def copy():
    count = opPop()
    opStackCopy = opstack[:]
    if count <= len(opStackCopy):
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


def stack(): # TODO: add scope
    if len(opstack) > 0:
        opstack.reverse()
        for val in opstack:
            print(val)
        opstack.reverse()

# Dict operators
def psDict():
    if len(opstack) > 0:
        val = opPop()
        if(isinstance(val, int)):
            opPush({})
        else:
            opPush(val)

def begin():
    if len(opstack) > 0:
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
    if len(opstack) > 1:
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

# Part 2 code -----------------------------------------------------------------------------------------
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    


# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}': # End of code block
            return {'codearray':res}
        elif c=='{': # Begining of new code Block
            res.append(groupMatch(it))
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
        elif c == 'true': # Boolean conversion 
            res.append(True)
        elif c == 'false':
            res.append(False)
        elif c[0] == '[':
            res.append(listMatch(c))
        else:
            try:
                res.append(int(c))
            except:
                res.append(c)
    return False

def listMatch(L):
    l = []
    item = ''
    for i in range(len(L)):
        if i == 0: # skipping the starting '['
            continue
        elif L[i] == ']': # End of list
            if item == 'false': # Double check to clear cache in 'item'
                l.append(False)
            elif item == 'true':
                l.append(True)
            else:
                try:
                    l.append(int(item))
                except:
                    l.append(item)
            return l
        elif L[i] == '[': # Start of listception 
            l.append(listMatch(i)) # this won't work
        elif L[i] == ' ': # new variable, clear cache in 'item
            if item == 'true' :
                l.append(True)
                item = ''
            elif item == 'false':
                l.append(False)
                item = ''
            else:
                try:
                    l.append(int(item)) # tests for int
                    item = ''
                except:
                    l.append(item)
                    item = ''
        else:
            item += L[i]
            
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c == 'true': # Boolean Conversion 
            res.append(True)
        elif c == 'false':
            res.append(False)
        elif c=='{': 
            res.append(groupMatch(it))
        elif c[0] == '[':
            res.append(listMatch(c))
        else:
            try:
                res.append(int(c)) # tests for integer
            except:
                res.append(c)
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
"""
def interpretSPS(code): # code is a code array # TODO: add scope
    commandlist = code.get('codearray')
    for command in commandlist:
        if isinstance(command, dict) or isinstance(command, int) or isinstance(command, bool): # Test for Bool, Int, or dict to be pushed directly to stack
            opPush(command)
        elif isinstance(command, list):  # Evaluates and pushes list
            opPush(evaluateList(command)) 
        elif (isinstance(command, str)): 
            if(command[0] == '/'): # '/' is a variable name, push to stack
                opPush(command)
            elif command in commanddict: # checks to see if the string is a command
                commanddict[command]()
            else:
                val = lookup(command) # variable is not a command or unassinged variable, check for definition
                if isinstance(val, dict): # could be code block, Intepret 
                    interpretSPS(val)
                elif val is not None: # Variable is something, push to stack
                    opPush(val)
                else:
                    print("ERROR: Unhandeled command") # Variable matches no definitions 
        else: 
            print("ERROR: Unhandeled command")


def interpreter(s): # s is a string # TODO: add scope
    interpretSPS(parse(tokenize(s))) 
    """

#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

def psIf(): #<Bool> <code> psIf() # TODO: add scope
    code = opPop()
    isTrue = opPop()
    if isinstance(isTrue, bool) and isinstance(code, dict) and ('codearray' in code): # Checks for booleans and code block
        if(isTrue):
            interpretSPS(code)
    else:
        opPush(isTrue)
        opPush(code)
        print("Error: psIf() expects a code block and a boolean")

def psIfelse(): # <Bool> <code if true> <code if false> psIfelse() # TODO: add scope
    falseCode = opPop()
    trueCode = opPop()
    isTrue = opPop()
    if isinstance(isTrue, bool) and isinstance(trueCode, dict) and ('codearray' in trueCode) and isinstance(falseCode, dict) and ('codearray' in falseCode):
        if(isTrue):
            interpretSPS(trueCode)
        else:
            interpretSPS(falseCode)
    else:
        opPush(isTrue)
        opPush(trueCode)
        opPush(falseCode)
        print("Error: psIfelse() expects two code blocks and a boolean")
    

def psRepeat(): #<count> <code array> psRepeat() # TODO: add scope
    code = opPop()
    count = opPop()
    if isinstance(count, int) and isinstance(code, dict) and ('codearray' in code): # Checks for int and code block
        for i in range(count):
            interpretSPS(code)
    else:
        opPush(count)
        opPush(code)
        print("Error: psRepeat() expects a code block and an int")

def forall(): #<array> <code array> forall() # one at a time # TODO: add scope
    if len(opstack) > 1:
        codeArr = opPop()
        arr = opPop()
        for val in arr:
            opPush(val)
            interpretSPS(codeArr)

def evaluateList(list):
    global opstack # make sure to refrence global opstack
    opStackCopy = opstack[:] # Makes a copy of opstack
    opstack[:] = [] # Clears opstack
    interpretSPS({'codearray':list}) # interprets code blcok 
    eList = opstack[:] # Stores the interpreted code block to a variable
    opstack[:] = opStackCopy[:] # Restore's opstack's previous state
    return eList

commanddict = { # List of all recognizeable string commands
    'add' : add,
    'sub' : sub,
    'mul' : mul,
    'lt' : lt,
    'gt' : gt,
    'and' : psAnd,
    'or' : psOr,
    'eq' : eq,
    'not' : psNot,
    'length' : length,

    'get' : get,
    'getinterval' : getinterval,
    'put' : put,
    'putinterval' : putinterval,

    'dup' : dup,
    'copy' : copy,
    'count' : count,
    'pop' : pop,
    'clear' : clear,
    'exch' : exch,
    'mark' : mark,
    'cleartomark' : cleartomark,
    'counttomark' : counttomark,
    'stack' : stack,

    'dict' : psDict,
    'begin' : begin,
    'end' : end,
    'def' : psDef,

    'forall' : forall,
    'if' : psIf,
    'ifelse' : psIfelse,
    'repeat' : psRepeat
    }


# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    pass

#the main recursive interpreter function
def interpretSPS(tokenList,scope):
    pass

#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():
    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    testinput2 = """
    /x 4 def
    [1 1 1] dup 1 [2 3] putinterval /arr exch def
    /g { x stack } def
    /f { 0 arr {7 mul add} forall /x exch def g } def
    f
    """
    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """
    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput5 = """
    /x 10 def
    /n 5  def
    /A { 0  n {x add} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    testinput7 = """
    /x [1 2 3 4] def
    /A { x length } def
    /C { /x [10 20 30 40 50 60] def A stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def C } def
    B
    """
    testinput8 = """
    [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
    /a 10 def  
    /A { x length } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
    B
    """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')