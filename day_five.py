# def str_append_list_join(s, n):
#     l1 = []
#     i = 0
#     while i < n:
#         l1.append(s)
#         i += 1
#     print(l1)    
#     return ''.join(l1)

# str_append_list_join('hi', 4)

# #1
# string1= "Hello Danielle"
# list=string1.split()
# if len(list[0])>len(list[1]):
#     print(list[0])
# else:
#     print(list[1])

#2
# nums=[1,5]
# def addfun(nums):
#     nums= list(range(nums[0],nums[1]+1))
#     sumation=sum(nums)
#     print(sumation)
# addfun(nums)

# #3
# arr1=['dan', 'ben']
# arr2=['dan', 'andy', 'ben', 'stuart']
# arr3=[]
# def comparray(arr1,arr2):
#     for person in arr1:
#         for guy in arr2:
#             if person==guy:
#                 arr3.append(guy)
#     return arr3
# comparray(arr1,arr2)    
# print(arr3)   

#4
line="__________________"
char="B"
# print(char+line)
def charcross(char,line):
    for i in range(len(line)):
        charline=char+line
        line=line.replace(line[i],"B",1)
        if i>0:
            line=line.replace(line[i-1],"_",1)
        print(line)
    charline=f"{char}{line}"
    print(charline)

charcross(char,line)

# def in_one(l1, l2):
#     return set(l1) & set(l2)  #^, |, &
# print(in_one([1,2,3],[3,4,5]))

# def find_longest_string(l):
#     return max(l.split(), key=len)
# print(find_longest_string("this is hy and my nam"))


# import sys
# import time
# def pick_character(y, x, character):
#     if y == x:
#         return character
#     elif any([y == 25 and x < y,
#               y == 50 and x < y,
#               y == 75 and x < y,
#               y == 100 and x < y]):
#         return chr(5603)
#     elif x < y:
#         return chr(8226)
#     return " "
# def move(character, size, speed):
#     for x in range(size):
#         line = ["\b" * size, *[pick_character(y, x, character) for y in range(size)]]
#         sys.stdout.write("".join(line))
#         sys.stdout.flush()
#         time.sleep(speed)
#     sys.stdout.write("".join(["\b" * size]))
#     sys.stdout.flush()
# move(chr(5607), 101, 0.1)