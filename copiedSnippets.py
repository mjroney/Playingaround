'''
all_equal
Check if all elements in a list are equal.

Use [1:] and [:-1] to compare all the values in the given list.
'''
def all_equal(lst):
  return lst[1:] == lst[:-1]

'''
all_unique
Returns True if all the values in a flat list are unique, False otherwise.

Use set() on the given list to remove duplicates, compare its length with the length of the list.
'''
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True

'''
bifurcate
Splits values into two groups. If an element in filter is True, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group.

Use list comprehension and enumerate() to add elements to groups, based on filter.
'''
def bifurcate(lst, filter):
  return [
    [x for i,x in enumerate(lst) if filter[i] == True],
    [x for i,x in enumerate(lst) if filter[i] == False]
  ]

'''
bifurcate_by
Splits values into two groups according to a function, which specifies which group an element in the input list belongs to. If the function returns True, the element belongs to the first group; otherwise, it belongs to the second group.

Use list comprehension to add elements to groups, based on fn.
'''
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]

'''
chunk
Chunks a list into smaller lists of a specified size.

Use list() and range() to create a list of the desired size. Use map() on the list and fill it with splices of the given list. Finally, return use created list.

from math import ceil
'''
def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(0, ceil(len(lst) / size)))))

'''
compact
Removes falsey values from a list.

Use filter() to filter out falsey values (False, None, 0, and "").
'''
def compact(lst):
  return list(filter(bool, lst))

'''
count_by
Groups the elements of a list based on the given function and returns the count of elements in each group.

Use map() to map the values of the given list using the given function. Iterate over the map and increase the element count each time it occurs.
'''
def count_by(arr, fn=lambda x: x):
  key = {}
  for el in map(fn, arr):
    key[el] = 1 if el not in key else key[el] + 1
  return key

'''
count_occurences
Counts the occurrences of a value in a list.

Increment a counter for every item in the list that has the given value and is of the same type.
'''
def count_occurrences(lst, val):
  return len([x for x in lst if x == val and type(x) == type(val)])

'''
deep_flatten
Deep flattens a list.

Use recursion. Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use list.extend() with an empty list and the spread function to flatten a list. Recursively flatten each element that is a list.
'''
def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

def deep_flatten(lst):
  result = []
  result.extend(
    spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
  return result

'''
difference
Returns the difference between two iterables.

Create a set from b, then use list comprehension on a to only keep values not contained in the previously created set, _b.
'''
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]

'''
difference_by
Returns the difference between two lists, after applying the provided function to each list element of both.

Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values not contained in the previously created set, _b.
'''
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]

'''
every
Returns True if the provided function returns True for every element in the list, False otherwise.

Use all() in combination with map and fn to check if fn returns True for all elements in the list.
'''
def every(lst, fn=lambda x: x):
  return all(map(fn, lst))

'''
every_nth
Returns every nth element in a list.

Use [nth-1::nth] to create a new list that contains every nth element of the given list.
'''
def every_nth(lst, nth):
  return lst[nth-1::nth]

'''
filter_non_unique
Filters out the non-unique values in a list.

Use list comprehension and list.count() to create a list containing only the unique values.
'''
def filter_non_unique(lst):
  return [item for item in lst if lst.count(item) == 1]

'''
flatten
Flattens a list of lists once.

Use nested list comprehension to extract each value from sub-lists in order.
'''
def flatten(lst):
  return [x for y in lst for x in y]

'''
group_by
Groups the elements of a list based on the given function.

Use map() and fn to map the values of the list to the keys of an object. Use list comprehension to map each element to the appropriate key.
'''
def group_by(lst, fn):
    return {key : [el for el in lst if fn(el) == key] for key in map(fn,lst)}

'''
has_duplicates
Returns True if there are duplicate values in a flast list, False otherwise.

Use set() on the given list to remove duplicates, compare its length with the length of the list.
'''
def has_duplicates(lst):
  return len(lst) != len(set(lst))

'''
head
Returns the head of a list.

use lst[0] to return the first element of the passed list.
'''
def head(lst):
  return lst[0]

'''
initial
Returns all the elements of a list except the last one.

Use lst[0:-1] to return all but the last element of the list.
'''
def initial(lst):
  return lst[0:-1]

'''
initialize_2d_list
Initializes a 2D list of given width and height and value.

Use list comprehension and range() to generate h rows where each is a list with length h, initialized with val. If val is not provided, default to None.
'''
def initialize_2d_list(w,h, val = None):
  return [[val for x in range(w)] for y in range(h)]

