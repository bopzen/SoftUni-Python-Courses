class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __check_if_supply_type_exists(self, supply_type):
        for supply in self.supplies:
            if supply.__class__.__name__ == supply_type:
                return True

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_last_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == supply_type:
                current_supply = self.supplies.pop(i)
                return current_supply
        if supply_type == 'Food':
            raise Exception("There are no food supplies left!")
        if supply_type == 'Drink':
            raise Exception("There are no drink supplies left!")

    @staticmethod
    def __attack(player1, player2):
        player2.stamina -= player1.stamina / 2

        if player1.stamina - (player2.stamina / 2) < 0:
            player1.stamina = 0
        else:
            player1.stamina -= player2.stamina / 2
        if player1.stamina < player2.stamina:
            return f"Winner: {player2.name}"
        else:
            return f"Winner: {player1.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def add_player(self, *players):
        players_to_add = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_to_add.append(player.name)
        return f"Successfully added: {', '.join(players_to_add)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name, sustenance_type):
        current_player = self.__find_player(player_name)
        if current_player.stamina == 100:
            return f"{current_player.name} have enough stamina."
        current_supply = self.__find_last_supply(sustenance_type)
        if current_supply:
            if current_player.stamina + current_supply.energy > 100:
                current_player.stamina = 100
            else:
                current_player.stamina += current_supply.energy
            return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name, second_player_name):
        player1 = self.__find_player(first_player_name)
        player2 = self.__find_player(second_player_name)
        result = self.__check_if_the_players_cannot_duel(player1, player2)
        if result:
            return result
        if player1.stamina < player2.stamina:
            return self.__attack(player1, player2)
        else:
            return self.__attack(player2, player1)

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = [str(player) for player in self.players]
        for supply in self.supplies:
            result.append(supply.details())
        return '\n'.join(result)