# two player chess game that will be the base of my adaptation into a THUD game

import os

import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Pygame!")
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
winner = ""
game_over = False
# promotion_pending: None, or ('white'/'black', pawn_index) while waiting for piece choice
promotion_pending = None

# set base directory for images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "piece_images", "pieces-png")

# game variables and images
black_pieces = [
    "rook",
    "knight",
    "bishop",
    "queen",
    "king",
    "bishop",
    "knight",
    "rook",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
]

black_locations = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (6, 0),
    (7, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
]

white_pieces = [
    "rook",
    "knight",
    "bishop",
    "queen",
    "king",
    "bishop",
    "knight",
    "rook",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
]


white_locations = [
    (0, 7),
    (1, 7),
    (2, 7),
    (3, 7),
    (4, 7),
    (5, 7),
    (6, 7),
    (7, 7),
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (6, 6),
    (7, 6),
]

captured_pieces_white = []
captured_pieces_black = []

# 0 - white turn, no selection: 1-whites turn, place selected: 2 - black turn, no selected: 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images (queen king rook bishop knight pawn) x 2
# piece_variable = pygame.image.load('path/to/image.png')

black_pawn = pygame.image.load(os.path.join(IMG_DIR, "black_pawn.png"))
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

black_rook = pygame.image.load(os.path.join(IMG_DIR, "black_rook.png"))
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_knight = pygame.image.load(os.path.join(IMG_DIR, "black_knight.png"))
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_bishop = pygame.image.load(os.path.join(IMG_DIR, "black_bishop.png"))
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_king = pygame.image.load(os.path.join(IMG_DIR, "black_king.png"))
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_queen = pygame.image.load(os.path.join(IMG_DIR, "black_queen.png"))
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

white_pawn = pygame.image.load(os.path.join(IMG_DIR, "white_pawn.png"))
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_rook = pygame.image.load(os.path.join(IMG_DIR, "white_rook.png"))
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_knight = pygame.image.load(os.path.join(IMG_DIR, "white_knight.png"))
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_bishop = pygame.image.load(os.path.join(IMG_DIR, "white_bishop.png"))
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_king = pygame.image.load(os.path.join(IMG_DIR, "white_king.png"))
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_queen = pygame.image.load(os.path.join(IMG_DIR, "white_queen.png"))
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_images = [
    white_pawn,
    white_rook,
    white_knight,
    white_bishop,
    white_queen,
    white_king,
]
black_images = [
    black_pawn,
    black_rook,
    black_knight,
    black_bishop,
    black_queen,
    black_king,
]

white_images_small = [
    white_pawn_small,
    white_rook_small,
    white_knight_small,
    white_bishop_small,
    white_queen_small,
    white_king_small,
]
black_images_small = [
    black_pawn_small,
    black_rook_small,
    black_knight_small,
    black_bishop_small,
    black_queen_small,
    black_king_small,
]

pieces_list = ["pawn", "rook", "knight", "bishop", "queen", "king"]
# check variables and flashing counter


