# space1= 'x'
# space2= 'o'
# space3= 'x'
# space4= 'o'
# space5= 'x'
# space6= 'o'
# space7= 'x'
# space8= 'x'
# space9= 'o'

# print('     |     |     ')
# print(f"   {space1} |  {space2}  |  " )
# print('     |     |     ')
# print('-----------------')
# print('     |     |     ')
# print(f"     |  {space5}  |  " )
# print('     |     |     ')
# print('-----------------')
# print('     |     |     ')
# print(f"   {space7} |  {space8}  |  " )
# print('     |     |     ')

# age= input("give me your age in years")
# age = int(age)*365
# print(age)
# import datetime
# day= input("give me your Day of birth ")
# month= input("give me your month of birth ")
# year= input("give me your year of birth ")
# current= datetime.datetime.now()
# dob = datetime.datetime(int(year),int(month),int(day))
# print(current-dob)

# for number in range(3):
#     print('     |     |     ')
# print('-----------------')
# for number in range(3):
#     print('     |     |     ')
# print('-----------------')
# for number in range(3):
#     print('     |     |     ')

# for number in range(11):
#     if number == (3):
#         print('----------------')
#     elif number == (7):
#         print('----------------')
#     else:
#         print('     |     |     ')
# name= 'Harvey'
# age= '23'
# color= 'green'
# print(f"I am {name}, {age} years old and I like {color}")

# breakfast= 'Toast'
# lunch= "carapulcra"
# dinner= "dunno"
# breakfast= 'cereal'
# lunch= "dunno"
# dinner= "dunno"
# print(f"{breakfast} {lunch} {dinner}")
 

# def play_lotto():
#     while True:
#         Play_lottery = input ("Would you like to play the lottery? ")
#         if not Play_lottery[0].lower() == ("y"):
#             print("Enter 'Y' to begin")
#             continue
#         else:
#             print("Good luck!")
#             break
#     while True:
#         lucky_dip = input ("To generate your ticket enter Y  ")
#         if not lucky_dip[0].lower() == ("y"):
#             print ("Please enter Y")
#             continue 
#         else:
#             print ("Your numbers for today are:")
#             break
#     import random
#     lottery_numbers = list(range(1,31))
#     random.shuffle(lottery_numbers)
#     three_nums = lottery_numbers[:3]
#     print(three_nums)
#     while True:
#         result = input ("Would you like today's results? Enter Y   ")
#         if not result[0].lower() == ("y"):
#             print ("Please enter 'Y'")
#             continue 
#         else:
#             print ("Today's winning numbers are:")
#             break
#     Correct_numbers = list (range(1,31))
#     random.shuffle(Correct_numbers)
#     three_winning = Correct_numbers[:3]
#     print (three_winning)
#     counter = 0
#     for number in three_nums:
#         if number in three_winning:
#             counter += 1
#     print ("You matched   "+str(counter) +"  numbers!")
#     prize = 0
#     for number in three_nums:
#         if number in three_winning:
#             prize += 100
#     print ("You win £    "+str(prize))

# play_lotto()

def cashmachine(pin,amount,balance): 
    
    if pin==3678:
        print(f"(taking £{amount} from your account. Your balance is £{balance-amount})") 
    else:
        print('wrong pin')
        endgame()

balance=10
while balance>0:
    amount=2
    cashmachine(3678,amount,balance)
    balance-=amount
    # print(balance)
