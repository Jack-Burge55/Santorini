import pygame
import sys
import math

pygame.init()
cell_size = 100
cell_number = 5
bar_width = 10
screen = pygame.display.set_mode((7 * cell_size + 6 * bar_width, 5 * cell_size + 6 * bar_width))
game_font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
# checks player count on board
player_counter = 0
# checks who is playing this turn
player_turn = 0
# checks where player pieces are
builder_locations = []
p_builder_locations = []
builder = None
moved = False
build_validity = False
move_validity = False
end_game = False
board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# Example
# level_one = pygame.image.load("C:\\Users\\Jack\\Desktop\\Graphics\\level_one.png").convert_alpha()
level_one = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\level_one.png").convert_alpha()
level_two = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\level_two.png").convert_alpha()
level_three = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\level_three.png").convert_alpha()
level_four = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\level_four.png").convert_alpha()
p_builder = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\p_builder.png").convert_alpha()
b_builder = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\b_builder.png").convert_alpha()
selector = pygame.image.load("C:\\Users\\jackb\OneDrive\\Desktop\\Graphics\\selector.png").convert_alpha()
grass = pygame.image.load("C:\\Users\\jackb\\OneDrive\\Desktop\\Graphics\\grass.png").convert_alpha()

height_dict = {-1: grass,0: level_one, 1: level_two, 2: level_three, 3: level_four}

def draw_board():
    board_base = pygame.Surface((7 * cell_size + 6 * bar_width, 5 * cell_size + 6 * bar_width))
    board_base.fill((64, 255, 83))
    side_menu = pygame.Surface((cell_size * 2, 5 * cell_size + 6 * bar_width))
    side_menu.fill((255, 239, 117))
    screen.blit(side_menu, (0, 0))
    screen.blit(board_base, (200, 0))
    builder_1 = pygame.Rect(82, 162, cell_size, cell_size)
    screen.blit(p_builder, builder_1)
    builder_2 = pygame.Rect(82, 342, cell_size, cell_size)
    screen.blit(b_builder, builder_2)
    square = pygame.Rect(50, 130, cell_size, cell_size)
    screen.blit(selector, square)
    vertical_line = pygame.Surface((bar_width, cell_size * cell_number + 6 * bar_width))
    horizontal_line = pygame.Surface((cell_size * cell_number + 6 * bar_width, bar_width))
    horizontal_line.fill((125, 125, 125))
    vertical_line.fill((125, 125, 125))
    for i in range(6):
        screen.blit(horizontal_line, (cell_size * 2, i * (cell_size + 10)))
        screen.blit(vertical_line, (i * (cell_size + 10) + 200, 0))

def current_height(x, y):
    return board[x][y]


def add_player(x, y, player_counter, player_turn):
    if [x, y] not in builder_locations and x >= 0:
        if player_turn == 0:
            builder_1 = pygame.Rect(242 + 110 * x, 41 + 110 * y, cell_size, cell_size)
            screen.blit(p_builder, builder_1)
            p_builder_locations.append([x, y])
            swap_square(player_turn)
        else:
            builder_2 = pygame.Rect(242 + 110 * x, 41 + 110 * y, cell_size, cell_size)
            screen.blit(b_builder, builder_2)
            swap_square(player_turn)
        builder_locations.append([x, y])
        player_counter += 1
        player_turn += 1
        player_turn %= 2
    return [player_counter, player_turn]


def swap_square(player_turn):
    if player_turn == 0:
        square = pygame.Rect(50, 310, cell_size, cell_size)
        screen.blit(selector, square)
        clear_square = pygame.Surface((cell_size, cell_size))
        clear_square.fill((255, 239, 117))
        screen.blit(clear_square, (50, 130))
        builder_1 = pygame.Rect(82, 162, cell_size, cell_size)
        screen.blit(p_builder, builder_1)
    else:
        square = pygame.Rect(50, 130, cell_size, cell_size)
        screen.blit(selector, square)
        clear_square = pygame.Surface((cell_size, cell_size))
        clear_square.fill((255, 239, 117))
        screen.blit(clear_square, (50, 310))
        builder_2 = pygame.Rect(82, 342, cell_size, cell_size)
        screen.blit(b_builder, builder_2)


