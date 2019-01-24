-- Comments
{-
	Multiline	
-}

import Data.List
import System.IO


-- Int -2^63 2^63

maxInt = maxBound :: Int
minInt = minBound :: Int


-- Math Function
sumOfNums = sum [1..1000]

modEx = mod 5 4
negNumEx = 5 + (-4)


-- List

primeNumbers = [3,5,7,11]
morePrime = primeNumbers ++ [13,17]
morePrime2 = 2 : primeNumbers
favNums = 2 : 7 : 21 : 66 : []