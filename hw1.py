
# celcius to farenheit
def cToF(t):
    return t*(9/5) + 32

# farenheit to celcius
def fToC(t):
    return (t-32)*5/9

# returns a list of strings from the input list L that are shorter than n
def shortStrings(L,n):
    def f(s):
        return n-len(s)>0
    newList = list(filter(f,L))
    return newList

# returns a list of strings from L but they have have their characters doubled
def doubleStrings(L):
    def f(s):
        return s*2
    new_list = list(map(f,L))
    return new_list

# translates s into Pig Latin
def pigLatin(s):
    y = list(s)
    y.append(y[0])
    y.pop(0)
    y.append('a')
    y.append('y')
    return(y)

# does this:
'''for s, returns a positive number, negative number, or zero depending on
the following conditions:
• a negative number if the string has more letters from the first half of the
alphabet
• 0 if the string has the same amount of letters from the first and second
half of the alphabet
• a positive number if the string has more letters from the second half of
the alphabet'''
import string
def stringBalance(s):
    alphabet = string.ascii_lowercase
    listString = list(s)
    def indexOf(c):
        return alphabet.index(c)
    mappedList = list(map(indexOf,listString))
    first_half = list(filter(lambda x: x<=12,mappedList))
    last_half = list(filter(lambda x: x>12,mappedList))
    return len(last_half)-len(first_half)

