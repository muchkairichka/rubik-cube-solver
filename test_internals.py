from cube import RubiksCube2x2


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
    cube._rotate_face("F", clockwise=True)

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
    cube._rotate_face("F", clockwise=False)

    cube_result = {
        "U": ["W", "O", "R", "W"], # UP
        "D": ["Y", "B", "G", "R"], # DOWN
        "F": ["G", "O", "Y", "B"], # FRONT
        "B": ["W", "B", "B", "Y"], # BACK
        "R": ["R", "G", "Y", "W"], # RIGHT
        "L": ["O", "G", "O", "R"]  # LEFT
    }
    assert cube.cube == cube_result