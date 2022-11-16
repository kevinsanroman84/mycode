import character

player = character.Rogue("Kevin")
character.Character.player_moves = 200

monster = character.Monster()


print(player.attack_damage(monster))

