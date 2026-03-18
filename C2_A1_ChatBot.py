import re,random
from colorama import Fore,init

init(autoreset=True)
destinations = {
    "Beaches":["Bali","Malidives","Phuket"],
    "Mountains":["Swiss Aplps","Himalaye","Rockey Mountains"],
    "Cities":["Tokyo","Paris","New York"]
}

programming_languages = {
    "Web development":["HTML","CSS","JS"],
    "App development":["JAVA","REAT"],
    "AI development":["Python"]
}

def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
def recommend():
    print(Fore.CYAN+"travel bot: beaches , mountains or cities?")
    choice = input(Fore.YELLOW+"You: ")
    choice = normalize_input(choice)
    if choice in destinations:
        suggetion = random.choice(destinations[{choice}])
        print(Fore.CYAN+f"Tavelbot: How about {suggetion}")
        print(Fore.GREEN+"Tavelbot: Do you like it ? (Yes , No)")
        answerte = input(Fore.YELLOW+"You: ").lower()
        if answerte == "yes":
            print(Fore.CYAN+f"Tavelbot: Awesome Enjoy {suggetion}")
        elif answerte == "no":
            print(Fore.RED+"Tavelbot: Lets try another")
            recommend()
        else:
            print(Fore.RED+"Travelbot: Ill suggest you again")
            recommend()

    else:
        print(Fore.RED+"Tavelbot: Sorry i dont have that type of a destination")

            
