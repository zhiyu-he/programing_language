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
morePrimes = primeNumbers ++ [13,17]
morePrimes2 = 2 : primeNumbers
favNums = 2 : 7 : 21 : 66 : []
lenPrime = length morePrimes2
revPrime = reverse morePrimes2
isListEmpty = null morePrimes2

secondPrime = morePrimes2 !! 1
firstPrime = head morePrimes2
lastPrime = last morePrimes2
primeInit = init morePrimes2
first3Primes = take 3 morePrimes2
removedPrimes = drop 3 morePrimes2

is7InList = 7 `elem` morePrimes2

maxPrime = maximum morePrimes2
minPrime = minimum morePrimes2

many2s = take 10 (repeat 2)

cycleList = take 10 (cycle [1,2,3,4,5])

listTimes2 = [x * 2 | x <- [1..10]]

listTimes3 = [x * 3 | x <- [1..10], x * 3 <= 50]

divisBy9N13 = [x | x <-[1..500], x `mod` 13 == 0, x `mod` 9 == 0]

sumOfLists = zipWith (+) [1,2,3,4,5] [6,7,8,9,10]

listBiggerThen5 = filter (>5) morePrimes
