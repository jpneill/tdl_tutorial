from enum import Enum

class RenderOrder(Enum):
    CORPSE = 1
    ITEM = 2
    ACTOR = 3

def render_bar(panel, x, y, total_width, name, value, maximum, bar_colour, back_colour, string_colour):
    bar_width = int(float(value) / maximum * total_width)

    panel.draw_rect(x, y, total_width, 1, None, bg=back_colour)

    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, None, bg=bar_colour)

    text = name + ': ' + str(value) + '/' + str(maximum)
    x_centered = x + int((total_width-len(text)) / 2)

    panel.draw_str(x_centered, y, text, fg=string_colour, bg=None)

def render_all(con, panel, entities, player, game_map, fov_recompute, root_console, screen_width, screen_height, bar_width, panel_height, panel_y, colours):
    if fov_recompute:
        for x, y in game_map:
            wall = not game_map.transparent[x, y]

            if game_map.fov[x, y]:
                if wall:
                    con.draw_char(x, y, None, fg=None, bg=colours.get('light_wall'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colours.get('light_ground'))

                game_map.explored[x][y] = True

            elif game_map.explored[x][y]:
                if wall:
                    con.draw_char(x, y, None, fg=None, bg=colours.get('dark_wall'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colours.get('dark_ground'))

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

    # Draw all entities in the list
    for entity in entities_in_render_order:
        draw_entity(con, entity, game_map.fov)

    root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)

    panel.clear(fg=colours.get('white'), bg=colours.get('black'))

    render_bar(panel, 1, 1, bar_width, 'HP', player.fighter.hp, player.fighter.max_hp, colours.get('light_red'), colours.get('darker_red'), colours.get('white'))

    root_console.blit(panel, 0, panel_y, screen_width, panel_height, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov):
    if fov[entity.x, entity.y]:
        con.draw_char(entity.x, entity.y, entity.char, entity.colour, bg=None)


def clear_entity(con, entity):
    # erase the character that represents this object
    con.draw_char(entity.x, entity.y, ' ', entity.colour, bg=None)