'''
initialize_list_with_range
Initializes a list containing the numbers in the specified range where start and end are inclusive with their common difference step.

Use list and range() to generate a list of the appropriate length, filled with the desired values in the given range. Omit start to use the default value of 0. Omit step to use the default value of 1.
'''
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))

'''
initialize_list_with_values
Initializes and fills a list with the specified value.

Use list comprehension and range() to generate a list of length equal to n, filled with the desired values. Omit val to use the default value of 0.
'''
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]

'''
intersection
Returns a list of elements that exist in both lists.

Create a set from b, then use list comprehension on a to only keep values contained in both lists.
'''
def intersection(a, b):
  _b = set(b)
  return [item for item in a if item in _b]

'''
intersection_by
Returns a list of elements that exist in both lists, after applying the provided function to each list element of both.

Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values contained in both lists.
'''
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]

'''
last
Returns the last element in a list.

use lst[-1] to return the last element of the passed list.
'''
def last(lst):
  return lst[-1]

'''
longest_item
Takes any number of iterable objects or objects with a length property and returns the longest one. If multiple objects have the same length, the first one will be returned.

Use max() with len as the key to return the item with the greatest length.
'''
def longest_item(*args):
  return max(args, key = len)

'''
max_n
Returns the n maximum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in descending order).

Use sorted() to sort the list, [:n] to get the specified number of elements. Omit the second argument, n, to get a one-element list.
'''
def max_n(lst, n=1):
  return sorted(lst, reverse=True)[:n]

'''
min_n
Returns the n minimum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in ascending order).

Use sorted() to sort the list, [:n]to get the specified number of elements. Omit the second argument,n`, to get a one-element list.
'''
def min_n(lst, n=1):
  return sorted(lst, reverse=False)[:n]

'''
none
Returns False if the provided function returns True for at least one element in the list, True otherwise.

Use all() and fn to check if fn returns False for all the elements in the list.
'''
def none(lst, fn=lambda x: x):
  return all(not fn(x) for x in lst)

'''
offset
Moves the specified amount of elements to the end of the list.

Use lst[offset:] and lst[:offset] to get the two slices of the list and combine them before returning.
'''
def offset(lst, offset):
  return lst[offset:] + lst[:offset]

'''
sample
Returns a random element from an array.

Use randint() to generate a random number that corresponds to an index in the list, return the element at that index.
'''
from random import randint

def sample(lst):
  return lst[randint(0, len(lst) - 1)]

'''
shuffle
Randomizes the order of the values of an list, returning a new list.

Uses the Fisher-Yates algorithm to reorder the elements of the list.
'''
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst

'''
similarity
Returns a list of elements that exist in both lists.

Use list comprehension on a to only keep values contained in both lists.
'''
def similarity(a, b):
  return [item for item in a if item in b]

'''
some
Returns True if the provided function returns True for at least one element in the list, False otherwise.

Use any() in combination with map() and fn to check if fn returns True for any element in the list.
'''
def some(lst, fn=lambda x: x):
  return any(map(fn, lst))

'''
spread
Flattens a list, by spreading its elements into a new list.

Loop over elements, use list.extend() if the element is a list, list.append() otherwise.
'''
def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

'''
symmetric_difference
Returns the symmetric difference between two iterables, without filtering out duplicate values.

Create a set from each list, then use list comprehension on each one to only keep values not contained in the previously created set of the other.
'''
def symmetric_difference(a, b):
  _a, _b = set(a), set(b)
  return [item for item in a if item not in _b] + [item for item in b if item not in _a]

'''
symmetric_difference_by
Returns the symmetric difference between two lists, after applying the provided function to each list element of both.

Create a set by applying fn to each element in every list, then use list comprehension in combination with fn on each one to only keep values not contained in the previously created set of the other.
'''
def symmetric_difference_by(a, b, fn):
  _a, _b = set(map(fn, a)), set(map(fn, b))
  return [item for item in a if fn(item) not in _b] + [item for item in b if fn(item) not in _a]

'''
tail
Returns all elements in a list except for the first one.

Return lst[1:] if the list's length is more than 1, otherwise, return the whole list.
'''
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst

'''
union
Returns every element that exists in any of the two lists once.

Create a set with all values of a and b and convert to a list.
'''
def union(a,b):
  return list(set(a + b))

'''
union_by
Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

Create a set by applying fn to each element in a, then use list comprehension in combination with fn on b to only keep values not contained in the previously created set, _a. Finally, create a set from the previous result and a and transform it into a list
'''
def union_by(a,b,fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))

