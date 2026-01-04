'''
API (application Programming Interface): It's a way where both/many programs can
    interact/communicate with each other
    EG: Google Maps in Swiggy

Roles in API: me order food in a restaurent. So you send a request via API, then server sends the response
client: you/me
API: Waitor
API: Chef
Server: Restaurent

Your Program(swiggy) → API Request(maps) → Server(google maps)
Server → API Response(map data) → Your Program(delivery partner location in swiggy)

Types of APIs:
	•	Web APIs (most common)
	•	REST APIs (JSON-based)
	•	SOAP (older)
	•	Internal APIs

'''

import requests

#It's a base url
base_url = "https://pokeapi.co/api/v2"

def get_pokemon(name):
    #we prepare url based on pokemon type
    url = f"{base_url}/pokemon/{name}"

    #if client request is good, we store the response
    response = requests.get(url)

    #200 means response successful
    if response.status_code == 200:
        pokemon_info = response.json()
        return pokemon_info
    else:
        print(f"The information cannot be retrieved: {response.status_code}")    

pokemon_name = input("Enter the pokemon name: ")
pokemon_data = get_pokemon(pokemon_name)

if pokemon_data: # it will be true if there is data
    print(f"Name: {pokemon_data["name"]}")
    print(f"ID: {pokemon_data["id"]}")
    print(f"Weight: {pokemon_data["weight"]}")
    print(f"Height: {pokemon_data["height"]}")
    
else:
    print("No data found")