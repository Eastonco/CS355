# Connor Easton - 11557902
# Created: March 7, 2020
# Last Updated: ^
# WSU CPTS 355, Assignment 3, Spring 2020

import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog = {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        self.assertDictEqual(sumSales(salesLog),summedLog)
        salesLog1 = {'Amazon':{'Mon':42,'Wed':110,'Sat':21},'Etsy':{'Mon':75,'Tue':42,'Wed':55,'Fri':33},'Ebay':{'Tue':37,'Wed':1562,'Thu':31},'Shopify':{'Tue':10,'Thu':40,'Sat':80}}
        summedLog1 = {'Mon': 117, 'Wed': 1727, 'Sat': 101, 'Tue': 89, 'Fri': 33, 'Thu': 71}
        self.assertDictEqual(sumSales(salesLog1),summedLog1)
        salesLog2 = {}
        summedLog2 = {}
        self.assertDictEqual(sumSales(salesLog2),summedLog2)


    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)
        salesLog1 = [{'ebay':{'Mon':79}},{'craigslist':{'Tue':6}}]
        summedLog1 = {'Mon': 79, 'Tue': 6}
        self.assertDictEqual(sumSalesN(salesLog1),summedLog1)
        self.assertDictEqual(sumSalesN([{}]), {})

    def test_searchDicts(self):
        #searchDicts inputs
        dictList3 = [{"cat":1,"dog":True,"Butch":"found"},{"Butch":2},{"cat":False}]
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        #self.assertEqual(searchDicts(dictList,"y"),False) #this is wrong, it should be True, Searching from the END of a list
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)
        self.assertEqual(searchDicts(dictList3,"cat"),False)
        self.assertEqual(searchDicts(dictList3,"Frank Ocean"),None)

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        dictList4 = [(0,{"he":0,"she":True,"y":"yes"}), (1,{"findme":True}), (2,{"infinite":False})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)

        self.assertEqual(searchDicts2(dictList4,"findme"),None)
        self.assertEqual(searchDicts2(dictList4,"infinite"),False)

    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])

        self.assertEqual(busStops(routes,"Grand"), ['Blue'])
        self.assertEqual(busStops(routes,"Orchard"), ['Lentil', 'Wheat'])

    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes ('myracecars')  ,['aceca', 'cec', 'racecar'])
        self.assertEqual(palindromes('arethereanypalindromesinhere?'), ['ere'])
        self.assertEqual(palindromes('nope'), [])

    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])

        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)


    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])




if __name__ == '__main__':
    unittest.main()