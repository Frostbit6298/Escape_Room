# txt.adventure game V3 -- 12/7/20 to 12/10/20
# By Frostbit#6298 - ( Discord Account )
# Introduction Code / Imports
from Game2ElectricBoogaloo.Endings import extract_end, silenced_end, out_of_reach_end, obedient_end, retarded_end, \
    truck_end, crowded_room_end, crowded_room_end_2, oops_lost_my_eye, syringe_poke, someone_else_end, ghost_busters, \
    sewer_squad, Villain_End, battle_to_le_ded, export2, viva_la_revolution_female, viva_la_revolution_male, \
    monster_scare, monster
from random import randint

print("Welcome to \'Escape_Room\'.")
username = input("What is your username? ")


# Functions - Main Code

# (Utility Code)


def clear():
    return "\n \n" * 50


# (Male Companion Paths)


def first_kill_male():
    print(clear())
    rev_choice4 = input('''You both opened the door to find one of the abductors in the middle of a surgery.
        Once he noticed you two, he frantically looked around for an escape..
        You both charged at him before he could find a weapon, and you slit his throat after tackling him.
        Your companion smiled insanely as they watched you retract the blood soaked scalpel from his neck.
        You both leave the room and are back in the hallway, where do you go?

        1] Right, The crossroads
        2] Left, keep going down the corridor\n\n > ''')
    if rev_choice4.lower() == "1":
        return male_comp_crossroads()
    elif rev_choice4.lower() == "2":
        print(clear())
        print(monster())
        return startup()
    else:
        print("Invalid Input")
        return first_kill_male()


def hide_corpse_male():
    print("\n" * 5)
    corpses = input('''You hide the bodies in your room.
         What do you do? 

         1] Feast upon their flesh
         2] Go to the crossroads\n\n > ''')
    if corpses.lower() == "1":
        print("Twas a joke, pick #2")
        return hide_corpse_male()
    elif corpses.lower() == "2":
        return male_comp_crossroads()
    else:
        print("Invalid Input")
        return hide_corpse_male()


def fast_kill_male():
    print("\n" * 5)
    rev_choice7 = input('''You both run towards the men and drive your weapons into their necks while they're still surprised.
         There is no point in hiding the bodies, their blood is in the middle of the corridor.
         What do you do?

         1] Feast on their flesh
         2] Go to the crossroads\n\n > ''')
    if rev_choice7.lower() == "1":
        print("That was a joke, choose #2")
        return fast_kill_male()
    elif rev_choice7.lower() == "2":
        return male_comp_crossroads()
    else:
        print("Invalid Input")
        return fast_kill_male()


def cool_kill_male():
    print(clear())
    rev_choice6 = input('''You both silently decided to kill them once they entered a room.
         You synced your footsteps with theirs to avoid detection.
         Once  they entered your room they looked inside to see if you were still there.
         As they started to leave, you both picked one and slashed their throats.
         Their blood filled their lungs and they suffocated while bleeding out.
         What do you do?

         1] Hide the bodies
         2] Go back to the crossroads\n\n > ''')
    if rev_choice6.lower() == "1":
        return hide_corpse_male()
    elif rev_choice6.lower() == "2":
        return male_comp_crossroads()
    else:
        print("Invalid Input")
        return cool_kill_male()


def encounter_male():
    print(clear())
    rev_choice5 = input('''As you both walked down the corridors leading back to your room you encountered two men.
              They were walking towards your room so it's likely they'll find you're gone.
              You must kill them.

              1] Kill them
              2] Kill them but stealthily for no reason\n\n > ''')
    if rev_choice5.lower() == "1":
        return fast_kill_male()
    elif rev_choice5.lower() == "2":
        return cool_kill_male()
    else:
        print("Invalid Input")
        return encounter_male()


def male_comp_path2():
    print(clear())
    rev_choice3 = input('''You and your companion head outside the room.
              You are presented with similar choices to earlier, what do you do?

              1] Right, Keep going down the hallway
              2] Left, Go back to the cross roads
              3] Forward, go into the unexplored room\n\n > ''')
    if rev_choice3.lower() == "1":
        print(clear())
        print(monster())
        return startup()
    elif rev_choice3.lower() == "2":
        return male_comp_crossroads()
    elif rev_choice3.lower() == "3":
        return first_kill_male()
    else:
        print("Invalid Input")
        return male_comp_path2()