'''
unique_elements
Returns the unique elements in a given list.

Create a set from the list to discard duplicated values, then return a list from it.
'''
def unique_elements(li):
  return list(set(li))

'''
zip
Creates a list of elements, grouped based on the position in the original lists.

Use max combined with list comprehension to get the length of the longest list in the arguments. Loop for max_length times grouping elements. If lengths of lists vary, use fill_value (defaults to None).
'''
def zip(*args, fillvalue=None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fillvalue for k in range(len(args))
    ])
  return result

'''
Math
average
Returns the average of two or more numbers.

Use sum() to sum all of the args provided, divide by len(args).
'''
def average(*args):
  return sum(args, 0.0) / len(args)

'''
average_by
Returns the average of a list, after mapping each element to a value using the provided function.

Use map() to map each element to the value returned by fn. Use sum() to sum all of the mapped values, divide by len(lst).
'''
def average_by(lst, fn=lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)

'''
clamp_number
Clamps num within the inclusive range specified by the boundary values a and b.

If num falls within the range, return num. Otherwise, return the nearest number in the range.
'''
def clamp_number(num,a,b):
  return max(min(num, max(a,b)),min(a,b))

'''
digitize
Converts a number to an array of digits.

Use map() combined with int on the string representation of n and return a list from the result.
'''
def digitize(n):
  return list(map(int, str(n)))

'''
factorial
Calculates the factorial of a number.

Use recursion. If num is less than or equal to 1, return 1. Otherwise, return the product of num and the factorial of num - 1. Throws an exception if num is a negative or a floating point number.
'''
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception(
      f"Number( {num} ) can't be floating point or negative ")
  return 1 if num == 0 else num * factorial(num - 1)

'''
fibonacci
Generates an array, containing the Fibonacci sequence, up until the nth term.

Starting with 0 and 1, use list.apoend() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n. If nis less or equal to0, return a list containing 0`.
'''
def fibonacci(n):
  if n <= 0:
    return [0]

  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)

  return sequence

'''
gcd
Calculates the greatest common divisor of a list of numbers.

Use reduce() and math.gcd over the given list.
'''
from functools import reduce
import math

def gcd(numbers):
  return reduce(math.gcd, numbers)

'''
in_range
Checks if the given number falls within the given range.

Use arithmetic comparison to check if the given number is in the specified range. If the second parameter, end, is not specified, the range is considered to be from 0 to start.
'''
def in_range(n, start, end = 0):
  if (start > end):
    end, start = start, end
  return start <= n <= end

'''
is_divisible
Checks if the first numeric argument is divisible by the second one.

Use the modulo operator (%) to check if the remainder is equal to 0.
'''
def is_divisible(dividend, divisor):
  return dividend % divisor == 0

'''
is_even
Returns True if the given number is even, False otherwise.

Checks whether a number is odd or even using the modulo (%) operator. Returns True if the number is even, False if the number is odd.
'''
def is_even(num):
  return num % 2 == 0

'''
is_odd
Returns True if the given number is odd, False otherwise.

Checks whether a number is even or odd using the modulo (%) operator. Returns True if the number is odd, False if the number is even.
'''
def is_odd(num):
  return num % 2 != 0

'''
lcm advanced
Returns the least common multiple of two or more numbers.

Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use math.gcd() and lcm(x,y) = x * y / gcd(x,y) to determine the least common multiple.
'''
from functools import reduce
import math

def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

def lcm(*args):
  numbers = []
  numbers.extend(spread(list(args)))

  def _lcm(x, y):
    return int(x * y / math.gcd(x, y))

  return reduce((lambda x, y: _lcm(x, y)), numbers)

'''
max_by
Returns the maximum value of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use max() to return the maximum value.
'''
def max_by(lst, fn):
  return max(map(fn,lst))

'''
min_by
Returns the minimum value of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use min() to return the minimum value.
'''
def min_by(lst, fn):
  return min(map(fn,lst))

'''
rads_to_degrees
Converts an angle from radians to degrees.

Use math.pi and the radian to degree formula to convert the angle from radians to degrees.
'''
import math

def rads_to_degrees(rad):
  return (rad * 180.0) / math.pi

'''
sum_by
Returns the sum of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use sum() to return the sum of the values.
'''
def sum_by(lst, fn):
  return sum(map(fn,lst))