# draw board for game
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(
                screen, "light gray", [600 - (column * 200), row * 100, 100, 100]
            )
        else:
            pygame.draw.rect(
                screen, "light gray", [700 - (column * 200), row * 100, 100, 100]
            )
        pygame.draw.rect(screen, "gray", [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, "purple", [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, "purple", [800, 0, 200, HEIGHT], 5)
        status_text = [
            "White: Select a piece!",
            "Move your piece!",
            "Black: Select a piece!",
            "Move your piece!",
        ]
        screen.blit(big_font.render(status_text[turn_step], True, "black"), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, "black", (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800), 2)


def draw_winner(winner_color):
    pygame.draw.rect(screen, "black", [150, 200, 500, 200])
    pygame.draw.rect(screen, "gold", [150, 200, 500, 200], 5)
    if winner_color == "Draw":
        win_text = big_font.render("Stalemate!", True, "gold")
        sub_text = font.render("The game is a draw", True, "white")
    else:
        win_text = big_font.render(f"{winner_color} Wins!", True, "gold")
        sub_text = font.render("by Checkmate", True, "white")
    restart_text = font.render("Press R to restart", True, "white")
    screen.blit(win_text, (200, 220))
    screen.blit(sub_text, (260, 290))
    screen.blit(restart_text, (260, 340))


# Draw pieces onto the board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = pieces_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(
                white_pawn,
                (white_locations[i][0] * 100 + 20, white_locations[i][1] * 100 + 20),
            )
        else:
            screen.blit(
                white_images[index],
                (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10),
            )
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(
                    screen,
                    "purple",
                    [
                        white_locations[i][0] * 100 + 1,
                        white_locations[i][1] * 100 + 1,
                        100,
                        100,
                    ],
                    2,
                )

    for i in range(len(black_pieces)):
        index = pieces_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            screen.blit(
                black_pawn,
                (black_locations[i][0] * 100 + 20, black_locations[i][1] * 100 + 20),
            )
        else:
            screen.blit(
                black_images[index],
                (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10),
            )
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(
                    screen,
                    "purple",
                    [
                        black_locations[i][0] * 100 + 1,
                        black_locations[i][1] * 100 + 1,
                        100,
                        100,
                    ],
                    2,
                )


# function to check all pieces valid moves
# w_locs and b_locs let simulations pass in hypothetical board states
# instead of always reading the globals (which broke check/pin detection)
def check_options(pieces, locations, turn, w_locs=None, b_locs=None):
    if w_locs is None:
        w_locs = white_locations
    if b_locs is None:
        b_locs = black_locations
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == "pawn":
            moves_list = check_pawn(location, turn, w_locs, b_locs)
        elif piece == "rook":
            moves_list = check_rook(location, turn, w_locs, b_locs)
        elif piece == "knight":
            moves_list = check_knight(location, turn, w_locs, b_locs)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn, w_locs, b_locs)
        elif piece == "queen":
            moves_list = check_queen(location, turn, w_locs, b_locs)
        elif piece == "king":
            moves_list = check_king(location, turn, w_locs, b_locs)
        all_moves_list.append(moves_list)
    return all_moves_list


# Check valid rook moves
def check_rook(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        enemies_list = b_locs
        friends_list = w_locs
    else:
        enemies_list = w_locs
        friends_list = b_locs
    for i in range(4):  # up down left right
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (
                (position[0] + (chain * x), position[1] + (chain * y))
                not in friends_list
                and 0 <= position[0] + (chain * x) <= 7
                and 0 <= position[1] + (chain * y) <= 7
            ):
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y))
                )
                if (
                    position[0] + (chain * x),
                    position[1] + (chain * y),
                ) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        if (
            (position[0], position[1] - 1) not in w_locs
            and (position[0], position[1] - 1) not in b_locs
            and position[1] > 0
        ):
            moves_list.append((position[0], position[1] - 1))
        if (
            (position[0], position[1] - 1) not in w_locs
            and (position[0], position[1] - 1) not in b_locs
            and (position[0], position[1] -2) not in w_locs
            and (position[0], position[1] -2) not in b_locs
            and position[1] == 6
        ):
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in b_locs:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in b_locs:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        if (
            (position[0], position[1] + 1) not in w_locs
            and (position[0], position[1] + 1) not in b_locs
            and position[1] < 7
        ):
            moves_list.append((position[0], position[1] + 1))
        if (
            (position[0], position[1] + 1) not in w_locs
            and (position[0], position[1] + 1) not in b_locs
            and (position[0], position[1] + 2) not in w_locs
            and (position[0], position[1] + 2) not in b_locs    
            and position[1] == 1
        ):
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in w_locs:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in w_locs:
            moves_list.append((position[0] - 1, position[1] + 1))
    return moves_list


