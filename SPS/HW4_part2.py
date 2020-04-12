import re
import copy
from HW4_part1 import *

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
def interpretSPS(code): # code is a code array
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


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s))) 

#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

def psIf(): #<Bool> <code> psIf()
    code = opPop()
    isTrue = opPop()
    if isinstance(isTrue, bool) and isinstance(code, dict) and ('codearray' in code): # Checks for booleans and code block
        if(isTrue):
            interpretSPS(code)
    else:
        opPush(isTrue)
        opPush(code)
        print("Error: psIf() expects a code block and a boolean")

def psIfelse(): # <Bool> <code if true> <code if false> psIfelse()
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
    

def psRepeat(): #<count> <code array> psRepeat()
    code = opPop()
    count = opPop()
    if isinstance(count, int) and isinstance(code, dict) and ('codearray' in code): # Checks for int and code block
        for i in range(count):
            interpretSPS(code)
    else:
        opPush(count)
        opPush(code)
        print("Error: psRepeat() expects a code block and an int")

def forall(): #<array> <code array> forall() # one at a time
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



input1 = """
            /square {dup mul} def
            0 [2 3 add -4 3 -2 1]
            {square add} forall
            55 eq false and
        """

# print(tokenize(input1))
# print(parse(tokenize(input1)))
# print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))



