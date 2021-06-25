import requests as req
import json

url = "https://pokeapi.co/api/v2/pokemon/"
image_url = "https://pokeres.bastionbot.org/images/pokemon/"

# Will contain the ultimate PokeDex
pokemons = {}

# There are moe than 890 Pokemons
# But for some reason I didn't find images for all above 890
# So, I have excluded them

# Also sending 890 get requests didn't get my IP blocked by pokeapi
# Even then, if you don't want to take any risks
# Use scrapy, make multiple crawlers and scrape in parts

for i in range(890):
    
    # Get the raw response and convert it to json
    poke_data = (req.get(url + str(i+1))).json()
    
    # Holds data for current pokemon
    poke = {}
    
    poke['id'] = poke_data['id']
    poke['name'] = poke_data['name']
    poke['height'] = poke_data['height']
    poke['weight'] = poke_data['weight']
    poke['xp'] = poke_data['base_experience']
    poke['image_url'] = image_url + str(i+1) + ".png"
    
    # Holds list of abilities for current pokemon
    # [ { 'name' : 'ability_name', 'is_hidden' : True/False } ]
    abilities = []
    
    total_abilities = len(poke_data['abilities'])
    for a in range(total_abilities):

        # Holds data for current ability
        # { 'name' : 'ability_name', 'is_hidden' : True/False }
        ab = {}
        ability = poke_data['abilities'][a]
        ab['name'] = ability['ability']['name']
        ab['is_hidden'] = ability['is_hidden']
        abilities.append(ab)
    
    poke['abilities'] = abilities

    # Holds list of stats for current pokemon
    # [ { 'name' : 'stat_name', 'base_stat' : stat_value } ]
    stats = []
    
    total_stats = len(poke_data['stats'])
    for s in range(total_stats):

        # Holds data for current stat
        # { 'name' : 'stat_name', 'base_stat' : stat_value }
        st = {}
        stat = poke_data['stats'][s]
        st['name'] = stat['stat']['name']
        st['base_stat'] = stat['base_stat']
        stats.append(st)
        
    poke['stats'] = stats
    
    # Holds list of types for current pokemon
    # [ { 'name' : 'type_name' } ]
    types = []
    
    total_types = len(poke_data['types'])
    for t in range(total_types):

        # Holds data for current type
        # { 'name' : 'type_name' }
        ty= {}
        type = poke_data['types'][t]
        ty['name'] = type['type']['name']
        types.append(ty)
        
    poke['types'] = types
    
    # Assign pokemon to its data
    pokemons[poke['name']] = poke

    # If you just want a list and not a dictionary/map
    # Append pokemon to list [] by
    # pokemons.append(poke)

    # If you want to assign pokemon by its index
    # pokemons[str(i + 1)] = poke
    
    print(i)

# JSONify everything and write to a file

with open("./pokedex_raw/pokedex_raw.json", "w") as f:
    f.write(json.dumps(pokemons))
    f.close()
