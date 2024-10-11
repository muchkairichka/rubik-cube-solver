from cube import RubiksCube2x2

def test_rotation_r():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_R()

    expected_result = {
        "U": ["Y", "B", "R", "R"], # UP
        "D": ["W", "Y", "O", "B"], # DOWN
        "F": ["Y", "B", "G", "O"], # FRONT
        "B": ["W", "B", "Y", "W"], # BACK
        "R": ["W", "O", "G", "O"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_r_prime():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_R_prime()

    expected_result = {
        "U": ["Y", "Y", "R", "B"], # UP
        "D": ["W", "B", "O", "R"], # DOWN
        "F": ["Y", "Y", "G", "W"], # FRONT
        "B": ["O", "B", "B", "W"], # BACK
        "R": ["O", "G", "O", "W"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_r_back_and_forth():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_R()
    cube.rotate_R_prime()

    assert cube.cube == original_cube

def test_rotation_l():
    original_cube = {
        "U": ["Y", "W", "R", "W"], # UP
        "D": ["Y", "O", "O", "W"], # DOWN
        "F": ["Y", "R", "B", "W"], # FRONT
        "B": ["O", "G", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["O", "G", "B", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_L()

    expected_result = {
        "U": ["Y", "W", "G", "W"], # UP
        "D": ["Y", "O", "B", "W"], # DOWN
        "F": ["Y", "R", "R", "W"], # FRONT
        "B": ["O", "O", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["B", "O", "R", "G"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_l_prime():
    original_cube = {
        "U": ["Y", "W", "R", "W"], # UP
        "D": ["Y", "O", "O", "W"], # DOWN
        "F": ["Y", "R", "B", "W"], # FRONT
        "B": ["O", "G", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["O", "G", "B", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_L_prime()

    expected_result = {
        "U": ["Y", "W", "B", "W"], # UP
        "D": ["Y", "O", "G", "W"], # DOWN
        "F": ["Y", "R", "O", "W"], # FRONT
        "B": ["O", "R", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["G", "R", "O", "B"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_l_back_and_forth():
    original_cube = {
        "U": ["Y", "W", "R", "W"], # UP
        "D": ["Y", "O", "O", "W"], # DOWN
        "F": ["Y", "R", "B", "W"], # FRONT
        "B": ["O", "G", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["O", "G", "B", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_L()
    cube.rotate_L_prime()

    assert cube.cube == original_cube

def test_rotation_u_prime():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_U_prime()

    expected_result = {
        "U": ["B", "R", "Y", "W"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["O", "R", "G", "O"], # FRONT
        "B": ["Y", "R", "G", "W"], # BACK
        "R": ["B", "G", "Y", "W"], # RIGHT
        "L": ["Y", "G", "O", "R"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_u():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_U()

    expected_result = {
        "U": ["W", "Y", "R", "B"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["Y", "R", "G", "O"], # FRONT
        "B": ["O", "R", "G", "W"], # BACK
        "R": ["Y", "G", "Y", "W"], # RIGHT
        "L": ["B", "G", "O", "R"]  # LEFT
    }

    assert cube.cube == expected_result

def test_rotation_u_back_and_forth():
    original_cube = {
        "U": ["Y", "W", "R", "W"], # UP
        "D": ["Y", "O", "O", "W"], # DOWN
        "F": ["Y", "R", "B", "W"], # FRONT
        "B": ["O", "G", "G", "Y"], # BACK
        "R": ["B", "B", "G", "R"], # RIGHT
        "L": ["O", "G", "B", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_U()
    cube.rotate_U_prime()

    assert cube.cube == original_cube

def test_rotation_d_prime():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_D_prime()

    expected_result = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["B", "O", "W", "B"], # DOWN
        "F": ["B", "G", "Y", "W"], # FRONT
        "B": ["Y", "G", "O", "R"], # BACK
        "R": ["Y", "R", "G", "W"], # RIGHT
        "L": ["O", "R", "G", "O"]  # LEFT
    }
    assert cube.cube == expected_result

def test_rotation_d():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_D()

    expected_result = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["B", "W", "O", "B"], # DOWN
        "F": ["B", "G", "O", "R"], # FRONT
        "B": ["Y", "G", "Y", "W"], # BACK
        "R": ["Y", "R", "G", "O"], # RIGHT
        "L": ["O", "R", "G", "W"]  # LEFT
    }
    assert cube.cube == expected_result

def test_rotation_d_back_and_forth():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_D()
    cube.rotate_D_prime()

    assert cube.cube == original_cube


def test_rotation_b():
    original_cube = {
        "U": ["Y", "B", "W", "R"], # UP
        "D": ["W", "B", "B", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["Y", "G", "G", "W"], # BACK
        "R": ["Y", "R", "Y", "W"], # RIGHT
        "L": ["O", "R", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_B()

    expected_result = {
        "U": ["R", "W", "W", "R"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["B", "G", "G", "O"], # FRONT
        "B": ["G", "Y", "W", "G"], # BACK
        "R": ["Y", "O", "Y", "B"], # RIGHT
        "L": ["B", "R", "Y", "R"]  # LEFT
    }
    assert cube.cube == expected_result

def test_rotation_b_prime():
    original_cube = {
        "U": ["B", "R", "R", "Y"], # UP
        "D": ["G", "G", "O", "R"], # DOWN
        "F": ["B", "G", "W", "W"], # FRONT
        "B": ["Y", "O", "B", "Y"], # BACK
        "R": ["O", "G", "R", "W"], # RIGHT
        "L": ["W", "Y", "B", "O"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_B_prime()

    expected_result = {
        "U": ["B", "W", "R", "Y"], # UP
        "D": ["G", "G", "W", "G"], # DOWN
        "F": ["B", "G", "W", "W"], # FRONT
        "B": ["O", "Y", "Y", "B"], # BACK
        "R": ["O", "B", "R", "R"], # RIGHT
        "L": ["O", "Y", "R", "O"]  # LEFT
    }
    assert cube.cube == expected_result

def test_rotation_b_back_and_forth():
    original_cube = {
        "U": ["B", "R", "R", "Y"], # UP
        "D": ["G", "G", "O", "R"], # DOWN
        "F": ["B", "G", "W", "W"], # FRONT
        "B": ["Y", "O", "B", "Y"], # BACK
        "R": ["O", "G", "R", "W"], # RIGHT
        "L": ["W", "Y", "B", "O"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_B()
    cube.rotate_B_prime()

    assert cube.cube == original_cube

def test_rotation_F():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    rotated_cube = {
        "U": ["Y", "Y", "R", "G"], # UP
        "D": ["W", "O", "O", "O"], # DOWN
        "F": ["G", "Y", "R", "B"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["R", "O", "W", "G"], # RIGHT
        "L": ["R", "W", "G", "B"]  # LEFT
    }

    cube.rotate_F()

    assert cube.cube == rotated_cube

def test_rotation_F_prime():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    rotated_cube = {
        "U": ["Y", "Y", "O", "W"], # UP
        "D": ["G", "R", "O", "O"], # DOWN
        "F": ["B", "R", "Y", "G"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["B", "O", "W", "G"], # RIGHT
        "L": ["R", "W", "G", "R"]  # LEFT
    }

    cube.rotate_F_prime()

    assert cube.cube == rotated_cube

def test_rotation_F_back_and_forth():
    original_cube = {
        "U": ["Y", "Y", "R", "W"], # UP
        "D": ["W", "B", "O", "O"], # DOWN
        "F": ["Y", "B", "G", "R"], # FRONT
        "B": ["B", "B", "Y", "W"], # BACK
        "R": ["O", "O", "W", "G"], # RIGHT
        "L": ["R", "G", "G", "R"]  # LEFT
    }
    cube = RubiksCube2x2(original_cube)

    cube.rotate_F()
    cube.rotate_F_prime()

    assert cube.cube == original_cube

def test_rotation_face():
    c = {
        "U": ["W", "O", "R", "W"], # UP
        "D": ["Y", "B", "G", "R"], # DOWN
        "F": ["Y", "G", "B", "O"], # FRONT
        "B": ["W", "B", "B", "Y"], # BACK
        "R": ["R", "G", "Y", "W"], # RIGHT
        "L": ["O", "G", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(c)
    cube.rotate_face("F")

    cube_result = {
        "U": ["W", "O", "R", "W"], # UP
        "D": ["Y", "B", "G", "R"], # DOWN
        "F": ["B", "Y", "O", "G"], # FRONT
        "B": ["W", "B", "B", "Y"], # BACK
        "R": ["R", "G", "Y", "W"], # RIGHT
        "L": ["O", "G", "O", "R"]  # LEFT
    }
    assert cube.cube == cube_result

def test_rotation_face_prime():
    c = {
        "U": ["W", "O", "R", "W"], # UP
        "D": ["Y", "B", "G", "R"], # DOWN
        "F": ["Y", "G", "B", "O"], # FRONT
        "B": ["W", "B", "B", "Y"], # BACK
        "R": ["R", "G", "Y", "W"], # RIGHT
        "L": ["O", "G", "O", "R"]  # LEFT
    }
    cube = RubiksCube2x2(c)
    cube.rotate_face_prime("F")

    cube_result = {
        "U": ["W", "O", "R", "W"], # UP
        "D": ["Y", "B", "G", "R"], # DOWN
        "F": ["G", "O", "Y", "B"], # FRONT
        "B": ["W", "B", "B", "Y"], # BACK
        "R": ["R", "G", "Y", "W"], # RIGHT
        "L": ["O", "G", "O", "R"]  # LEFT
    }
    assert cube.cube == cube_result
