number = input("what is the number ")
number = int(number)
print(number)
if number >= 5:
    print("big num")
elif number < 0:
    print("small num")
else:
    print("medium num")

# else:
#     print("small num")
# print(chr(10597))
# and returns the first value if it is false otherwise it returns the second value
# or returns the first value if it is true otherwise it returns the second value

# #1
# password= 'fufyhhghf'
# if len(password)<8:
#     print('password too short')
# else:
#     print(password)

# #2
# num= 70
# if num%3 == 0 or num%5==0:
#     print('num divisible by 3 or 5')
# else:
#     print("num not divisible by 3 or 5")

##3
# num= 30
# if num%3 == 0 and num%7==0:
#     print('fizz buzz')
# elif num%3 == 0:
#     print("fizz")
# elif num%7 == 0:
#     print("buzz")

##4
# word = "ltrs"
# if word[-1]== word[0]:
#     print("true")
# else:
#     print("false")

##5
# place_of_work= "vas"
# town_of_home= "hih"
# time=9
# if time==7:
#     print("at home")
# elif time==8:
#     print("commuting")
# else:
#     print("work")

# #6
# num1= 45
# num2= 48
# if (num1+num2)%2==0:
#     print("its even")
# else:
#     print("odd")

#7

# num=102401
# num=str(num)
# if num[::-1]==num:
#   print("palindrome")
# else:
#     print("not palindrome")

# #8
# strg="fhuidfreilgsrelnoigj".upper()

# def find_last_vowel(letters):
#     for letter in letters[::-1]:
#         vowels= ["a","e","i","o","u"]
#         if letter.lower() in vowels:
#             return f"found {letter}"

# print(find_last_vowel(strg))


# x=(len(num))
# strnum=[]
# for i in range(0,x):
#     strnum[i]= [(f"'{i}'")]
#     print(f"'{i}'") 
# print(strnum)
# if strnum[0]==strnum[-1] and strnum[1]==strnum[-2]:
# # # if strnum[i]==strnum[-i-1]
#     print("palindrome")
# else:
#     print("not palindrome")

# def press():
#     print('grind')
# press()

# def cash_withdrawal(amount,accnum):
#     print("Withdrawing {} from account {}".format(amount,accnum))

# cash_withdrawal(300,50449921)
# cash_withdrawal(30,50449921)
# cash_withdrawal(200,50449921)

# def coffee(size,type):
#     print(f"coffee {size} and {type}")

# coffee("large","latte")

# order_count = 0
# def take_order(topping,size): 
#     global order_count 
#     print("Pizza with {} and {}".format(topping,size))     
#     order_count += 1
# take_order("pineapple",'12in')

# balance=4000
# pin=int(input('pin number'))
# amount=int(input('how much u want'))

# def cashmachine(pin,amount): 
#     global balance
#     if pin==3333:
#         print(f"dispense {amount}") 
#         print(f"new balance is {balance-amount}")      
#     else:
#         print('wrong pin')

# cashmachine(pin, amount)



