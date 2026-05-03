# # Find the first repeating character in a string
# string=input("enter a string:")
# seen=set()
# for ch in string:
#     if ch in seen:
#         print(ch)
#         break
#     seen.add(ch)
# else:
#     print("No repeating characters")


# # Find the first non-repeating character in a string
# string=input("enter a string:")
# freq={}
# for char in string:
#         freq[char]=freq.get(char,0)+1
# for ch in string:
#         if freq[ch]==1:
#                 print(ch)
#                 break
# else:
#         print("No non-repeacting character")

# # Check if two strings are isomorphic
# s1=input("enter first string:")
# s2=input("enter second string:")
# if len(s1)!=len(s2):
#     print(False)
# else:
#     map1={}
#     map2={}
#     for c1,c2 in zip(s1,s2):
#         if c1 in map1:
#             if map1[c1]!=c2:
#                 print(False)
#                 break
#         else:
#             map1[c1]=c2
#         if c2 in map2:
#             if map2[c2]!=c1:
#                 print(False)
#                 break
#         else:
#             map2[c2]=c1
#     else:
#         print(True)


# # Longest substring without repeating characters

# s=input("enter a string:")
# char_set=set()
# left=0
# max_length=0
# for right in range(len(s)):
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left+=1
#     char_set.add(s[right])
#     max_length=max(max_length,right-left+1)
# print(max_length)

# # Check if one string is a rotation of another
# s1=input("enter first string:")
# s2=input("enter second string:")
# if len(s1)==len(s2) and s2 in (s1+s1):
#     print(True)
# else:
#     print(False)