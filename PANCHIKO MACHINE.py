import random
print("Welcome to Panchiko Machine")    
winning_number=random.randint(1,100) # lets a random number from a range from 1 to 100
guess_number=int(input("Enter your guess:"))
print("guess number",guess_number)
while guess_number != winning_number:
    if guess_number > winning_number:
        print("TOO HIGH")
    else:
        print("TOO LOW")
    guess_number = int(input("Try again: "))
    
if(guess_number==winning_number):
   result="YOU WIN"
elif(guess_number>winning_number):
   result="TOO HIGH"

elif(guess_number<winning_number):
    result="TOO LOW"
print("the winning number is",winning_number)
print("the result is",result)
