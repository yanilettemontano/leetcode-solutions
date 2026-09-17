#Variables are dynamically typed in Python. You do not
#  need to declare the type of a variable when you 
# create one. The interpreter infers the type 
# of the variable based on the value assigned to it.

n = 0
print('n = ', n)

n = "abc"
print('n = ', n)

#Multiple assignments
n, m = 0, "abc"

#Increment
n = n + 1
n += 1

#None is null (absence of a value)
n = None
print('n = ', n)

#If statements don't need parentheses
#or curly braces.
n = 1 
if n > 2:
    n -= 1 #use indentation to denote blocks of code
elif n == 2:
    n *= 2
else:
    n += 2

#Parentheses needed for multi-line conditions.
# and = &&
# or = ||
n, m = 1, 2
if ((n > 2 and 
     n != m) or n == m):
    n += 1

#while loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

#looping from i = 0 to i = 4
for i in range(5):
    print(i)

#looping from i = 2 to i = 5
for i in range(2, 6): #starting from 2 and ending at 5 (not including 6)
    print(i)

#looping from i = 5 to i = 2
for i in range(5, 1, -1): #starting from 5 and ending at 2 (not including 1)
    print(i)

#Division is decimal by default
print(5/2) #prints 2.5

#double slash rounds down
print(5//2) #prints 2 (integer division)

#CAREFUL: most langages round towards 0 by
#default so negative numbers will round down
print(-3//2) #prints -2 (rounds down to -2)

#A workaround for rounding towards 0 is
#to use decimal division and then convert to int
print(int(-3/2)) #prints -1 (rounds towards 0)

#Modulus is similar to other languages
print(10%3) #prints 1

#Except for negative numbers, the modulus is always positive
print(-10%3) #prints 2

#to be consistent with other languages,
#you can use:
import math
print(math.fmod(-10, 3)) #prints -1 (rounds towards 0)

#more math helpers
print(math.floor(3/2)) #prints 1 (rounds down)
print(math.ceil(3/2)) #prints 2 (rounds up)
print(math.sqrt(2)) #prints 1.4142135623730951 (square root)
print(math.pow(2, 3)) #prints 8.0 (2 raised to the power of 3)

#Max / Min Int
float('inf') #positive infinity
float('-inf') #negative infinity

#Python numbers are infinite so they never overflow
print(math.pow(2, 1000)) #prints 1.0715086071862673e+301 (2 raised to the power of 1000)

#Arrays (called lists in Python)
arr = [1, 2, 3]
print(arr)

#can be used as a stack (dynamic arrays by default)
arr.append(4) #push 4 to the end of the array
arr.append(5) #push 5 to the end of the array
print(arr)

arr.pop() #pop the last element (5) from the array
print(arr)

arr.insert(1, 7)
print(arr) #inserts 7 at index 1, shifts the rest of the elements to the right

arr[0] = 0 #sets the first element to 0
print(arr)

#Initalize an arr of size n with default value of 1
n = 5 
arr = [1] * n
print(arr)
print(len(arr)) #prints 5 (size of the array)

#Careful: -1 is not out of bounds, 
#it's the last value
arr = [1, 2, 3]
print(arr[-1]) #prints 3 (last element)

#Indexing -2 is the second to last value, etc.
print(arr[-2]) #prints 2 (second to last element)

#Sublists (slicing)
arr = [1, 2, 3, 4]
print(arr[1:3]) #prints [2, 3] (from index 1 to index 2)

#Similar to for-loop ranges, last index is
# non-inclusive
print(arr[0:4]) #prints [1, 2, 3, 4] (from index 0 to index 3)

#Unpacking
a, b, c = [1, 2, 3]

#Loop through arrays
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

#Without index
for n in nums:
    print(n)

#with index and value
for i, n in enumerate(nums):
    print(i, n)

#Loop through multiple arrays simultaneously
#with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

#Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

#Sorting
arr = [5, 4, 7, 3, 8]
arr.sort() #sorts in ascending order
print(arr)

arr.sort(reverse=True) #sorts in descending order
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort() #sorts in ascending order
print(arr)

#custom sort (by length of string)
arr.sort(key = lambda x: len(x)) #sorts in ascending order by length of string
print(arr)

#list comprehensions
arr = [ i for i in range(5) ] #creates a list of [0, 1, 2, 3, 4]
print(arr)
arr = [i+i for i in range(5)] #creates a list of [0, 2, 4, 6, 8]
print(arr)

#2-D lists
arr = [[0] * 4 for i in range(4)] #this makes a 4 by 4 grid array of 0s

#Strings are similar to arrays
s = "abc"
print(s[0:2]) #prints ab (slices)

#But they are immutable (we can't modify or reassign the character at index 0)
#s[0] = "A" doesnt work, gets an error

#So this creates a new string
s += "def"
print(s) #prints abcdef

#Valid numeric strings can be converted
print(int("123") + int("123")) #prints 246

#And numbers can be converted to strings
print(str(123) + str(123)) #prints 123123

# # In rare cases you may need the ASCII value
# of a char
print(ord("a")) #prints 97
print(ord("b")) #prints 98

#combine a list of strings (with an empty string
# delimitor)
strings = ["ab", "cd", "ef"]
print(" ".join(strings)) #prints ab cd ef

#Queues (double ended queue)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue) #prints deque([1, 2])

queue.popleft()
print(queue) #prints deque([2])

queue.appendleft(1)
print(queue) #adds the 1 back and prints deque([1, 2])

queue.pop() #pops the right element 2
print(queue) #prints deque([1])

#HashSet

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

#list to set
print(set([1, 2, 3]))

#Set comprehension
mySet = { i for i in range(5) }
print(mySet)

#HashMap (aka dict) -- MOST GONNA USE
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap)) #prints the number of keys in the hashmap

# we can modify the value attached to a key
myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap) #checks if the key "alice" exists in the Hashmap

myMap.pop("alice") #we can also remove a key from the hashmap
print("alice" in myMap)

#manually inserting in hashmaps
myMap = { "alice": 90, "bob": 70 } #we can initalize pairs in the hashmap

#Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)
#helpful in creating graphs or adjacency lists

#Looping through maps
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

#Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

#Can't modify
#tup[0] = 0 wont work

#tuples can be used as a key for hash map/set
myMap = { (1, 2): 3}
print(myMap[(1, 2)]) #prints 3

mySet = set()
mySet.add((1, 2)) 
print((1, 2) in mySet) #prints True

#lists can't be keys
#myMap[[3,4]] = 5 wont work

#Heaps
import heapq

#under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

#Min is always at index 0
print(minHeap[0])
print(minHeap)

while len(minHeap):
    print(heapq.heappop(minHeap))

#No max heaps by default, work around is
#to use min heap and multiply by -1 when
#push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

#Max is always index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print( -1 * heapq.heappop(maxHeap))

#Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

#Functions
def myFunc(n,m):
    return n * m

print(myFunc(3, 4))

#Nested functions have acces to outer variables
#useful for recursive problems
def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

#can modify objects but not reassign
#unless using nonlocal keyword
def double(arr, val):
    def helper():
        #Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        #will only modify val in the helper scope
        #val *= 2

        #this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

#Class 
class MyClass:
    #Constructor
    def __init__(self, nums):
        #create member variables
        self.nums = nums
        self.size = len(nums)

    #self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

