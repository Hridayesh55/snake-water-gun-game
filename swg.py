import random
print("snake water gun")
print("note:\nyou will get a total of 5 chances and enter your input as\ns for snake\nw for water\ng for gun")
lst1 = ["s", "w", "g"]
# this will give name to computer (name to our opposition)
bot1=["FARHAN","MOHAN","ROHIT","KARTIK"]
r=random.choice(bot1)
a=1
pp=0
bp=0
chance=6
while(a<=5):
    player=input('enter your choice : ')
    bot=random.choice(lst1)
    if player==bot:
        print("tie")
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    elif player=="s" and bot=="w":
        pp=pp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    elif player=="g" and bot=="s":
        pp=pp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your  {pp} {r}'s point {bp}")
    elif player=="w" and bot=="g":
        pp=pp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    elif player=="s" and bot=="g":
        bp=bp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    elif player == "g" and bot == "w":
        bp=bp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    elif player == "w" and bot == "s":
        bp=bp+1
        print(f"your input {player} {r}'s input {bot}")
        print(f"your point {pp} {r}'s point {bp}")
    else:
        print("invalid input")
    a=a+1
    chance=chance-1
    print(chance-1," chance left")
print(f"your total points are :{pp}\n{r}'s total points are :{bp}")
if pp>bp:
    print("victory")
if bp>pp:
    print("defeat")
elif pp==bp:
    print("draw")

