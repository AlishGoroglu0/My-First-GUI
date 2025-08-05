from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#character class

class Character:
    def __init__(self, name, age, race, level, health, mana, strength, wisdom, intelligence):
        self.name = name
        self.age = age
        self.race = race
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.wisdom = wisdom
        self.intelligence = intelligence

character_object = Character("", "" , "" ,1 , 100 , 30 , 20 , 10, 10)


print(character_object.strength)

def reset_character():
    
    #Class reset
    character_object.name = ""
    character_object.age = ""
    character_object.race = ""
    character_object.health = 100
    character_object.mana = 30
    character_object.strength = 20
    character_object.wisdom = 10
    character_object.intelligence = 10
    character_object.level = 1

    #Reset widgeds
    Character_race_choose.set("Human")
    Character_class_choose.set("Warrior")
    Character_age.set("Youth")
    
    #INPUT Enabled!
    submit_button.config(state="active") 
    name_entry.config(state="normal")
    Character_class_choose.config(state="active")
    Character_age.config(state="active")
    Character_race_choose.config(state="active")

    status_label.config(text="Restarted")
    Character_show(2)


# Function to handle character submission
def submit_character():
    
    

    #Disables the submit button and input fields to prevent multiple submissions
    submit_button.config(state="disabled") 
    name_entry.config(state="disabled")
    Character_class_choose.config(state="disabled")
    Character_age.config(state="disabled")
    Character_race_choose.config(state="disabled")
    
    
    #Character data!
    name = name_entry.get()
    age = Character_age.get()
    Clas = Character_class_choose.get()
    race = Character_race_choose.get()
    
    #in case Character does not have a name
    if name == "":
        nameless_name_dict = {
            "Human" : "Henry Richword",
            "Elf" : "Litrius Aletria",
            "Dwarf" : "Yogen Monger",
            "Ork" : "Glammar"
        }
        name = nameless_name_dict.get(race)
        print(name)

    #Stat bonus varriables
    add_health = 10
    add_mana = -0
    add_strength = 0
    add_wisdom = 0
    add_intelligence = 0

    #Stat bonuses!
    match age:
        case "Youth":
            add_health += 20
            add_mana += -20
            add_strength += 15
            add_wisdom += -10
            
        case "Young Adult":
            add_health += 70
            add_mana += 25
            add_strength += 15
            add_wisdom += 10
        case "Adult":
            add_health += 25
            add_mana += 5
            add_strength += 60
            add_wisdom += 15
            add_intelligence += 20
        case "Old":
            add_health += -25
            add_mana += 30
            add_strength += -25
            add_wisdom += 35
            add_intelligence += 45
        case _:
            reset_character()
            messagebox.showerror("Invalid Age", "Please don't touch age!")
            return 0
            
    match Clas:
        case "Warrior":
            add_health += 10
            add_strength += 5
        case "Mage":
            add_health += 5
            add_mana += 10
        case "Rogue":
            add_health += 5
            add_strength += 3
        case _:
            reset_character()
            messagebox.showerror("Invalid Class", "Please don't touch class!")
            return 0
    match race:

        case "Human":
            add_health += 5
            add_strength += 2
        case "Elf":
            add_health += 3
            add_mana += 5
            add_intelligence += 2
        case "Dwarf":
            add_health += 7
            add_strength += 3
        case "Orc":
            add_health += 10
            add_strength += 5
        case _:
            reset_character()
            messagebox.showerror("Invalid Race", "Please don't touch Race!")
            return 0

    if character_object.strength < 0:
        character_object.strength = 0
    if character_object.intelligence < 0:
        character_object.intelligence = 0
    if character_object.wisdom < 0:
        character_object.wisdom = 0


    # Update character object
    character_object.name = name
    character_object.age = age
    character_object.race = race
    character_object.strength += add_strength
    character_object.health += add_health
    character_object.mana += add_mana
    character_object.wisdom += add_wisdom
    character_object.intelligence += add_intelligence
    status_label.config(text="Character submitted successfully!")
    Character_show(1)



def Character_show(Is_submitted_OR_LEVEL_UP_OR_RESET=NONE):

    def config():
        Character_name_show.config(text=f"NAME:{character_object.name}")
        Character_age_show.config(text=f"AGE:{character_object.age}")
        Character_race_show.config(text=f"RACE:{character_object.race}")
        Character_health_show.config(text=f"HEALTH:{character_object.health}")
        Character_Level_show.config(text=f"LEVEL:{character_object.level}")
        Character_wisdom_show.config(text=f"WIS:{character_object.wisdom}")
        Character_intelegence_show.config(text=f"INT:{character_object.intelligence}")
        Character_strenght_show.config(text=f"STR:{character_object.strength}")
        Character_mana_show.config(text=f"MANA:{character_object.mana}")

    if Is_submitted_OR_LEVEL_UP_OR_RESET == NONE:
        messagebox.showerror("something Went Wrong!", "Something Went Wrong!")
        return 0
    
    elif Is_submitted_OR_LEVEL_UP_OR_RESET == 1:
        config()
    elif Is_submitted_OR_LEVEL_UP_OR_RESET == 2:
        config()
    elif Is_submitted_OR_LEVEL_UP_OR_RESET == 3:
        config()

