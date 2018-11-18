from game_states import GameStates
from game_messages import Message
from render_functions import RenderOrder

def kill_player(player, colours):
    player.char = '%'
    player.colour = colours.get('dark_red')

    return Message('You Died!',colours.get('red')), GameStates.PLAYER_DEAD

def kill_monster(monster, colours):
    dead_message = Message('{0} is dead!'.format(monster.name.capitalize()),colours.get('orange'))

    monster.char = '%'
    monster.colour = colours.get('dark_red')
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.render_order = RenderOrder.CORPSE
    monster.name = 'remains of ' + monster.name

    return dead_message