def male_comp_crossroads():
    print(clear())
    rev_choice2 = input('''You and your companion head back to the cross roads, luckily they remembered to take the saw with them.
             Before you both lay three paths, where do you go?

             1] Left, the \"EXPORT\" doors
             2] Forward, you haven't went there before.
             3] Right, back to where you woke up.\n\n > ''')
    if rev_choice2.lower() == "1":
        print(clear())
        print(export2())
        return startup()
    elif rev_choice2.lower() == "2":
        print(clear())
        print(viva_la_revolution_male())
        return startup()
    elif rev_choice2.lower() == "3":
        return encounter_male()
    else:
        print("Invalid Input")
        return male_comp_crossroads()


def male_companion():
    print(clear())
    rev_choice1 = input('''Whenever you took the white cloth off of the body, you found an unconscious man in a hospital gown.
          You were able to wake him up by slapping him a few times.After they woke up they were disoriented and confused.
          You explained to them where they were, what's going to happen, and who you are.
          You both decided to fight together against the organization which took you, but first, you have to free them.
          You were able to take the other cuff off of the bed frame but they were still wearing the cuffs.
          Now you both needed to choose where to go next.
          
          1] The previous cross roads
          2] The hallway you were just in\n\n > ''')
    if rev_choice1.lower() == "1":
        return male_comp_crossroads()
    elif rev_choice1.lower() == "2":
        return male_comp_path2()
    else:
        print("Invalid Input")
        return male_companion()


# (Female Companion Paths)


def first_kill_female():
    print(clear())
    rev0_choice4 = input('''You both opened the door to find one of the abductors in the middle of a surgery.
    Once he noticed you two, he frantically looked around for an escape..
    You both charged at him before he could find a weapon, and you slit his throat after tackling him.
    Your companion gagged as they watched you retract the blood soaked scalpel from his neck.
    You both leave the room and are back in the hallway, where do you go?
    
    1] Right, The crossroads
    2] Left, keep going down the corridor\n\n > ''')
    if rev0_choice4.lower() == "1":
        return fem_comp_crossroads()
    elif rev0_choice4.lower() == "2":
        print(clear())
        print(monster_scare())
        return startup()
    else:
        print("Invalid Input")
        return first_kill_female()


def hide_corpse_female():
    print("\n" * 5)
    corpses = input('''You hide the bodies in your room.
     What do you do? 
     
     1] Feast upon their flesh
     2] Go to the crossroads\n\n > ''')
    if corpses.lower() == "1":
        print("Twas a joke, pick #2")
        return hide_corpse_female()
    elif corpses.lower() == "2":
        return fem_comp_crossroads()
    else:
        print("Invalid Input")
        return hide_corpse_female()


def cool_kill_fem():
    print(clear())
    rev0_choice6 = input('''You both silently decided to kill them once they entered a room.
     You synced your footsteps with theirs to avoid detection.
     Once  they entered your room they looked inside to see if you were still there.
     As they started to leave, you both picked one and slashed their throats.
     Their blood filled their lungs and they suffocated while bleeding out.
     What do you do?
     
     1] Hide the bodies
     2] Go back to the crossroads\n\n > ''')
    if rev0_choice6.lower() == "1":
        return hide_corpse_female()
    elif rev0_choice6.lower() == "2":
        return fem_comp_crossroads()
    else:
        print("Invalid Input")
        return cool_kill_fem()


def fast_kill_fem():
    print("\n" * 5)
    rev0_choice7 = input('''You both run towards the men and drive your weapons into their necks while they're still surprised.
     There is no point in hiding the bodies, their blood is in the middle of the corridor.
     What do you do?
     
     1] Feast on their flesh
     2] Go to the crossroads\n\n > ''')
    if rev0_choice7.lower() == "1":
        print("That was a joke, choose #2")
        return fast_kill_fem()
    elif rev0_choice7.lower() == "2":
        return fem_comp_crossroads()
    else:
        print("Invalid Input")
        return fast_kill_fem()


def encounter_female():
    print(clear())
    rev0_choice5 = input('''As you both walked down the corridors leading back to your room you encountered two men.
          They were walking towards your room so it's likely they'll find you're gone.
          You must kill them.
          
          1] Kill them
          2] Kill them but stealthily for no reason\n\n > ''')
    if rev0_choice5.lower() == "1":
        return fast_kill_fem()
    elif rev0_choice5.lower() == "2":
        return cool_kill_fem()
    else:
        print("Invalid Input")
        return encounter_female()


def fem_comp_path2():
    print(clear())
    rev0_choice3 = input('''You and your companion head outside the room.
          You are presented with similar choices to earlier, what do you do?
          
          1] Right, Keep going down the hallway
          2] Left, Go back to the cross roads
          3] Forward, go into the unexplored room\n\n > ''')
    if rev0_choice3.lower() == "1":
        print(clear())
        print(monster_scare())
        return startup()
    elif rev0_choice3.lower() == "2":
        return fem_comp_crossroads()
    elif rev0_choice3.lower() == "3":
        return first_kill_female()
    else:
        print("Invalid Input")
        return fem_comp_path2()


