debugging = True 
def debug(*s):
    if debugging: 
        print(*s)





sales = {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}

def sumSales(d):
    totalSales = {}
    for sales in d.values():
        for day, price in sales.items():
            #debug(day, '->', price)
            if day in totalSales:
                totalSales[day] = (price + totalSales.get(day))
            else:
                totalSales[day] = price
    return totalSales


weekSales = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},
{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50},'Ebay':{'Mon':100,'Sat':30}}, {'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40}, 'Shopify':{'Sat':35}}]
#list of two dicts

def sumSalesN(L):
    totalSales = {}
    count = 1
    for dict in L:
        totalSales[count]= (sumSales(dict))
        count += 1
    return sumSales(totalSales)


L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

def searchDicts(L,k):
    tmp = L
    tmp.reverse()
    for dict in tmp:
        debug(dict)
        if k in dict:
            return dict.get(k)
    return None

L2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}),
(1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]

def searchDicts2(L,k):
    return dictHelper(L,k,(len(L)-1))


def dictHelper(L,k,index):
    if k in L[index][1]:
        return L[index][1].get(k)
    elif L[index][0] == index:
        return None
    else:
        return dictHelper(L,k,L[index][0])

buses = {
"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
"Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"], "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
"Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
"Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
}

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
    return removeDupes(palindrome)


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
    count = 1
    list = []

    def __init__(self, l1, l2):
        while True:
            try:
                if self.count % 2 == 0:
                    self.count +=1
                    self.list.append(next(l2))
                else:
                    self.count +=1
                    self.list.append(next(l1))
            except StopIteration:
                self.count = 0
                break


    def __next__(self):
        try:
            self.count += 1
            return self.list[self.count-1]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self
    
    def __reset__(self):
        self.count = 0
        return "Iterator Reset"


        


#def typeHistogram (it,n):    