'''
Object
keys_only
Returns a flat list of all the keys in a flat dictionary.

Use dict.keys() to return the keys in the given dictionary. Return a list() of the previous result.
'''
def keys_only(flat_dict):
  return list(flat_dict.keys())

'''
map_values
Creates an object with the same keys as the provided object and values generated by running the provided function for each value.

Use dict.keys() to iterate over the object's keys, assigning the values produced by fn to each key of a new object.
'''
def map_values(obj, fn):
  ret = {}
  for key in obj.keys():
    ret[key] = fn(obj[key])
  return ret

'''
values_only
Returns a flat list of all the values in a flat dictionary.

Use dict.values() to return the values in the given dictionary. Return a list() of the previous result.
'''
def values_only(dict):
  return list(dict.values())

'''
String
byte_size
Returns the length of a string in bytes.

Use string.encode('utf-8') to encode the given string and return its length.
'''
def byte_size(string):
  return len(string.encode('utf-8'))

'''
camel
Converts a string to camelcase.

Break the string into words and combine them capitalizing the first letter of each word, using a regexp, title() and lower.
'''
import re

def camel(s):
  s = re.sub(r"(\s|_|-)+", " ", s).title().replace(" ", "")
  return s[0].lower() + s[1:]

'''
capitalize
Capitalizes the first letter of a string.

Capitalize the first letter of the string and then add it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to True to convert to lowercase.
'''
def capitalize(string, lower_rest=False):
  return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])

'''
capitalize_every_word
Capitalizes the first letter of every word in a string.

Use string.title() to capitalize first letter of every word in the string.
'''
def capitalize_every_word(string):
  return string.title()

'''
decapitalize
Decapitalizes the first letter of a string.

Decapitalize the first letter of the string and then add it with rest of the string. Omit the upper_rest parameter to keep the rest of the string intact, or set it to True to convert to uppercase.
'''
def decapitalize(string, upper_rest=False):
  return str[:1].lower() + (str[1:].upper() if upper_rest else str[1:])

'''
is_anagram
Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

Use str.replace() to remove spaces from both strings. Compare the lengths of the two strings, return False if they are not equal. Use sorted() on both strings and compare the results.
'''
def is_anagram(str1, str2):
  _str1, _str2 = str1.replace(" ", ""), str2.replace(" ", "")

  if len(_str1) != len(_str2):
    return False
  else:
    return sorted(_str1.lower()) == sorted(_str2.lower())

'''
kebab
Converts a string to kebab case.

Break the string into words and combine them adding - as a separator, using a regexp.
'''
import re

def kebab(str):
  return re.sub(r"(\s|_|-)+","-",
    re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: mo.group(0).lower(),str)
  )

'''
n_times_string
Prints out the same string a defined number of times.

Repeat the string n times, using the * operator.
'''
def n_times_string(str,n):
  return (str * n)

'''
palindrome
Returns True if the given string is a palindrome, False otherwise.

Use str.lower() and re.sub() to convert to lowercase and remove non-alphanumeric characters from the given string. Then, compare the new string with its reverse.
'''
from re import sub

def palindrome(string):
  s = sub('[\W_]', '', string.lower())
  return s == s[::-1]

'''
snake
Converts a string to snake case.

Break the string into words and combine them adding _-_ as a separator, using a regexp.
'''
import re

def snake(str):
  return re.sub(r"(\s|_|-)+","-",
    re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: mo.group(0).lower(),str)
  )

'''
split_lines
Splits a multiline string into a list of lines.

Use str.split() and '\n' to match line breaks and create a list.
'''
def split_lines(str):
  return str.split('\n')

'''
Utility
cast_list
Casts the provided value as an array if it's not one.

Use isinstance() to check if the given value is a list and return it as-is or encapsulated in a list accordingly.
'''
def cast_list(val):
  return val if isinstance(val, list) else [val]
'''
30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
Fatos Morina
September 7, 2019

Python represents one of the most popular languages that many people use it in data science and machine learning, web development, scripting, automation, etc.
Part of the reason for this popularity is its simplicity and easiness to learn it.
If you are reading this, then it is highly likely that you already use Python or at least have an interest in it.
In this article, we will briefly see 30 short code snippets that you can understand and learn in 30 seconds or less.
'''

'''1. All unique
The following method checks whether the given list has duplicate elements. It uses the property of set() which removes duplicate elements from the list.'''


def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True

'''2. Anagrams
This method can be used to check if two strings are anagrams.
An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.'''


from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True

'''3. Memory
This snippet can be used to check the memory usage of an object.'''


import sys 

variable = 30 
print(sys.getsizeof(variable)) # 24

