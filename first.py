# if 5 > 2:
#     print("it is true")

# x = 2
# print(x)

# x = 4
# y = "string"

# print(type(y))

# cars = ["car1", "car2", "car3"]
# print(cars)
# x,y,z = cars
# print(x)
# print(y)
# print(z)

# print(x+y+z)

# print(4 == 4)

# y = "Hello World"
# def myfun():
#     global y 
#     y="new var"
    
# myfun()

# print("global variable" +   y)

# x = "hello world"
# y = 'h'
# z = 1j
# print(x[1])
# print(type(y))
# print(type(z))

# for x in "hello world":
#     print(x)

# cars = ["car1", "car2", "car3", "car1"]
# print(len(cars))
    
# cars.clear()
# print(cars)
    
# for x in cars:
#     print(x)
    
# i=0
# while i < len(cars):
#     print(cars[i])
#     i=i+1
    
# [print(x) for x in cars]

# cars = ["car1", "car2", "car3", "car1"]
# car1=[]


# #    if "1" in cars:
# #      car1.append(cars)
# # print(car1)


# # for x in range(1,11):
# #     print(x)
    
# sur=[55,46,34,67,29]
# sur.sort()
# print(sur)

# Surya= sur+cars
# print(Surya)

# tup=("car1", "car2", "car3")
# x = list(tup)
# x[0]="car9"
# tup=tuple(x)
# print(tup)

# s1={1,2,3,4}
# s2={4,5,6,7}
# print(s1 | s2)

# print(len(s1))
# print(len(s2))

# print(type(s1))

# # whileloops
# # number = 10
# # i=0
# # while i < number:
# #     print(i)
# #     i=i+1

# # # forloop
# # items = [1,2,3,4]
# # for item in items:
# #     print(item)
    
    
    
# #     #dictionaries
# # product_data = {
# #     "title": "iphone11",
# #     "price": "30000"
# # }

# # product_data["discount"] =  "11%";
# # print(product_data)  

# #  def sum(x,y):
# #     sum= x+y
# #     print(sum)

# # number1= int(input("enter first number:"))
# # number2= int(input("enter second number:"))

# # sum(number1,number2)
    
# n = int(input("enter the value: "))
# if n <=1:
#     n = int(input("please enter the values more the 1: "))
# for i in range(2,int(n**0.5)+1):
#     if n % i == 0:
#         print("it is not a prime number")
#         break
#     else:
#         print("it is a prime number")
#         break
 

# def myfun(n):
#     if n <=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n% i == 0:
#             return False
#     return True

# start=int(input("enter the starting value: "))
# end=int(input("enter the last value: "))
# print(f"prime number between {start} and {end} are:  ")
# for i in range(start,end+1):
#         print(i , end=' ')


# def myfun(n):
#     return str(n) == str(n)[::-1]

# n = int(input("enter any string for checking the palindrome:  "))
# if myfun(n):
#     print(f"{n} is a palindrome")
# else:
#     print(f"{n} is not a palindrome")

# def myfun(n):
#     return str(n) == str(n)[::-1]

# start=int(input("enter the starting value: "))
# end=int(input("enter the last value: "))
# print(f"prime number between {start} and {end} are:  ")
# for i in range(start,end+1):
#     if myfun(i):
#         print(i , end=' ')



n=int(input("enter the number of row: "))
for i in range(0,n):
    print(" " * (n - i)+ "*" * (2 * i - 1))





# # import two................
# ;;;;;;;;;
# ''''''''''''''




# {"name":"mrv"}
# try:
#     print("Surya")
# except:
#     print("show error")
# finally:
#     print("try and execpt block successfully run")



# def merge_sorted_lists(list, list1):
#     merged_list = []
#     i = j = 0
    
#     while i < len(list) and j < len(list1):
#         if list[i] < list1[j]:
#             merged_list.append(list[i])
#             i = i+1
#         else:
#             merged_list.append(list1[j])
#             j = j+1
#     while i < len(list):
#         merged_list.append(list[i])
#         i = i+1
#     while j < len(list1):
#         merged_list.append(list1[j])
#         j = j+1
#     return merged_list
    

# list = [2,6,5,8]
# list1 = [6,3,2,1]
# merged_list = merge_sorted_lists(list, list1)
# print(merged_list)

# list = [2,6,5,8]
# list1 = [6,3,2,1]
# list2= list+list1
# print(list2)

# def find_all_substrings(s):
#     substrings = []
#     n = len(s)
    
#     for i in range(n):
#         for j in range(i+1, n+1):
#             substrings.append(s[i:j])
            
#     return substrings

# s = "abcd"
# all_substrings = find_all_substrings(s)
# print(all_substrings)
           
           
           
# str1 ="race"
# str2 = "care"

# str1 = str1.lower()
# str2 = str2.lower()

# if (len(str1) == len(str2)):
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
    
#     if (sorted_str1 == sorted_str2):
#         print(str1   +   " and "   + str2  + " are anagrams")
#     else:
#         print(str1 + "ans" + str2  +" are not anagrams")
        
# else:
#     print(str1 + "and" + str2 + "are not anagrams")
    
    
    
# def count_frequency(string):
#     F = {}
#     for item in string:
#         if item in F:
#             F[item] +=1
#         else:
#             F[item] = 1
#     x = max(F.values())
#     y = []
#     for keys,values in F.items():
#         if values == x:
#             y.append(keys)
#     return y

# string = [1,2,2,3,3,5,7,8,8,8]
# print(count_frequency(string))







    
# list = [2,4,3,5,63,2,]
# se = set(list)
# print(se)

# def removeConsecutiveDuplicates(string):
#     result = ''
#     for i in range(len(string)):
#         if string[i]  != string[i-1]:         #if string[i]  == string[i-1]:
#             result += string[i]
#     return result

# string = "aaabbbccdddeee"
# result= removeConsecutiveDuplicates(string)
# print(result)

def myfun(n):
    for i in range(1, n+1):
        print( "*" *(n-i))
        
n=5
myfun(n)

# n = int(input("enter the number of players"))
# arr = map(int, input("enter the scores").split())
# n1 = list(set(arr))
# n2 = n1.sort()
# runnerup = n1[-2]
# print(runnerup)

