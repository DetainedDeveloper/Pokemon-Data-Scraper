# Pokemon Data Scraper

I wanted to make different Pokemon projects, so I scraped the data. [Here](https://github.com/DetainedDeveloper/Pokemon-Data-Scraper/tree/main/pokedex_raw) it is, have fun!

- **`pokedex_raw.json`** and **`pokedex.json`** have **same** data
- Just that **`pokedex_raw.json`** is all in one line
- Whilst I've properly formatted **`pokedex.json`**

# Brief Explanation

- First of all, **`requests`** and **`json`** already come with **`python`**, so there is no need for **`requirements.txt`**
- I've added **`comments`** and that cover everything in detail

### How code works

1. A **`request`** is sent to [Pokemon API](https://pokeapi.co/) followed by pokemon's **`id`**

2. Then convert the response to **`json`**

3. **`poke{}`** **dictionary/map** holds data for **current** pokemon
    - **`id`**
    - **`name`**
    - **`height`**
    - **`weight`**
    - **`xp`**
    - **`image_url`** [Pokeres](https://pokeres.bastionbot.org/)

4. **`abilities[]`**, **`stats[]`** and **`types[]`** hold data of abilities, stats and types of **current** pokemon and then, assigned to **current** pokemon
    - **`poke['abilities'] = abilities`**
    - **`poke['stats'] = stats`**
    - **`poke['types'] = types`**

5. Then, the **current** **`poke{}`** is assigned to **`pokemons{}`** with the key of pokemon's name
    - **`pokemons[poke['name']] = poke`**

6. Finally, **`pokemons{}`** is converted to **`json`** and stored in a **`.json`** file