def fem_comp_crossroads():
    print(clear())
    rev0_choice2 = input('''You and your companion head back to the cross roads, luckily they remembered to take the saw with them.
          Before you both lay three paths, where do you go?
          
          1] Left, the \"EXPORT\" doors
          2] Forward, you haven't went there before.
          3] Right, back to where you woke up.\n\n > ''')
    if rev0_choice2.lower() == "1":
        print(clear())
        print(export2())
        return startup()
    elif rev0_choice2.lower() == "2":
        print(clear())
        print(viva_la_revolution_female())
        return startup()
    elif rev0_choice2.lower() == "3":
        return encounter_female()
    else:
        print("Invalid Input")
        return fem_comp_crossroads()


def female_companion():
    print(clear())
    rev0_choice1 = input('''Whenever you took the white cloth off of the body, you found an unconscious woman in a hospital gown.
              You were able to wake her up by slapping her a few times. After they woke up they were disoriented and confused.
              You explained to them where they were, what's going to happen, and who you are.
              You both decided to fight together against the organization which took you, but first, you have to free them.
              You were able to take the other cuff off of the bed frame but they were still wearing the cuffs.
              Now you both needed to choose where to go next.

              1] The previous cross roads
              2] The hallway you were just in\n\n > ''')
    if rev0_choice1.lower() == "1":
        return fem_comp_crossroads()
    elif rev0_choice1.lower() == "2":
        return fem_comp_path2()
    else:
        print("Invalid Input")
        return female_companion()


# (Solo Paths)


def recruitment():
    print(clear())
    join = input('''You opened the door on the left to find a man in the middle of a surgery.
    He was cutting open the skin of someone, who looked recently deceased, with a scalpel.
    He didn't notice you up until you started to close the door, when which he immediately turned towards you.
    After he saw you, he stopped the procedure and dashed to the door. You brandished the saw and he stopped his approach.
    After he considered his options, he asked,\"How about you join us? This is a very lucrative business.\"
    
    1] \"yes\"
    2] \"No\" \n\n > ''')
    if join.lower() == "1":
        print(clear())
        Villain_End()
        return startup()
    elif join.lower() == "2":
        print(clear())
        battle_to_le_ded()
        return startup()
    else:
        print("Invalid Input")
        return recruitment()


def path2_2():
    print(clear())
    choice6 = input('''You decided to go on the left path, after you walked down the hallway for a while,
        you stumbled upon two parallel doors. Which route will you take?

        1] left door
        2] right door
        3] ignore both doors and keep walking\n \n> ''')
    if choice6.lower() == "1":
        print(clear())
        print(recruitment())
        return startup()
    elif choice6.lower() == "2":
        return revolution_begins()
    elif choice6.lower() == "3":
        number = randint(1, 4)
        if str(number) == "1":
            print(clear())
            ghost_busters()
            return startup()
        elif str(number) == ('2', '3', '4'):
            print(clear())
            sewer_squad()
            return startup()
        else:
            print(clear())
            sewer_squad()
            return startup()
    elif choice6.lower() == "4":
        print(clear())
        print(syringe_poke())
        return startup()
    else:
        print("Invalid Input")
        return path2_2()


def revolution_begins():
    print(clear())
    choice5 = input('''You open the right door to see a room identical to the one you woke up in.
    In the room, you see an unconscious person chained to an iron bed frame like you were. They are covered by a white cloth.
    Do you wish to see who they are and free them? 
    
    1] take off the white cloth, wake them up, and free them
    2] leave them there
    3] kill them\n \n > ''')
    if choice5.lower() == "1":
        number = randint(1, 2)
        if str(number) == "1":
            male_companion()
        elif str(number) == "2":
            female_companion()
        else:
            female_companion()
    elif choice5.lower() == "2":
        return path2()
    elif choice5.lower() == "3":
        print(clear())
        print(someone_else_end())
        return startup()
    else:
        print("Invalid Input")
        return revolution_begins()


def path2():
    print(clear())
    choice4 = input('''You decided to go on the left path, after you walked down the hallway for a while,
    you stumbled upon two parallel doors. Which route will you take?
    
    1] left door
    2] right door
    3] ignore both doors and keep walking\n \n> ''')
    if choice4.lower() == "1":
        print(clear())
        print(oops_lost_my_eye())
        return startup()
    elif choice4.lower() == "2":
        return revolution_begins()
    elif choice4.lower() == "3":
        number = randint(1, 4)
        if str(number) == "1":
            print(clear())
            ghost_busters()
            return startup()
        elif str(number) == ('2', '3', '4'):
            print(clear())
            sewer_squad()
            return startup()
        else:
            print(clear())
            sewer_squad()
            return startup()
    elif choice4.lower() == "4":
        print(clear())
        print(syringe_poke())
        return startup()
    else:
        print("Invalid Input")
        return path2()