def level_up():
    character_object.level += 1
    level_up_val = character_object.level * 0.25
    character_object.health += int(25*level_up_val)
    character_object.wisdom += int(25*level_up_val)
    character_object.intelligence += int(25*level_up_val)
    character_object.mana += int(25*level_up_val)
    character_object.strength += int(25*level_up_val)
    Character_show(3)
window = Tk()
window .title("Character")
window.geometry("600x400")






#Character creation widgets
#Character Name here!
name_label = Label(window, text="Character Name:", font=("Arial", 14))
name_label.place(x=1, y=1)
name_entry = Entry(window, font=("Arial", 14))
name_entry.place(x=150, y=1)



#Character Age here! Young Adult OLD!
Age_label = Label(window, text="Character Age:", font=("Arial", 14))
Age_label.place(x=1, y=30)

Character_age = combobox = ttk.Combobox(window, values=["Youth","Young Adult", "Adult", "Old"])
Character_age.place(x=150, y=30)
Character_age.current(0)  # Set default selection to "Young"

#Character Race Here! Human, Elf, Dwarf, Orc, etc.

Character_race_label = Label(window, text="Character race:", font=("Arial", 14),
                             state="active")
Character_race_label.place(x=1, y=60)

Character_race_choose = ttk.Combobox(window, values=["Human", "Elf", "Dwarf", "Orc"])
Character_race_choose.current(0)  # Set default selection to "Human"
Character_race_choose.place(x=150, y=60)


#Character Class Here! Warrior, Mage, Rogue, etc.
Character_class_label = Label(window, text="Character Class:", font=("Arial", 14))
Character_class_label.place(x=1, y=90)

Character_class_choose = ttk.Combobox(window, values=["Warrior", "Mage", "Rogue"],
                                      state="active")
Character_class_choose.current(0)  # Set default selection to "Warrior"
Character_class_choose.place(x=150, y=90)

#Character restart button
character_reset_button = Button(window, text="Reset Character", font=("Arial", 14),
                                command=reset_character,activebackground="Crimson"
                                ,bd=3 , relief="raised")
character_reset_button.place(x=1, y=120)

submit_button = Button(window, text="Submit Character", font=("Arial", 13) , command=submit_character,
                       activebackground="Light Green" , bd=3 , relief="raised")
submit_button.place(x=161, y=120)

#level up button

level_up_button = Button(window, text="Level Up Character", font=("Arial", 14),
                         activebackground="Light blue",bd=3 , relief="raised", 
                         command=level_up)
level_up_button.place(x=1, y=160)

#Status label
status_label = Label(window, text="Waiting!", font=("Arial", 14))
status_label.place(x=1, y=360)


 # Character info here!
Character_name_show = Label(text=f"NAME:{character_object.name}")
Character_age_show = Label(text=f"AGE:{character_object.age}")
Character_race_show = Label(text=f"RACE:{character_object.race}")
Character_Level_show = Label(text=f"LEVEL:{character_object.level}")
Character_intelegence_show = Label(text=f"INT:{character_object.intelligence}")
Character_wisdom_show = Label(text=f"WIS:{character_object.wisdom}")
Character_strenght_show = Label(text=f"STR:{character_object.strength}")
Character_health_show = Label(text=f"HEALTH:{character_object.health}")
Character_mana_show = Label(text=f"MANA:{character_object.mana}")

Character_name_show.place(x=400 , y=1)
Character_age_show.place(x=400 , y=20)
Character_race_show.place(x=400 , y=40)
Character_Level_show.place(x=400 , y=60)
Character_intelegence_show.place(x=400 , y=80)
Character_wisdom_show.place(x=400 , y=100)
Character_strenght_show.place(x=400 , y=120)
Character_health_show.place(x=400 , y=140)
Character_mana_show.place(x=400 , y=160)

#exit button

exit_button = Button(window, text="EXIT", font=("Arial", 20),
                         activebackground="RED",bd=3 , relief="raised", 
                         command=lambda: window.destroy())
exit_button.place(x=200, y=160)






window.mainloop()