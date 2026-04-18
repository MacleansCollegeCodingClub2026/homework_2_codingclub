#adventure!!
print("You are exploring a rainforest for a rumored treasure.")
print("Legend has it that there are some buried on a nearby island.")
#introduction

#first choice

print("You come across a lake!")
choice1 = input("Do you swim across, or wait for a boat? Enter 'swim' or 'wait'")
if choice1 == "swim":
    print("You are eaten by a shark. Game over. ")
elif choice1 == "wait":
    print("A boat arrives and you arrive at the island safely. ")
else:
    print("What. Game over.")
#second choice

choice2 = input("You come to a cavern, do you venture inside or walk away? Enter 'venture' or 'walk'")
if choice2 == "venture":
    print("You get squished by a boulder and you are never seen again. Game over.")
elif choice2 == "walk":
    print("You walk around the cavern and find yourself at a crossroads.")
else:
    print("What are you doing? Game over.")
#third choice

choice3 = input("Do you go left, right, or straight? Enter 'left', 'right', or 'straight': ")
if choice3 == "left":
    print("You are trampled by a herd of wildebeast. Game over.")
elif choice3 == "right":
    print("You march on and find the hidden treasure. Yippeee!!")
elif choice3 == "straight":
    print("You are stung by a poisonous wasp. Game over.")
else:
    print("...why? Game over.")
#end