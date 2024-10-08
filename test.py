from main import RubiksCube2x2

def test_rotation_r():
    cube = RubiksCube2x2()
    cube.rotate_R()

    cube_result = {
        'U': ['W', 'G', 'W', 'G'],  # Белая
        'D': ['Y', 'B', 'Y', 'B'],  # Желтая
        'F': ['G', 'Y', 'G', 'Y'],  # Зеленая
        'B': ['W', 'B', 'W', 'B'],  # Синяя
        'R': ['R', 'R', 'R', 'R'],  # Красная
        'L': ['O', 'O', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_r_prime():
    cube = RubiksCube2x2()
    cube.rotate_R_prime()

    cube_result = {
        'U': ['W', 'B', 'W', 'B'],  # Белая
        'D': ['Y', 'G', 'Y', 'G'],  # Желтая
        'F': ['G', 'W', 'G', 'W'],  # Зеленая
        'B': ['Y', 'B', 'Y', 'B'],  # Синяя
        'R': ['R', 'R', 'R', 'R'],  # Красная
        'L': ['O', 'O', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_l():
    cube = RubiksCube2x2()
    cube.rotate_L()

    cube_result = {
        'U': ['B', 'W', 'B', 'W'],  # Белая
        'D': ['G', 'Y', 'G', 'Y'],  # Желтая
        'F': ['W', 'G', 'W', 'G'],  # Зеленая
        'B': ['B', 'Y', 'B', 'Y'],  # Синяя
        'R': ['R', 'R', 'R', 'R'],  # Красная
        'L': ['O', 'O', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_l_prime():
    cube = RubiksCube2x2()
    cube.rotate_L_prime()

    cube_result = {
        'U': ['G', 'W', 'G', 'W'],  # Белая
        'D': ['B', 'Y', 'B', 'Y'],  # Желтая
        'F': ['Y', 'G', 'Y', 'G'],  # Зеленая
        'B': ['B', 'W', 'B', 'W'],  # Синяя
        'R': ['R', 'R', 'R', 'R'],  # Красная
        'L': ['O', 'O', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_u_prime():
    cube = RubiksCube2x2()
    cube.rotate_U_prime()

    cube_result = {
        'U': ['W', 'W', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'Y', 'Y'],  # Желтая
        'F': ['R', 'R', 'G', 'G'],  # Зеленая
        'B': ['O', 'O', 'B', 'B'],  # Синяя
        'R': ['B', 'B', 'R', 'R'],  # Красная
        'L': ['G', 'G', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_u():
    cube = RubiksCube2x2()
    cube.rotate_U()

    cube_result = {
        'U': ['W', 'W', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'Y', 'Y'],  # Желтая
        'F': ['O', 'O', 'G', 'G'],  # Зеленая
        'B': ['R', 'R', 'B', 'B'],  # Синяя
        'R': ['G', 'G', 'R', 'R'],  # Красная
        'L': ['B', 'B', 'O', 'O']   # Оранжевая
    }

    assert cube.cube == cube_result

def test_rotation_d_prime():
    cube = RubiksCube2x2()
    cube.rotate_D_prime()

    cube_result = {
        'U': ['W', 'W', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'Y', 'Y'],  # Желтая
        'F': ['G', 'G', 'O', 'O'],  # Зеленая
        'B': ['B', 'B', 'R', 'R'],  # Синяя
        'R': ['R', 'R', 'G', 'G'],  # Красная
        'L': ['O', 'O', 'B', 'B']   # Оранжевая
    }
    assert cube.cube == cube_result

def test_rotation_d():
    cube = RubiksCube2x2()
    cube.rotate_D()

    cube_result = {
        'U': ['W', 'W', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'Y', 'Y'],  # Желтая
        'F': ['G', 'G', 'R', 'R'],  # Зеленая
        'B': ['B', 'B', 'O', 'O'],  # Синяя
        'R': ['R', 'R', 'B', 'B'],  # Красная
        'L': ['O', 'O', 'G', 'G']   # Оранжевая
    }
    assert cube.cube == cube_result

def test_rotation_b():
    cube = RubiksCube2x2()
    cube.rotate_B()

    cube_result = {
        'U': ['R', 'R', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'O', 'O'],  # Желтая
        'F': ['G', 'G', 'G', 'G'],  # Зеленая
        'B': ['B', 'B', 'B', 'B'],  # Синяя
        'R': ['R', 'Y', 'R', 'Y'],  # Красная
        'L': ['W', 'O', 'W', 'O']   # Оранжевая
    }
    assert cube.cube == cube_result

def test_rotation_b_prime():
    cube = RubiksCube2x2()
    cube.rotate_B_prime()

    cube_result = {
        'U': ['O', 'O', 'W', 'W'],  # Белая
        'D': ['Y', 'Y', 'R', 'R'],  # Желтая
        'F': ['G', 'G', 'G', 'G'],  # Зеленая
        'B': ['B', 'B', 'B', 'B'],  # Синяя
        'R': ['R', 'W', 'R', 'W'],  # Красная
        'L': ['Y', 'O', 'Y', 'O']   # Оранжевая
    }
    assert cube.cube == cube_result

def test_rotation_face():
    c = {
        "U": ["W", "O", "R", "W"],
        "D": ["Y", "B", "G", "R"],
        "F": ["Y", "G", "B", "O"],
        "B": ["W", "B", "B", "Y"],
        "R": ["R", "G", "Y", "W"],
        "L": ["O", "G", "O", "R"]
    }
    cube = RubiksCube2x2(c)
    cube.rotate_face("F")

    cube_result = {
        "U": ["W", "O", "R", "W"],
        "D": ["Y", "B", "G", "R"],
        "F": ["B", "Y", "O", "G"],
        "B": ["W", "B", "B", "Y"],
        "R": ["R", "G", "Y", "W"],
        "L": ["O", "G", "O", "R"]
    }
    assert cube.cube == cube_result

def test_rotation_face_prime():
    c = {
        "U": ["W", "O", "R", "W"],
        "D": ["Y", "B", "G", "R"],
        "F": ["Y", "G", "B", "O"],
        "B": ["W", "B", "B", "Y"],
        "R": ["R", "G", "Y", "W"],
        "L": ["O", "G", "O", "R"]
    }
    cube = RubiksCube2x2(c)
    cube.rotate_face_prime("F")

    cube_result = {
        "U": ["W", "O", "R", "W"],
        "D": ["Y", "B", "G", "R"],
        "F": ["G", "O", "Y", "B"],
        "B": ["W", "B", "B", "Y"],
        "R": ["R", "G", "Y", "W"],
        "L": ["O", "G", "O", "R"]
    }
    assert cube.cube == cube_result