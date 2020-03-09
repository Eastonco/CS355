# Connor Easton - 11557902
# Created: March 7, 2020
# Last Updated: ^
# WSU CPTS 355, Assignment 3, Spring 2020

# Used for debugging... duh
debugging = True 
def debug(*s):
    if debugging: 
        print(*s)

# Accepts a dictionary of -> {'str1': {'str2':int}}
# Returns a single dictionary -> {'str2': ints}
# sums all entries from value index in input dict
def sumSales(d):
    totalSales = {}
    for sales in d.values():
        for day, price in sales.items():
            if day in totalSales:
                totalSales[day] = (price + totalSales.get(day))
            else:
                totalSales[day] = price
    return totalSales

# Same as sumSales except input is list of dictionaries -> [{'str1': {'str2':int}}]
def sumSalesN(L):
    totalSales = {}
    count = 1
    for dict in L:
        totalSales[count]= (sumSales(dict))
        count += 1
    return sumSales(totalSales)

# Accepts a list of Dictionaries(L) -> [{"str":val}] and a key(k) "str"
# Returns the correstponding value to the key if it exists, else: returns None
def searchDicts(L,k):
    tmpL = L[:]
    tmpL.reverse()
    for dict in tmpL:
        if k in dict:
            return dict.get(k)
    return None

# Accepts a list of tuples(L) of int and dict -> [(int,{"str":val})] and a key value(k) -> "str"
# Returns the corresponding value to the key if found, otherwise returns None
# Starting at end of the list, searches first dict for value
#   if not found uses the tuple int as an index to go to the corresponding
#   next dict, some dicts may not be searched
def searchDicts2(L,k):
    return dictHelper(L,k,(len(L)-1))

# Helper funciton to searchDicts2() - recursive
# Accepts the same as searchDicts2 except with an index to search
def dictHelper(L,k,index):
    if k in L[index][1]:
        return L[index][1].get(k)
    elif L[index][0] == index:
        return None
    else:
        return dictHelper(L,k,L[index][0])

# Accepts a dict of strings(buses) and list of stirngs -> {"str": ["str1"]}
#   and a target stop(stop) -> "str"
# Returns a list of str that match target
def busStops (buses,stop):
    buslist = []
    for route, stops in buses.items():
        if stop in stops:
            buslist.append(route)
    return buslist

# Accepts a string(S) -> 'str'
# Returns all possible palindromes in the string
def palindromes(S):
    palindrome = []
    index = 2
    while index <= len(S):
        palindrome.extend(palindromeIndex(S,index))
        index += 1
    return sorted(removeDupes(palindrome))

# Helper function to palindromes()
# Accepts a string(S) -> "str" and an index(n) -> int
# Iterates over a sub set between 0 and n until reaching the end of the string
# Returns all palindromes between the two indecies
def palindromeIndex(S,n):
    palindrome = []
    start = 0
    end = n
    while end <= len(S):
        if(palindromeHelper(S[start:end])):
            palindrome.append(S[start:end])
        start += 1
        end += 1
    return palindrome

# Helper function to palindromes()
# accepts a List and removes all duplicates
# Returns a list
def removeDupes(L):
    list = []
    for val in L:
        if val not in list:
            list.append(val)
    return list

# Helper function to palindromes()
# Accepts a string(s)
# Returns a boolean
# Tests to see if the string == reverse(string)
def palindromeHelper(s):
    tmp = s [::-1]
    if(tmp == s):
        return True
    return False

class interlaceIter:

    # Accepts two iterator values for constructor
    def __init__(self, l1, l2):
            self.itr1 = l1
            self.itr2 = l2
            self.count = 0
            self.isEnd = False

    # Returns the next value, alternating between the two iterators
    def __next__(self):
        if self.isEnd == True:
            raise StopIteration 
        try:
            if self.count % 2 == 0:
                self.count += 1
                self.tmpval = next(self.itr2)
                return next(self.itr1)
            else:
                self.count += 1
                return self.tmpval
        except StopIteration:
            self.isEnd= True
            raise StopIteration

    # Enables the object to be iterated though in a for loop
    def __iter__(self):
        return self

# Accepts an iterator(it) and an int(n)
# Returns a list of tupels -> [(str, int)] for all entires in d
# iterates through the iterator n times. Checks the return type of
#   the iterator and places it into a corrisponding dict(sequencedict)
#   entry. Essentialy counting the number of occouraces of a given type
def typeHistogram (it,n):    
    count = 0
    sequencedict = {}
    while count < n:
        try:
            val = it.__next__()
            if type(val) is str:
                if sequencedict.get('str'):
                    sequencedict['str'] = 1 + sequencedict.get('str')
                    count += 1
                else:
                    sequencedict['str'] = 1
                    count += 1
            elif type(val) is int:
                if sequencedict.get('int'):
                    sequencedict['int'] = 1 + sequencedict.get('int')
                    count += 1
                else:
                    sequencedict['int'] = 1
                    count += 1
            elif type(val) is tuple:
                if sequencedict.get('tuple'):
                    sequencedict['tuple'] = 1 + sequencedict.get('tuple')
                    count += 1
                else:
                    sequencedict['tuple'] = 1
                    count += 1
            elif type(val) is float:
                if sequencedict.get('float'):
                    sequencedict['float'] = 1 + sequencedict.get('float')
                    count += 1
                else:
                    sequencedict['float'] = 1
                    count += 1
            
        except StopIteration:
            break
    return dictToList(sequencedict)

# Helper function to typeHistogram()
# Accepts a dictionary(d) -> {'str': int}
# Returns a list of tupels -> [(str, int)] for all entires in d
def dictToList(d):
    returnList = []
    for type, count in d.items():
        returnList.append((type, count))
    return returnList
