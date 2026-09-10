program_name = "    Welcome to Love calculator    "
print("="*len(program_name))
print(program_name)
print("="*len(program_name))
print()
user_name = input("Enter your name : ")
other_person_name = input("Enter your person name : ")
#TRUE LOVE
user_name.lower()
other_person_name.lower()
T = user_name.count("t")+other_person_name.count("t")
R = user_name.count("r")+other_person_name.count("r")
U = user_name.count("u")+other_person_name.count("u")
E = user_name.count("e")+other_person_name.count("e")

L = user_name.count("l")+other_person_name.count("l")
O = user_name.count("o")+other_person_name.count("o")
V = user_name.count("v")+other_person_name.count("v")
E = user_name.count("e")+other_person_name.count("e")

TRUE = T+R+U+E
LOVE = L+O+V+E

love_percent = int(str(TRUE)+str(LOVE))
if love_percent <10 or love_percent >90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent >= 40 and love_percent <=50:
    print(f"Your score is {love_percent}, you are alright together")
else:
    print(f"Your score : {love_percent}")