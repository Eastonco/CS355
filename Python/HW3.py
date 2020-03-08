debugging = True 
def debug(*s):
    if debugging: 
        print(*s)





#sales = {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}

def sumSales(d):
    totalSales = {}
    for sales in d.values():
        for day, price in sales.items():
            if day in totalSales:
                totalSales[day] = (price + totalSales.get(day))
            else:
                totalSales[day] = price
    return totalSales


#weekSales = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},
#{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50},'Ebay':{'Mon':100,'Sat':30}}, {'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40}, 'Shopify':{'Sat':35}}]
#list of two dicts

def sumSalesN(L):
    totalSales = {}
    count = 1
    for dict in L:
        totalSales[count]= (sumSales(dict))
        count += 1
    return sumSales(totalSales)


#L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

def searchDicts(L,k):
    L.reverse()
    for dict in L:
        if k in dict:
            return dict.get(k)
    return None

#L2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}),(1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]

def searchDicts2(L,k):
    return dictHelper(L,k,(len(L)-1))


def dictHelper(L,k,index):
    if k in L[index][1]:
        return L[index][1].get(k)
    elif L[index][0] == index:
        return None
    else:
        return dictHelper(L,k,L[index][0])
"""
buses = {
"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
"Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"], "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
"Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
"Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
}"""

def busStops (buses,stop):
    buslist = []
    for route, stops in buses.items():
        if stop in stops:
            buslist.append(route)
    return buslist

def palindromes(S):
    palindrome = []
    index = 2
    while index <= len(S):
        palindrome.extend(palindromeIndex(S,index))
        index += 1
    return sorted(removeDupes(palindrome))


def palindromeIndex(S,l):
    palindrome = []
    start = 0
    end = l
    while end <= len(S):
        if(palindromeHelper(S[start:end])):
            palindrome.append(S[start:end])
        start += 1
        end += 1
    return palindrome

def removeDupes(L):
    list = []
    for val in L:
        if val not in list:
            list.append(val)
    return list

def palindromeHelper(s):
    tmp = s [::-1]
    if(tmp == s):
        return True
    return False



class interlaceIter:
    def __init__(self, l1, l2):
            self.itr1 = l1
            self.itr2 = l2
            self.count = 0
            self.isEnd = False

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

    def __iter__(self):
        return self


        
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

def dictToList(d):
    returnList = []
    for type, count in d.items():
        returnList.append((type, count))
    return returnList

