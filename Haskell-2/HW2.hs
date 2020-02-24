-- CptS 355 - Spring 2020 Assignment 2
-- Connor Easton 11557902
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW2
     where


{- intersect & intersectTail & intersectAll - 22%-}
--intersect 
intersect :: Eq a => [a] -> [a] -> [a]
intersect [] l2 = []
intersect l1 l2 = let
                    intersectHelper [] l2 = []
                    intersectHelper (x:xs) l2
                         | elem x l2 = x : intersect xs l2
                         | otherwise = intersect xs l2
                    removeDupes [] = []
                    removeDupes (x:xs)
                         | elem x xs = removeDupes xs
                         | otherwise = x : removeDupes xs
                 in
                    removeDupes (intersectHelper l1 l2)

--intersectTail
intersectTail :: Eq a => [a] -> [a] -> [a]
intersectTail l1 l2 = let 
                         intersectTailHelper [] l2 acc = reverse acc
                         intersectTailHelper (x:xs) l2 acc
                              | elem x l2 =  intersectTailHelper xs l2 (x:acc)
                              | otherwise = intersectTailHelper xs l2 acc
                         removeDupes [] acc = acc
                         removeDupes (x:xs) acc
                              | elem x xs = removeDupes xs acc
                              | otherwise = removeDupes xs (x:acc)
                      in
                         reverse (removeDupes (intersectTailHelper l1 l2 []) [])


--intersectAll
intersectAll:: Ord a => [[a]] -> [a]
intersectAll (x:xs) = (foldr (intersectTail) x xs)



{-2 - partition - 10%-}
partition :: (a -> Bool) -> [a] -> ([a], [a])
partition isTrue list = (filter isTrue list, filter (not.isTrue) list)


{- 3 - sumL, sumMaybe, and sumEither - 27% -}

--sumL
sumL :: (Num b) => [[b]] -> b
sumL [] = 0
sumL l1 = let
           sumHelper [] = 0
           sumHelper l1 = (foldr (+) 0 l1)
          in
           sumHelper (map sumHelper l1)


-- sumMaybe 
sumMaybe :: (Num a) => [[Maybe a]] -> Maybe a
sumMaybe [] = Nothing
sumMaybe l1 = let
               sumMaybeBase l1 = (foldr (sumMaybeHelper) Nothing l1)

               sumMaybeHelper Nothing Nothing = Nothing
               sumMaybeHelper Nothing (Just x) = (Just x)
               sumMaybeHelper (Just x) Nothing = (Just x)
               sumMaybeHelper (Just x) (Just y) = (Just (x+y))
              in
               sumMaybeBase(map sumMaybeBase l1)



-- sumEither
data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)

sumEither :: [[IEither]] -> IEither
sumEither l1 = let
                    getInt x = read x::Int

                    sumEitherBase l1 = (foldr (sumEitherHelper) (IInt 0) l1)

                    sumEitherHelper (IString string1) (IString string2) = IInt ((getInt string1) + (getInt string2))
                    sumEitherHelper (IString string) (IInt num) = IInt ((getInt string) + num)
                    sumEitherHelper (IInt num) (IString string) = IInt (num + (getInt string))
                    sumEitherHelper (IInt num1) (IInt num2) = IInt (num1 + num2)
               in 
                    sumEitherBase(map sumEitherBase l1)


{-4 - depthScan, depthSearch, addTrees - 37%-}

data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)
 
--depthScan
depthScan :: Tree a -> [a]
depthScan (LEAF a) = [a]
depthScan (NODE a (left) (right)) = (depthScan left) ++ (depthScan right) ++ [a]

--depthSearch
depthSearch :: (Ord p, Num p, Eq a) => Tree a -> a -> p
depthSearch tree target = let
                              depthSearchHelper (LEAF a) target level 
                                   | (target == a) = level
                                   | otherwise = -1
                              depthSearchHelper (NODE a (left) (right)) target level
                                   | ((depthSearchHelper left target (level + 1)) /= -1) = depthSearchHelper left target (level + 1)
                                   | otherwise = (depthSearchHelper right target (level + 1))
                           in
                              depthSearchHelper tree target 1


                              
--addTrees
addTrees :: Num a => Tree a -> Tree a -> Tree a
--addTrees left right = LEAF 3
addTrees (LEAF a) (LEAF b) = LEAF (a + b)
addTrees (NODE a lefta righta) (NODE b leftb rightb) = NODE (a+b) (addTrees (lefta) (leftb)) (addTrees (righta) (rightb))
addTrees (NODE a lefta righta) (LEAF b) = NODE (a+b) (copyTree lefta) (copyTree righta)
addTrees (LEAF a) (NODE b leftb rightb) = NODE (a+b) (copyTree leftb) (copyTree rightb)


copyTree (LEAF x) = LEAF x
copyTree (NODE a t1 t2) = NODE a (copyTree t1) (copyTree t2)


{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}

tree1 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (NODE 6 (LEAF 7) (LEAF 8))) (NODE 9 (NODE 10 (LEAF 11) (LEAF 12)) (NODE 13 (LEAF 14) (LEAF 15)))
tree2 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 4)) (NODE 9 (LEAF 3) (NODE 13 (LEAF 14) (LEAF 15)))