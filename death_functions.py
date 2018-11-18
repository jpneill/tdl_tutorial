from game_states import GameStates

def kill_player(player, colours):
    player.char = '%'
    player.colour = colours.get('dark_red')

    return 'You died!', GameStates.PLAYER_DEAD

def kill_monster(monster, colours):
    dead_message = '{0} is dead!'.format(monster.name.capitalize())

    monster.char = '%'
    monster.colour = colours.get('dark_red')
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name

    return dead_message
