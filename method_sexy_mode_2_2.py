
from cube import Side

def sexy_mode(cube, right=True):
    """Выполняет последовательность движений "sexy move"."""
    if right:
        moves = [cube.rotate_R, cube.rotate_U, cube.rotate_R_prime, cube.rotate_U_prime]
    else:
        moves = [cube.rotate_L_prime, cube.rotate_U_prime, cube.rotate_L, cube.rotate_U]

    for move in moves:
        move()

def get_corners(cube):
    """Возвращает словарь углов с указанием цветов для каждой грани."""
    return {
        "F0": [cube.cube[Side.Front][0], cube.cube[Side.Left][1], cube.cube[Side.Up][2]],
        "F1": [cube.cube[Side.Front][1], cube.cube[Side.Up][3], cube.cube[Side.Right][0]],
        "F2": [cube.cube[Side.Front][2], cube.cube[Side.Down][0], cube.cube[Side.Left][3]],
        "F3": [cube.cube[Side.Front][3], cube.cube[Side.Right][2], cube.cube[Side.Down][1]],
        "B0": [cube.cube[Side.Back][0], cube.cube[Side.Right][1], cube.cube[Side.Up][1]],
        "B1": [cube.cube[Side.Back][1], cube.cube[Side.Up][0], cube.cube[Side.Left][0]],
        "B2": [cube.cube[Side.Back][2], cube.cube[Side.Down][3], cube.cube[Side.Right][3]],
        "B3": [cube.cube[Side.Back][3], cube.cube[Side.Left][2], cube.cube[Side.Down][2]]
    }

def orient_white_down(cube):
    """Ориентирует куб так, чтобы белая сторона находилась внизу."""
    if not cube.cube[Side.Down].count('W'):
        rotations = {
            Side.Front: cube.rotate_X_prime,
            Side.Back: cube.rotate_X,
            Side.Right: cube.rotate_Z,
            Side.Left: cube.rotate_Z_prime,
            Side.Up: lambda: (cube.rotate_Z(), cube.rotate_Z())
        }
        for face, rotate in rotations.items():
            if cube.cube[face].count('W'):
                rotate()
                break

def adjust_bottom_left_corner(cube):
    """Подгоняет нижний левый угол так, чтобы он был белым."""
    adjustments = {
        1: cube.rotate_D_prime,
        2: cube.rotate_D,
        3: lambda: (cube.rotate_D(), cube.rotate_D())
    }
    for position, adjust in adjustments.items():
        if cube.cube[Side.Down][position] == 'W':
            adjust()
            break

def build_white_side(cube):
    """Собирает белую сторону."""
    while cube.cube[Side.Down].count('W') < 4:
        if сoncer_in_place_F3(cube):
            cube.rotate_D_prime()
        move_сoncer_to_place_F1(cube.cube[Side.Down][0], cube.cube[Side.Front][2], cube)
        while not сoncer_in_place_F3(cube):
            sexy_mode(cube)

def align_two_or_more_corners(cube):
    """Выравнивает два или более углов."""
    while count_matching_corners(cube) < 2:
        cube.rotate_U_prime()
    count = 0
    while count_matching_corners_left(cube) < 2 and count < 5:
        cube.rotate_Y_prime()
        count += 1

def align_all_corners(cube):
    """Выравнивает все углы на место."""
    while count_matching_corners(cube) != 4:
        for _ in range(3):
            sexy_mode(cube)
        cube.rotate_Y()
        for _ in range(3):
            sexy_mode(cube, right=False)
        while count_matching_corners(cube) < 2:
            cube.rotate_U_prime()
        while count_matching_corners_left(cube) < 2:
            cube.rotate_Y_prime()
    cube.rotate_X()
    cube.rotate_X()

def place_all_yellows(cube):
    """Подгоняет все желтые элементы на место."""
    while cube.cube[Side.Down].count("Y") != 4:
        while cube.cube[Side.Down][1] != "Y":
            sexy_mode(cube)
        cube.rotate_D_prime()
    while count_matching_corners(cube) == 0:
        cube.rotate_U_prime()

def сoncer_in_place_F3(cube):
    """Проверяет, находится ли угловой элемент F3 на своем месте."""
    return (cube.cube[Side.Down][0] == "W" and
            cube.cube[Side.Down][1] == 'W' and
            cube.cube[Side.Front][2] == cube.cube[Side.Front][3])

def move_сoncer_to_place_F1(side1, side2, cube):
    """Перемещает указанный угол на место F1, если цвета совпадают."""
    corners = get_corners(cube)
    positions = {
        "F1": lambda: None,
        "F0": cube.rotate_U_prime,
        "F3": lambda: sexy_mode(cube),
        "B0": cube.rotate_U,
        "B1": lambda: (cube.rotate_U(), cube.rotate_U()),
        "B2": lambda: (cube.rotate_R(), cube.rotate_R()),
        "B3": lambda: (cube.rotate_B_prime(), cube.rotate_U(), cube.rotate_U())
    }
    for position, move in positions.items():
        if corners[position].count(side1) and corners[position].count(side2):
            move()
            break

def check_corner(corner1, corner2):
    """Проверяет, совпадают ли углы corner1 и corner2 по цветам (кроме 'Y')."""
    side1 = corner1[0] if corner1[0] != "Y" else corner1[1]
    side2 = corner1[2] if corner1[2] != "Y" else corner1[1]
    return corner2.count(side1) and corner2.count(side2)

def count_matching_corners(cube):
    """Возвращает количество совпадающих углов."""
    pairs = [("F0", "F2"), ("F1", "F3"), ("B0", "B2"), ("B1", "B3")]
    return sum(check_corner(get_corners(cube)[c1], get_corners(cube)[c2]) for c1, c2 in pairs)

def count_matching_corners_left(cube):
    """Возвращает количество совпадающих углов на левой стороне."""
    pairs = [("F0", "F2"), ("B1", "B3")]
    return sum(check_corner(get_corners(cube)[c1], get_corners(cube)[c2]) for c1, c2 in pairs)

def method_sexy_mode_2_2(cube):

    # Выполнение основных этапов
    orient_white_down(cube)
    
    adjust_bottom_left_corner(cube)
    
    build_white_side(cube)
    
    align_two_or_more_corners(cube)
    
    align_all_corners(cube)
    
    place_all_yellows(cube)
