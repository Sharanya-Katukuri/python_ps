# Reverse a string
word=input("enter a string:")
print(word[::-1])

word2=input("enter a string:")
rev=""
for ch in word2:
    rev=ch+rev
print(rev)

# Check if a string is a palindrome
str1=input("enter a string:").lower()
rev=""
for char in str1:
    rev=char+rev
if rev==str1:
    print("Palindrome:TRUE")
else:
    print("Palindrome:FALSE")


# Count number of vowels in a string
string=input("enter a string:").lower()
count=0
for chr in string:
    if chr in "aeiou":
        count+=1
print(count)

# Count number of consonants in a string
string=input("enter a string:").lower()
count=0
for char in string:
    if char.isalpha() and char not in "aeiou":
        count+=1
print(count)

# Find length of a string WITHOUT using len()

string=input("enter a string:")
count=0
for _ in string:
    count+=1
print(count)

# Count frequency of each character in a string

string=input("enter a string:")
freq={}
for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# Find the largest number in a list

list1=[1,2,3,6,7,9]
max_num=list1[0]
for i in list1:
    if i>max_num:
        max_num=i
print(max_num)

# Find the smallest number in a list

list2=[2,3,6,7,1,5,8,9]
min_num=list2[0]
for i in list2:
    if i<min_num:
        min_num=i
print(min_num)

# Remove duplicates from a string (keep order)

string=input("enter a string:")
string2=""
for char in string:
    if char not in string2:
        string2+=char
print(string2)


# Check if two strings are anagrams

string1=input("enter a string:")
string2=input("enter a string:")
if sorted(string1)==sorted(string2):
    print("true")
else:
    print("false")

# Find second largest number in a list

nums = [3, 7, 2, 9, 5]

largest = second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)

# Count digits, letters, and special characters in a string

string=input("enter a string:")
letter=0
digits=0
special=0
for i in string:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1
print("Letters:",letter)
print("Digits:",digits)
print("Special:",special)


# Replace all spaces in a string with -
string=input("enter a string:")
print(string.replace(" ","-"))

string=input("enter a string:")
result=""
for chr in string:
    if chr==" ":
        result+="-"
    else:
        result+=chr
print(result)

# Find first non-repeating character in a string

string=input("enter a string:")
freq={}
for ch in string:
    freq[ch]=freq.get(ch,0)+1
for ch in string:
    if freq[ch]==1:
        print(ch)

# Check if a string contains only digits
string=input("enter a string:")
if string.isdigit():
    print("true")
else:
    print("false")

string=input("enter a string:")
for ch in string:
    if not ch.isdigit():
        print("False")
        break
else:
    print("True")
        