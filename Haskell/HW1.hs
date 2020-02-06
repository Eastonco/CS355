-- CptS 355 - Spring 2020 Assignment 1
-- Connor Easton 11557902
-- worked with Zach Barnett


module HW1
     where

-- 1a. exists

exists :: Eq t => t -> [t] -> Bool
exists a [] = False
exists a (b:bs)
     | length bs == 0 && a == b = True
     | length bs == 0 = False
     | a == b = True
     | otherwise = exists a bs

-- 1b. type for exists
--     The type needs the Eq class to define equality
--     and inequaltiy to compare the two objects


-- 1.c countInList

countInList :: (Num p, Eq t) => t -> [t] -> p
countInList p (t:ts) 
     | (length ts == 0 && p==t) = 1
     | length ts == 0 = 0
     | p == t = 1 +(countInList p ts)
     | otherwise = countInList p ts



-- 2. listDiff

listDiff :: Eq a => [a] -> [a] -> [a]
listDiff src [] = src
listDiff src (del:dels) = let 
                              diffHelper [] del = []
                              diffHelper (src:srcs) del | del == src = srcs
                                                        | otherwise = src : diffHelper srcs del
                          in
                              if (null dels) == False then listDiff (diffHelper src del) dels 
                              else diffHelper src del


-- 3. firstN

firstN :: (Num t, Eq t) => [a] -> t -> [a]
firstN [] k = []
firstN (j:js) k
     |k == 0 = []
     |otherwise = j : firstN js(k-1)


-- 4. busFinder

busFinder :: Eq t => t -> [(a, [t])] -> [a]
busFinder location [] = []
busFinder location (x:xs) = if (exists location (snd x))
                              then (fst x) : busFinder location xs
                              else busFinder location xs



-- 5. cumulativeSums

cumulativeSums :: (Num a) => [a] -> [a]
cumulativeSums [] = [0]
cumulativeSums (x:xs) = let
                         sumHelper [] sum = []
                         sumHelper (x:xs) sum = (x+sum) : (sumHelper xs (sum + x))
                        in
                         x : sumHelper xs (x)


-- 6. groupNleft

groupNleft :: ( Num t, Eq t, Eq a) => t -> [a] -> [[a]]
groupNleft 0 list = [list]
groupNleft count [] = []
groupNleft count list = let
                         bagMe :: (Num t, Eq t) => t -> [a] -> [a]
                         bagMe count [] = []
                         bagMe count (x:xs) | count == 0 = []
                                            | otherwise = x : (bagMe (count-1) xs)
                        in
                         bagMe count list : if ( null (listDiff list (firstN list count)) == True) then []
                                             else (groupNleft count (listDiff list (firstN list count))) 




