# # Find the sum of all elements in a list

# lst=[1,2,3,4,5]
# total=0
# for i in lst:
#     total+=i
# print(total)

# # Find average of elements in a list

# lst = list(map(int, input().split()))
# total=0
# count=0
# for i in lst:
#     total+=i
#     count+=1
# if count==0:
#     print(0)
# else:
#     print(total/count)

# # Find the maximum and minimum in a list (in one loop)
# lst=list(map(int,input().split()))
# min_num=lst[0]
# max_num=lst[0]
# for i in lst:
#     if i<min_num:
#         min_num=i
#     if i>max_num:
#         max_num=i
# print(min_num)
# print(max_num)


# # Count even and odd numbers in a list
# lst=list(map(int,input().split()))
# even_count=0
# odd_count=0
# for i in lst:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("Even=",even_count)
# print("Odd=",odd_count)

# # Reverse a list (without using reverse() or slicing)
# lst=list(map(int,input().split()))
# lst1=[]
# for i in range(len(lst)-1,-1,-1):
#     lst1.append(lst[i])
# print(lst1)

# lst=list(map(int,input().split()))
# lst1=[]
# for i in lst:
#     lst1.insert(0,i)
# print(lst1)

# # Find the second smallest number in a list

# lst=list(map(int,input().split()))
# smallest=second=float('inf')
# for num in lst:
#     if num<smallest:
#         second=smallest
#         smallest=num
#     elif num<second and num!=smallest:
#         second=num
# print(second)

# lst=list(map(int,input().split()))
# lst=list(set(lst))
# lst.sort()
# print(lst[1])

# # Check if a list is sorted (ascending)
# lst=list(map(int,input().split()))
# for i in range(len(lst)-1):
#     if lst[i]>lst[i+1]:
#         print(False)
#         break
# else:
#     print(True)


# print(lst==sorted(lst))


# # Remove duplicates from a list (keep order)
# lst=list(map(int,input().split()))
# result=[]
# for i in lst:
#     if i not in result:
#         result.append(i)
# print(result)

# lst=list(map(int,input().split()))
# result=[]
# seen=set()
# for i in lst:
#     if i not in seen:
#         result.append(i)
#         seen.add(i)
# print(result)


# # Find all pairs in a list whose sum equals a target

# lst=[1,2,4,3,3,5,6]
# target=6
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             print((lst[i],lst[j]))

# lst = [2, 4, 3, 5, 7]
# target = 7

# seen = set()

# for num in lst:
#     complement = target - num
#     if complement in seen:
#         print((complement, num))
#     seen.add(num)

# # Find the intersection of two lists

# lst1=[1,2,3,3,4]
# lst2=[3,4,5,6]
# lst3=[]
# for i in lst1:
#     if i in lst2 and i not in lst3:
#             lst3.append(i)
# print(lst3)


# lst1=[1,2,3,5]
# lst2=[2,4,5,6]
# print(list(set(lst1)&set(lst2)))
            
# # Find the union of two lists (no duplicates)

# lst1=[1,2,3]
# lst2=[3,4,5]
# result=[]
# for i in lst1:
#     if i not in result:
#         result.append(i)
# for i in lst2:
#     if i not in result:
#         result.append(i)
# print(result)

# print(list(set(lst1)|set(lst2)))

# # Find the missing number in a list (1 to n)
# lst=[1,2,4,5]
# n=len(lst)+1
# total_sum=n*(n+1)//2
# actual_sum=sum(lst)
# print(total_sum-actual_sum)

# lst=[1,2,3,4,5]
# n=len(lst)+1
# for i in range(1,n+1):
#     if i not in lst:
#         print(i)
#         break


# # Move all zeros to end of list (maintain order)

# lst=list(map(int,input().split()))
# result=[]
# for i in lst:
#     if i!=0:
#         result.append(i)
# zero_count=lst.count(0)
# for _ in range(zero_count):
#     result.append(0)
# print(result)

# lst=[0,1,0,5,6,0,7]
# pos=0
# for i in range(len(lst)):
#     if lst[i]!=0:
#         lst[pos]=lst[i]
#         pos+=1
# for i in range(pos,len(lst)):
#     lst[i]=0
# print(lst)


# Find the maximum subarray sum (Kadane’s Algorithm – basic)

# lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# max_sum = lst[0]
# current_sum = lst[0]

# for i in range(1, len(lst)):
#     current_sum = max(lst[i], current_sum + lst[i])
#     max_sum = max(max_sum, current_sum)

# print(max_sum)

# Rotate a list to the right by k steps

lst = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst)   # handle large k

result = lst[-k:] + lst[:-k]

print(result)

lst = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    last = lst[-1]
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = last

print(lst)