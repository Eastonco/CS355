-- CptS 355 - Spring 2020 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW2
     where


{- intersect & intersectTail & intersectAll - 22%-}
--intersect



--intersectTail



--intersectAll



{-2 - partition - 10%-}



{- 3 - sumL, sumMaybe, and sumEither - 27% -}

--sumL



-- sumMaybe 



-- sumEither

data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)


{-4 - depthScan, depthSearch, addTrees - 37%-}

data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)
 
--depthScan



--depthSearch



--addTrees


{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}