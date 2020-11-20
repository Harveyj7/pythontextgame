# grinding_beans = False
# def grind_beans(grinding):
#     if grinding:
#         print("Stop")
#     else:
#         print("Start")
#     return not grinding
# grinding_beans = grind_beans(grinding_beans)

# coffee_order= [
#     "Alex-Cortado",
#     "Ben-Latte",
#     "Charlie- Whatever's new"
#     ]
# coffee_order.sort(reverse=True)
# print(coffee_order)

# websites=[
#     "facebook","google","reddit"
#     ]
# websites.append("pgth")
# websites.append("ph")
# # websites.pop()
# print(websites)

# numbers=[1,2,3,4,10,9]
# complete=False
# for number in numbers:
#     print(number)
#     complete=True
# #can use- else: print("loop didnt start")
# if not complete:
#     print('didnt start')

# numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# for number in numbers:
#     if number == 10:
#         print("Found 50")
#         break
#         print(f"Looking for 50, found: {number}")
#     else:
#         print("Didn't find what we were looking for")

# for number in numbers:
#     if number%2==1:
#         continue
#     print(number)

# num=0
# while num<10:
#     num+= 1
#     print(num)


# import random
# tries=[]
# number=10
# random_number=0
# while random_number != number:
#     tries.append(random_number)
#     random_number = random.randint(0,30)
#     print(random_number)
# print(f"took this many {len(tries)}")

# #1
# films=["titanic","2020","Ghostbusters","sixth sense"]
# for film in films:
#     print(film)
#     def film_check():
#         if films[2]=="Ghostbusters":
#             print("yay")
#         else:
#             print("boo")
# film_check()

##2
# count=0
# while count!=10:
#     count+=1
#     print(count)

# #3
# number=0
# import random
# while number<6:
#     rand= random.randint(1,30)
#     number+=1
#     print(rand)
#     if rand%7==0:
#         print("divible by 7")
#     else:
#         print("not divisible by 7")

# # 4
# user_guess = 0
# magic_number = 5

# while user_guess != magic_number:
# 	print('What is the magic number?')
# 	user_guess = int(input())

# print('You have correctly guessed the magic number!')


#5
numbers=list(range(5, 10))
print(numbers)
for number in numbers:
    ascending=list(range(1,number))
    descending=(ascending[::-1])
    descending.pop()
    print(f"this is current number: {number}")
    for descend in descending:     
        if number % descend ==0:
            print("not prime")
            break
        else:
            print("prime")
    # print(f"{descend} is a prime number")
    