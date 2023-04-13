import random

douglas_adams = ["The Ultimate Answer to Life, The Universe and Everything is...42!", "And wow! Hey! What’s this thing suddenly coming towards me very fast? Very very fast. So big and flat and round, it needs a big wide sounding name like … ow … ound … round … ground! That’s it! That’s a good name – ground!", "I always thought something was fundamentally wrong with the universe.", "DON'T PANIC!", "Curiously enough, the only thing that went through the mind of the bowl of petunias as it fell was Oh no, not again. Many people have speculated that if we knew exactly why the bowl of petunias had thought that we would know a lot more about the nature of the Universe than we do now." ]
num = random.randint(1, 99)
print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!''')
tries = 0
while (True):
    tries += 1
    ans = input("What's your guess between 1 and 99?\n")
    if (ans.lower() == "exit"):
        print("Ok, loser, see ya...")
        break
    try:
        ans = int(ans)
    except:
        print("That is not a number!")
    else:
        if (ans < 1 or ans > 99):
         print("Your guess is out of the range!")
        else:
         if ans == num:
            if ans == 42:
                print(f"Wow! The answer was 42... Here is some wisdom for you:\n{random.choice(douglas_adams)}")
            if tries == 1:
                print("Lucky guess! You got oon the first try! Nice job!");
            else:
                print(f"Ok, you got it in {tries} tries, goodbye!")
            break
         elif ans < num:
             print("Too low...")
         else:
             print("Too high...")

