import requests
from colorama import Fore, Back, Style, init
init(autoreset = True)

def lineDraw():
    print(Style.BRIGHT + Fore.RED + "--" * 70)

def displayPokemon(pokemon): # Pokemon is of type dictionary
    lineDraw()
    # Abilities
    print(Style.BRIGHT + Fore.RED  + "\nABILITIES SECTION\n")
    for index, item in enumerate(pokemon['abilities']):
        print(Fore.BLUE + f'Ability number {index+1}')
        sub_ability = item['ability']
        print(f"Name = {sub_ability['name']}\nURL = {sub_ability['url']}")
        print(f"Hidden = {item['is_hidden']}\nSlot = {item['slot']}")
        print()


    lineDraw()
    # Forms
    print(Style.BRIGHT + Fore.RED  + "FORMS SECTION")
    for index, item in enumerate(pokemon['forms']):
        print(f'Form no. {index+1}')
        print(f"Name = {item['name']}\nURL = {item['url']}")
        print()


    lineDraw()
    #Game indices
    print(Style.BRIGHT + Fore.RED   + "LIST OF GAME INDICES\n")
    for index, item in enumerate(pokemon['game_indices']):
        sub_version = item['version'] # Here sub_version is dictionary which is a value for the key 'version' of the dict item
        print(f"Game Index = {item['game_index']}")
        print(f"Version Name = {sub_version['name']}\nVersion URL = {sub_version['url']}")
        print()


    lineDraw()
    # Held Items
    print(Style.BRIGHT + Fore.RED  + "HELD ITEMS\n")
    for index, item in enumerate(pokemon['held_items']):
        print(Fore.BLUE + f"Held Item No. {index + 1}")
        print(f"Name = {item['item']['name']}\nURL = {item['item']['url']}")
        print(f"Version Details: \n")
        for subindex, subitem in enumerate(item['version_details']):
            print(Fore.MAGENTA + f"Sub-list of version detail no. {subindex+1}")
            print(f"Version Rarity = {subitem['rarity']}\nVersion Name = {subitem['version']['name']}\nVersion URL = {subitem['version']['url']}")
            print()
        print()


    lineDraw()
    # Moves
    print(Style.BRIGHT + Fore.RED  + "MOVES\n")
    for index, item in enumerate(pokemon['moves']):
        print(Fore.BLUE + f"Move no. {index+1}")
        print(f"Move = {item['move']['name']}\nMOVE URL = {item['move']['url']}\n")
        for subindex, subitem in enumerate(item['version_group_details']):
            print(Fore.MAGENTA + f"Sub-list of Moves(Move no {index+1}) Details no {subindex+1}")
            print(f"Level Learnt = {subitem['level_learned_at']}")
            print(f"Move Learn Method = {subitem['move_learn_method']['name']}\nMove URL = {subitem['move_learn_method']['url']}")
            print(f"Version Group Name = {subitem['version_group']['name']}\nVersion Group URL = {subitem['version_group']['url']}")
            print()
        print()


    lineDraw()
    # Species
    print(Style.BRIGHT + Fore.RED  + "SPECIES")
    speciesURL = requests.get(pokemon['species']['url'])
    speciesURL = speciesURL.json()
    print(f"Name = {pokemon['species']['name']}\nURL = {pokemon['species']['url']}\nBase Happiness = {speciesURL['base_happiness']}\nCapture Rate = {speciesURL['capture_rate']}")
    print()


def pokemonAPI():
    while True:
        #Asking User Input
        pokemonName = input(Style.BRIGHT + Fore.RED + "\nENTER POKEMON CHARACTER NAME: ")
        # Fetching api request
        req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName.lower()}')

        if req.status_code == 200:
            pokemon = req.json() # pokemon is now of type dictionary
            displayPokemon(pokemon)
            ans = input(Style.BRIGHT + Fore.CYAN + "DO YOU WANT TO EXIT? (y/n): ")
            if ans.lower() == 'y':
                break
            else:
                print()
                continue
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid Pokemon Character")
            continue

print(Style.BRIGHT + Fore.GREEN + "\nWELCOME TO POKEMON API CHARACTER INFORMATION GENERATOR\n")
pokemonAPI()