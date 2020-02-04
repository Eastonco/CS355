-- CptS 355 - Spring 2020 Assignment 1
-- Connor Easton 11557902


-- length :: [a] -> integer
-- length [0,1,2,3] => 4

-- elem :: Eq a => a -> [a] -> Bool
-- elem 3 [0,1,2,3] => True
-- elem 't' "CptS" => True

-- maximum :: Ord a => [a] -> a
-- minimum :: Ord a => [a] -> a
-- sum :: Num a => [a] -> a
-- product :: Num a => [a] -> a
-- sum [0,1,2,3] => 6
-- product [1,2,3,4] => 24

module HW1
     where

-- 1a. exists

exists :: Eq t => t -> [t] -> Bool
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
listDiff src (del:dels) = let 
                              diffHelper [] del = []
                              diffHelper (src:srcs) del | del == src = srcs
                                                        | otherwise = src : diffHelper srcs del
                          in
                              if (null dels) == False then listDiff (diffHelper src del) dels 
                              else diffHelper src del


-- 3. firstN

firstN :: (Num t, Eq t) => [a] -> t -> [a]
firstN (j:js) k
     | k == 1 = js
     | otherwise = firstN js (k-1)


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


