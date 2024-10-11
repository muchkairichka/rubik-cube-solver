from cube import RubiksCube2x2


cube = RubiksCube2x2()
cube.display_cube()  # Показываем начальное состояние кубика
cube.rotate_R_prime()
cube.rotate_R()
print("===")
cube.display_cube()  # Показываем состояние после запутывания
