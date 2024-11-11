from cube import RubiksCube2x2
from method_sexy_mode_2_2 import method_sexy_mode_2_2


# cube = RubiksCube2x2()
# cube.display_cube()  # Показываем начальное состояние кубика
# cube.rotate_R_prime()
# cube.rotate_R()
# print("===")
# cube.display_cube()  # Показываем состояние после запутывания

c = {
    "U": ["W", "R", "O", "O"], # UP
    "D": ["R", "W", "G", "O"], # DOWN
    "F": ["G", "B", "Y", "R"], # FRONT
    "B": ["W", "B", "G", "R"], # BACK
    "R": ["Y", "B", "G", "W"], # RIGHT
    "L": ["O", "Y", "Y", "B"]  # LEFT
}
c = {
    "U": ['W', 'B', 'O', 'O'],
    "F": ['G', 'G', 'R', 'B'],
    "R": ['W', 'W', 'W', 'Y'],
    "D": ['B', 'O', 'Y', 'O'],
    "L": ['R', 'Y', 'R', 'Y'],
    "B": ['R', 'G', 'B', 'G']
}

for i in range(650):
    print("===")
    print(i)
    print("===")
    cube = RubiksCube2x2()
    cube.scramble()
    cube.display_cube() 
    print("===")
    method_sexy_mode_2_2(cube)
    cube.display_cube() 