# define moves for a bishop
def check_bishop(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        enemies_list = b_locs
        friends_list = w_locs
    else:
        enemies_list = w_locs
        friends_list = b_locs

    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        chain = 1
        path = True
        while path:
            new_x = position[0] + (chain * dx)
            new_y = position[1] + (chain * dy)
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                if (new_x, new_y) not in friends_list:
                    moves_list.append((new_x, new_y))
                    if (new_x, new_y) in enemies_list:
                        path = False
                else:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Now define valid moves of a knight
def check_knight(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        friends_list = w_locs
    else:
        friends_list = b_locs

    knight_moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    for move in knight_moves:
        new_x = position[0] + move[0]
        new_y = position[1] + move[1]
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if (new_x, new_y) not in friends_list:
                moves_list.append((new_x, new_y))

    return moves_list


# define valid moves for queen
def check_queen(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        enemies_list = b_locs
        friends_list = w_locs
    else:
        enemies_list = w_locs
        friends_list = b_locs

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        chain = 1
        path = True
        while path:
            new_x = position[0] + (chain * dx)
            new_y = position[1] + (chain * dy)
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                if (new_x, new_y) not in friends_list:
                    moves_list.append((new_x, new_y))
                    if (new_x, new_y) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
            else:
                path = False
    return moves_list


# define valid moves for king
def check_king(position, color, w_locs, b_locs):
    moves_list = []
    if color == "white":
        friends_list = w_locs
    else:
        friends_list = b_locs

    king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for move in king_moves:
        new_x = position[0] + move[0]
        new_y = position[1] + move[1]
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if (new_x, new_y) not in friends_list:
                moves_list.append((new_x, new_y))

    return moves_list


def is_in_check(color, w_locs, b_locs, w_pieces_list, b_pieces_list):
    """Return True if the given color's king is under attack.
    If the king was captured in a hypothetical simulation, treat as in check
    so that move is always rejected as illegal - kings cannot be captured."""
    if color == "white":
        if "king" not in w_pieces_list:
            return True
        king_loc = w_locs[w_pieces_list.index("king")]
        # pass the hypothetical board state into check_options
        enemy_moves = check_options(b_pieces_list, b_locs, "black", w_locs, b_locs)
    else:
        if "king" not in b_pieces_list:
            return True
        king_loc = b_locs[b_pieces_list.index("king")]
        enemy_moves = check_options(w_pieces_list, w_locs, "white", w_locs, b_locs)

    for move_set in enemy_moves:
        if king_loc in move_set:
            return True
    return False


def filter_legal_moves(piece_index, candidate_moves, color):
    """Remove any move that would leave our own king in check."""
    legal = []
    for move in candidate_moves:
        temp_w_locs = list(white_locations)
        temp_b_locs = list(black_locations)
        temp_w_pieces = list(white_pieces)
        temp_b_pieces = list(black_pieces)

        if color == "white":
            temp_w_locs[piece_index] = move
            if move in temp_b_locs:
                idx = temp_b_locs.index(move)
                temp_b_locs.pop(idx)
                temp_b_pieces.pop(idx)
        else:
            temp_b_locs[piece_index] = move
            if move in temp_w_locs:
                idx = temp_w_locs.index(move)
                temp_w_locs.pop(idx)
                temp_w_pieces.pop(idx)

        if not is_in_check(
            color, temp_w_locs, temp_b_locs, temp_w_pieces, temp_b_pieces
        ):
            legal.append(move)

    return legal


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
        color = "white"
    else:
        options_list = black_options
        color = "black"
    raw_moves = options_list[selection]
    return filter_legal_moves(selection, raw_moves, color)


# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = "red"
    else:
        color = "blue"
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5
        )


def draw_promotion_menu(color):
    """Draw a promotion choice panel in the right sidebar."""
    pygame.draw.rect(screen, "dark gray", [800, 0, 200, 800])
    pygame.draw.rect(screen, "gold", [800, 0, 200, 800], 4)
    label = font.render("Promote to:", True, "gold")
    screen.blit(label, (815, 20))
    promo_pieces = ["queen", "rook", "bishop", "knight"]
    if color == "white":
        images = [white_queen, white_rook, white_bishop, white_knight]
    else:
        images = [black_queen, black_rook, black_bishop, black_knight]
    for i, (piece, img) in enumerate(zip(promo_pieces, images)):
        y = 60 + i * 160
        pygame.draw.rect(screen, "gray", [810, y, 180, 140])
        pygame.draw.rect(screen, "white", [810, y, 180, 140], 2)
        screen.blit(img, (860, y + 30))
        piece_label = font.render(piece.capitalize(), True, "white")
        screen.blit(piece_label, (855, y + 110))


# main game loop

black_options = check_options(black_pieces, black_locations, "black")
white_options = check_options(white_pieces, white_locations, "white")


run = True
while run:
    timer.tick(fps)
    screen.fill("dark gray")
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Reset all game state
                white_pieces = [
                    "rook",
                    "knight",
                    "bishop",
                    "queen",
                    "king",
                    "bishop",
                    "knight",
                    "rook",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                ]
                white_locations = [
                    (0, 7),
                    (1, 7),
                    (2, 7),
                    (3, 7),
                    (4, 7),
                    (5, 7),
                    (6, 7),
                    (7, 7),
                    (0, 6),
                    (1, 6),
                    (2, 6),
                    (3, 6),
                    (4, 6),
                    (5, 6),
                    (6, 6),
                    (7, 6),
                ]
                black_pieces = [
                    "rook",
                    "knight",
                    "bishop",
                    "queen",
                    "king",
                    "bishop",
                    "knight",
                    "rook",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                    "pawn",
                ]
                black_locations = [
                    (0, 0),
                    (1, 0),
                    (2, 0),
                    (3, 0),
                    (4, 0),
                    (5, 0),
                    (6, 0),
                    (7, 0),
                    (0, 1),
                    (1, 1),
                    (2, 1),
                    (3, 1),
                    (4, 1),
                    (5, 1),
                    (6, 1),
                    (7, 1),
                ]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                winner = ""
                game_over = False
                promotion_pending = None
                black_options = check_options(black_pieces, black_locations, "black")
                white_options = check_options(white_pieces, white_locations, "white")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    # Check for pawn promotion (white reaches row 0)
                    if white_pieces[selection] == "pawn" and click_coords[1] == 0:
                        promotion_pending = ("white", selection)
                        selection = 100
                        valid_moves = []
                        continue
                    black_options = check_options(
                        black_pieces, black_locations, "black"
                    )
                    white_options = check_options(
                        white_pieces, white_locations, "white"
                    )
                    black_legal = []
                    for i in range(len(black_pieces)):
                        black_legal += filter_legal_moves(i, black_options[i], "black")
                    if len(black_legal) == 0 and is_in_check(
                        "black",
                        white_locations,
                        black_locations,
                        white_pieces,
                        black_pieces,
                    ):
                        winner = "White"
                        game_over = True
                    elif len(black_legal) == 0 and not is_in_check(
                        "black",
                        white_locations,
                        black_locations,
                        white_pieces,
                        black_pieces,
                    ):
                        winner = "Draw"
                        game_over = True

                    if not game_over:
                        turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    # Check for pawn promotion (black reaches row 7)
                    if black_pieces[selection] == "pawn" and click_coords[1] == 7:
                        promotion_pending = ("black", selection)
                        selection = 100
                        valid_moves = []
                        continue
                    black_options = check_options(
                        black_pieces, black_locations, "black"
                    )
                    white_options = check_options(
                        white_pieces, white_locations, "white"
                    )
                    white_legal = []
                    for i in range(len(white_pieces)):
                        white_legal += filter_legal_moves(i, white_options[i], "white")
                    if len(white_legal) == 0 and is_in_check(
                        "white",
                        white_locations,
                        black_locations,
                        white_pieces,
                        black_pieces,
                    ):
                        winner = "Black"
                        game_over = True
                    elif len(white_legal) == 0 and not is_in_check(
                        "white",
                        white_locations,
                        black_locations,
                        white_pieces,
                        black_pieces,
                    ):
                        winner = "Draw"
                        game_over = True
                    if not game_over:
                        turn_step = 0
                    selection = 100
                    valid_moves = []
    # Handle promotion menu clicks
    if promotion_pending is not None:
        promo_color, promo_index = promotion_pending
        draw_promotion_menu(promo_color)
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.button == 1:
                mx, my = event.pos
                if 810 <= mx <= 990:
                    promo_pieces = ["queen", "rook", "bishop", "knight"]
                    for i, piece in enumerate(promo_pieces):
                        y = 60 + i * 160
                        if y <= my <= y + 140:
                            if promo_color == "white":
                                white_pieces[promo_index] = piece
                            else:
                                black_pieces[promo_index] = piece
                            promotion_pending = None
                            # Now do post-move checks
                            black_options = check_options(black_pieces, black_locations, "black")
                            white_options = check_options(white_pieces, white_locations, "white")
                            if promo_color == "white":
                                black_legal = []
                                for j in range(len(black_pieces)):
                                    black_legal += filter_legal_moves(j, black_options[j], "black")
                                if len(black_legal) == 0 and is_in_check("black", white_locations, black_locations, white_pieces, black_pieces):
                                    winner = "White"
                                    game_over = True
                                elif len(black_legal) == 0:
                                    winner = "Draw"
                                    game_over = True
                                if not game_over:
                                    turn_step = 2
                            else:
                                white_legal = []
                                for j in range(len(white_pieces)):
                                    white_legal += filter_legal_moves(j, white_options[j], "white")
                                if len(white_legal) == 0 and is_in_check("white", white_locations, black_locations, white_pieces, black_pieces):
                                    winner = "Black"
                                    game_over = True
                                elif len(white_legal) == 0:
                                    winner = "Draw"
                                    game_over = True
                                if not game_over:
                                    turn_step = 0
                            break
    if game_over:
        draw_winner(winner)

    pygame.display.flip()
pygame.quit()