def dress_wound_2():
    choice3 = input('''\n\n\n\n\nYou rationally decided to dress the wound before any further actions. After evaluating your choices, you decided
       to leave the room. You came upon a cross road after walking for a few minutes. What do you do?

       1] go left
       2] go through the doors with an \"EXPORT\" sign
       3] go right \n \n > ''')
    if choice3.lower() == "1":
        return path2()
    elif choice3.lower() == "2":
        print(clear())
        print(truck_end())
        return startup()
    elif choice3.lower() == "3":
        print(clear())
        print(crowded_room_end_2())
        return startup()
    else:
        print("Invalid Input")
        return dress_wound_2()


def secret_path():
    print(clear())
    print('''In a moment of realization, you realized you could take the saw with you for future use.
    You decided to take it with you for your future endeavors.''')
    return dress_wound_2()


def dress_wound():
    print(clear())
    choice2 = input('''You rationally decided to dress the wound before any further actions. After evaluating your choices, you decided
    to leave the room. You came upon a cross road after walking for a few minutes. What do you do?

    1] go left
    2] go through the doors with an \"EXPORT\" sign
    3] go right \n \n > ''')
    if choice2.lower() == "1":
        return path2()
    elif choice2.lower() == "2":
        print(clear())
        print(truck_end())
        return startup()
    elif choice2.lower() == "3":
        print(clear())
        print(crowded_room_end())
        return startup()
    elif choice2.lower() == "4":
        return secret_path()
    else:
        print("Invalid Input")
        return dress_wound()


def hand_one():
    print(clear())
    choice1 = input('''You hesitantly picked up the saw and began your work.
     Luckily, the flesh and bone cut away with shocking ease, and as you suspected you were on anesthesia.
     Now you were free, and. . . bleeding torrents of blood. You would have to do something about that soon.
     On the nearby table is a variety of medicinal supplies, maybe you can find something to help.
     What do you do?
     
     1] Leave Immediately
     2] Sit and wait for assistance
     3] Look on the table for supplies to dress the wound
     4] Cut off a leg too\n \n > ''')
    if choice1.lower() == "1":
        print(clear())
        print(out_of_reach_end())
        return startup()
    elif choice1.lower() == "2":
        print(clear())
        print(obedient_end())
        return startup()
    elif choice1.lower() == "3":
        return dress_wound()
    elif choice1.lower() == "4":
        print(clear())
        print(retarded_end())
        return startup()
    else:
        print("Invalid Input")
        return hand_one()


# Startup Functions


def opening():
    print(clear())
    print('''You're driving down a dark, desolate road. The winding path seemed to extend endlessly,
    and you grew weary as you drove for hours ; however, despite the long journey the end was in sight.
    as you turned onto an unpaved road, a deer lunged in front of the car. Causing you to swerve and crash.
    Everything was dark, some distorted sounds and glimpses of images come to mind as you slept.\n \n \n''')
    opening_choice = input('''As you awake, a blinding white light greets you.
     As your eyes adjust, you notice you\'re inside a room with smooth, gray walls.
     You're shackled to an iron bed frame, and within the room is a table with assorted items upon it.
     Aside you lays a saw, and it appears that you're on anesthesia based off how you feel. What do you do:
     
     1] Cut off the shackled hand
     2] Don't do anything
     3] Scream for help\n \n > ''')
    if opening_choice.lower() == "1":
        return hand_one()
    elif opening_choice.lower() == "2":
        print(clear())
        print(extract_end())
        return startup()
    elif opening_choice.lower() == "3":
        print(clear())
        print(silenced_end())
        return startup()
    else:
        print("Invalid Input")
        return opening()


def info():
    print(clear())
    print("This is a text based adventure game, you will read a story then choose from a list of options.\n"
          "The options will be numbered, simply choose which one to do. There are many endings, have fun."
          " ( There are some secrets too! )\n \n \n")
    return startup()


# -- Startup Code --

def startup():
    open = input("\n\n\n\n\nWhat do you wish to do?\n 1] play\n 2] read info\n 3] quit\n \n > ")
    if open.lower() == "1":
        return opening()
    elif open.lower() == "2":
        return info()
    elif open.lower() == "3":
        return "\n \nToo bad."


print(startup())

# Contributor - stewing_crisis#3464 ( Discord Account ) : Helped write path2() and some more