def valid_builder(player_turn, builder_locations, p_builder_locations, x, y, builder):
    if player_turn == 0 and [x, y] in p_builder_locations:
        return [x, y]
    elif player_turn == 0 and [x, y] not in p_builder_locations:
        if builder is None:
            return None
        else:
            return builder
    elif player_turn == 1 and [x, y] in builder_locations and [x, y] not in p_builder_locations:
        return [x, y]
    elif player_turn == 1 and [x, y] not in builder_locations:
        if builder is None:
            return None
        else:
            return builder


def is_move_valid(builder, x, y, builder_locations, board):
    if (abs(builder[0] - x) <= 1 and abs(builder[1] - y) <= 1 and [abs(builder[0] - x), abs(builder[1] - y)] != [0, 0])  and (x >= 0) and ([x, y] not in builder_locations) and (board[x][y] - board[builder[0]][builder[1]] <= 1):
        return True
    else:
        return False


def is_build_valid(builder, x, y, builder_locations, board):
    if (abs(builder[0] - x) <= 1 and abs(builder[1] - y) <= 1 and [abs(builder[0] - x), abs(builder[1] - y)] != [0, 0])  and (x >= 0) and ([x, y] not in builder_locations) and (board[x][y] < 4):
        return True
    else:
        return False

draw_board()
while end_game is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Gets tile coords and height of selected tile
            pos = pygame.mouse.get_pos()
            x, y = math.floor((pos[0] - 210) / 110), math.floor((pos[1] - 10) / 110)
            tile = pygame.Rect(210 + 110 * x, 10 + 110 * y, cell_size, cell_size)
            ht = current_height(x, y)
            if player_counter == 4:
                # Builder check
                if builder is None:
                    builder = valid_builder(player_turn, builder_locations, p_builder_locations, x, y, builder)
                else:
                    if moved is False:
                        move_validity = is_move_valid(builder, x, y, builder_locations, board)
                        if move_validity is False:
                            builder = valid_builder(player_turn, builder_locations, p_builder_locations, x, y, builder)
                        else:
                            moved = True
                            temp = height_dict[current_height(builder[0], builder[1]) - 1]
                            builder_tile = pygame.Rect(210 + 110 * builder[0], 10 + 110 * builder[1], cell_size, cell_size)
                            screen.blit(temp, builder_tile)
                            if player_turn == 0:
                                builder_1 = pygame.Rect(242 + 110 * x, 41 + 110 * y, cell_size, cell_size)
                                screen.blit(p_builder, builder_1)
                                p_builder_locations.remove([builder[0], builder[1]])
                                p_builder_locations.append([x, y])
                                builder_locations.remove([builder[0], builder[1]])
                                builder_locations.append([x, y])
                            else:
                                builder_2 = pygame.Rect(242 + 110 * x, 41 + 110 * y, cell_size, cell_size)
                                screen.blit(b_builder, builder_2)
                                builder_locations.remove([builder[0], builder[1]])
                                builder_locations.append([x, y])
                            if board[x][y] == 3:
                                end_game = True
                            builder = [x, y]
                    else:
                        build_validity = is_build_valid(builder, x, y, builder_locations, board)
                        if build_validity is True:
                            board[x][y] += 1
                            temp = height_dict[current_height(x, y) - 1]
                            screen.blit(temp, tile)
                            swap_square(player_turn)
                            player_turn += 1
                            player_turn %= 2
                            builder = None
                            moved = False
                            build_validity = False
                            move_validity = False

            # Adds Player if not 4
            if player_counter <= 3:
                temp = add_player(x, y, player_counter, player_turn)
                player_counter = temp[0]
                player_turn = temp[1]
    pygame.display.update()
    clock.tick(15)