'''4. Byte size
This method returns the length of a string in bytes.'''


def byte_size(string):
    return(len(string.encode('utf-8')))
    
    
byte_size('😀') # 4
byte_size('Hello World') # 11   

'''5. Print a string N times
This snippet can be used to print a string n times without having to use loops to do it.'''

n = 2; 
s ="Programming"; 

print(s * n); # ProgrammingProgramming

'''6. Capitalize first letters
This snippet simply uses the method title() to capitalize first letters of every word in a string.'''

s = "programming is awesome"

print(s.title()) # Programming Is Awesome

'''7. Chunk
This method chunks a list into smaller lists of a specified size.'''

def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

'''8. Compact
This method removes falsy values (False, None, 0 and “”) from a list by using filter().'''


def compact(lst):
    return list(filter(bool, lst))
  
  
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]

'''9. Count by
This snippet can be used to transpose a 2D array.'''

array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]

'''10. Chained comparison
You can do multiple comparisons with all kinds of operators in a single line.'''

a = 3
print( 2 < a < 8) # True
print(1 == a < 2) # False

'''11. Comma-separated
This snippet can be used to turn a list of strings into a single string with each element from the list separated by commas.'''

hobbies = ["basketball", "football", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies)) # basketball, football, swimming

'''12. Get vowels
This method gets vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) found in a string.'''

def get_vowels(string):
    return [each for each in string if each in 'aeiou'] 


get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []

'''13. Decapitalize
This method can be used to turn the first letter of the given string into lowercase.'''

def decapitalize(str):
    return str[:1].lower() + str[1:]
  
  
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'

'''14. Flatten
The following methods flatten a potentially deep list using recursion.'''

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

'''15. Difference
This method finds the difference between two iterables by keeping only the values that are in the first one.'''

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]

'''16. Difference by
The following method returns the difference between two lists after applying a given function to each element of both lists.'''

def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]

'''17. Chained function call
You can call multiple functions inside a single line.'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9   

'''18. Has duplicates
The following method checks whether a list has duplicate values by using the fact that set() contains only unique elements.'''

def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
    
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
has_duplicates(x) # True
has_duplicates(y) # False

'''19. Merge two dictionaries
The following method can be used to merge two dictionaries.'''

def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}

'''In Python 3.5 and above, you can also do it like the following:'''

def merge_dictionaries(a, b)
   return {**a, **b}


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}

'''20. Convert two lists into a dictionary
The following method can be used to convert two lists into a dictionary.'''

def to_dictionary(keys, values):
    return dict(zip(keys, values))
    

keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}

'''21. Use enumerate
This snippet shows that you can use enumerate to get both the values and the indexes of lists.'''

list = ["a", "b", "c", "d"]
for index, element in enumerate(list): 
    print("Value", element, "Index ", index, )
# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
#('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)  

'''22. Time spent
This snippet can be used to calculate the time it takes to execute a particular code.'''


import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)

'''23. Try else
You can have an else clause as part of a try/except block, which is executed if no exception is thrown.'''

try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.

'''24. Most frequent
This method returns the most frequent element that appears in a list.'''

def most_frequent(list):
    return max(set(list), key = list.count)
  

numbers = [1,2,1,2,3,2,1,4,2]
most_frequent(numbers)  

'''25. Palindrome
This method checks whether a given string is a palindrome.'''

def palindrome(a):
    return a == a[::-1]


palindrome('mom') # True

'''26. Calculator without if-else
The following snippet shows how you can write a simple calculator without the need to use if-else conditions.'''

import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25

'''27. Shuffle
This snippet can be used to randomize the order of the elements in a list. Note that shuffle works in place, and returns None.'''

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo) 
print(foo) # [1, 4, 3, 2] , foo = [1, 2, 3, 4]

'''28. Spread
This method flattens a list similarly like [].concat(…arr) in JavaScript.'''

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]

'''29. Swap values
A really quick way for swapping two variables without having to use an additional one.'''

a, b = -1, 14
a, b = b, a

print(a) # 14
print(b) # -1

'''30. Get default value for missing keys
This snippet shows how you can get a default value in case a key you are looking for is not included in the dictionary.'''

d = {'a': 1, 'b': 2}

print(d.get('c', 3)) # 3


'''This was a short list of snippets that you may find useful in your everyday work.
It was highly based on this GitHub repository (https://github.com/30-seconds/30_seconds_of_knowledge)
in which you can find many other useful code snippets both in Python and other languages and technologies.'''
