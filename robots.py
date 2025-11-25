#printing and updating variables
space = " "
robots = 0


print("Unknown: *SMACK* *SMACK* WAKE UP.")
print(space)
print("Unknown: Hey don't hit our new guest.")
print(space)
print("Unknown: Welcome to The Trailer Park.")
print(space)

#Introduction
print("Allow me to introduce myself, I'm Rocelyn, the overseer of this here park")
print(space)
print("Rocelyn: Whats your name?")
print(space)
player = input()
print(space)
print(player,": My name is", player)
print(space)
print(f"Rocelyn: Mmmmm, {player}, How lovely.")
print(space)
print("Unknown: That'll look good on your gravestone.")
print(space)
print("Rocelyn: Excuse him that'll be my partner, Gerald.")
print(space)
print(player,": What's going on? Im chained up and my whole body hurts!")
print(space)
print("Gerald: Typical, Another vagrant that lost their memories. Just my luck.")
print(space)
print("Gerald: Long story short you're our slave.")
print(space)

#Objective of the game
print("Rocelyn: What he means is you arrived here work in our factory. And You're tied up since you just arrived from Central.")
print(space)
print("Rocelyn: Here at The Trailer Park we are building the future! One mechanoid at a time! ")
print(space)
print(player,": Mechaniod? you mean like ... robots.")
print(space)
print("Gerald: *SMACK* We mean Mechanoids! Dont say that vile term again unless you want more!")
print(space)
print("Rocelyn: Your task is to collect gears. Every gear goes to making mechanoids. We will touch on that when the time comes but for now lets untie those chains.")
print(space)
print("Rocelyn: Thats must feel nice.")
print(space)
print("Rocelyn: Lets take you to the factory.")
print(space)

#add a narrator that ask questions to the player to decide movement such as a path game (bandersnatch style)
simple_question = "yes or no?"
print(f"Narrotor: Do you wish to go with Rocelyn to the factory?", simple_question) 
print(space)
answer_000 = input()
if answer_000 == "yes":
    print(space)
    print("You have arrived at the factory" + " " + "day: 1")
else:
    print(space)
    print("Rocelyn: Have you decided to run away. I wouldn't recommed that.")
day = 1

print(space)
print("Rocelyn: Welcome to the factory. Your task is simple. Stand here and collect gears")
print(space)
print("Rocelyn: When the day ends you'll be able to exchange your gears in for NFTs. NFTS can be exchanged for your necessities.")
print(space)
print("Rocelyn: Are you ready to begin?", simple_question)
print(space)
answer_001 = input()
if answer_001 == "yes":
    print(space)
    print("Rocelyn: Great, lets start")
else:
    print(space)
    print("Rocelyn: Oh do you need time to get ready... TOO BAD! *SLAP* Get to work!")
print(space)
print("Narrator: Now begins the game you'll be prompted to collect the gears. Collect all the gears and the workday will end.")
print(space)
print("Do you wish to gather gears. type: collect_gear ")
print(space)

actions = 10
gears = 0
while actions > 0:
        answer = input()
        if answer == "collect_gear":
            gears += 1
            print(space)
            print("You have collected Gears:", gears)
            print(space)
            actions -= 1
            print("collect another?")
        else:
            print("Try again, check your spelling")
        if actions == 0:
            print("Narrator: You have used all your actions of the day")
            print(space)
            print("Narrator: Return home and sleep to refresh your actions avaliable.")
if actions == 0:
    print(space)
    print("Go home and sleep?")
    answer = input()
    if answer == "yes":
        print(space)
        print("you have slept well.")
        actions += 10
    else:
        print("you have died of exhaustion")


