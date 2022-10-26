from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for element in self.pokemons:
            if element.name == pokemon_name:
                self.pokemons.remove(element)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        data = []
        data.append(f"Pokemon Trainer {self.name}")
        data.append(f"Pokemon count {len(self.pokemons)}")
        for element in self.pokemons:
            data.append(f"- {element.pokemon_details()}")
        return '\n'.join(data)
