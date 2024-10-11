from copy import deepcopy
import random


class RubiksCube2x2:
    def __init__(self, cube=None):
        if cube is None:
            self.cube = {
                "U": ["W", "W", "W", "W"],  # Белая
                "D": ["Y", "Y", "Y", "Y"],  # Желтая
                "F": ["G", "G", "G", "G"],  # Зеленая
                "B": ["B", "B", "B", "B"],  # Синяя
                "R": ["R", "R", "R", "R"],  # Красная
                "L": ["O", "O", "O", "O"],  # Оранжевая
            }
        else:
            self.cube = deepcopy(cube)

    def rotate_face(self, face):
        self.cube[face] = [
            self.cube[face][2],
            self.cube[face][0],
            self.cube[face][3],
            self.cube[face][1],
        ]

    def rotate_face_prime(self, face):
        self.cube[face] = [
            self.cube[face][1],
            self.cube[face][3],
            self.cube[face][0],
            self.cube[face][2],
        ]

    def rotate(self, face, neighbors):
        self.rotate_face(face)
        temp = [self.cube[neighbors[0][0]][i] for i in neighbors[0][1]]
        for i in range(3):
            for j, pos in enumerate(neighbors[i][1]):
                self.cube[neighbors[i][0]][pos] = self.cube[neighbors[i + 1][0]][
                    neighbors[i + 1][1][j]
                ]
        for j, pos in enumerate(neighbors[3][1]):
            self.cube[neighbors[3][0]][pos] = temp[j]

    def rotate_U_prime(self):
        """Поворот верхней грани против часовой стрелки"""
        self.rotate_face_prime("U")
        (
            self.cube["R"][0],
            self.cube["R"][1],
            self.cube["B"][0],
            self.cube["B"][1],
            self.cube["L"][0],
            self.cube["L"][1],
            self.cube["F"][0],
            self.cube["F"][1],
        ) = (
            self.cube["F"][0],
            self.cube["F"][1],
            self.cube["R"][0],
            self.cube["R"][1],
            self.cube["B"][0],
            self.cube["B"][1],
            self.cube["L"][0],
            self.cube["L"][1],
        )

    def rotate_U(self):
        self.rotate_face("U")
        (
            self.cube["L"][0],
            self.cube["L"][1],
            self.cube["F"][0],
            self.cube["F"][1],
            self.cube["R"][0],
            self.cube["R"][1],
            self.cube["B"][0],
            self.cube["B"][1],
        ) = (
            self.cube["F"][0],
            self.cube["F"][1],
            self.cube["R"][0],
            self.cube["R"][1],
            self.cube["B"][0],
            self.cube["B"][1],
            self.cube["L"][0],
            self.cube["L"][1],
        )

    def rotate_D_prime(self):
        """Поворот нижней грани против часовой стрелки"""
        self.rotate_face_prime("D")
        (
            self.cube["L"][2],
            self.cube["L"][3],
            self.cube["F"][2],
            self.cube["F"][3],
            self.cube["R"][2],
            self.cube["R"][3],
            self.cube["B"][2],
            self.cube["B"][3],
        ) = (
            self.cube["F"][2],
            self.cube["F"][3],
            self.cube["R"][2],
            self.cube["R"][3],
            self.cube["B"][2],
            self.cube["B"][3],
            self.cube["L"][2],
            self.cube["L"][3],
        )

    def rotate_D(self):
        self.rotate_face("D")
        (
            self.cube["F"][2],
            self.cube["F"][3],
            self.cube["R"][2],
            self.cube["R"][3],
            self.cube["B"][2],
            self.cube["B"][3],
            self.cube["L"][2],
            self.cube["L"][3],
        ) = (
            self.cube["L"][2],
            self.cube["L"][3],
            self.cube["F"][2],
            self.cube["F"][3],
            self.cube["R"][2],
            self.cube["R"][3],
            self.cube["B"][2],
            self.cube["B"][3],
        )

    def rotate_F_prime(self):
        """Поворот передней грани против часовой стрелки"""
        self.rotate_face_prime("F")
        (
            self.cube["L"][3],
            self.cube["L"][1],
            self.cube["U"][2],
            self.cube["U"][3],
            self.cube["R"][0],
            self.cube["R"][2],
            self.cube["D"][0],
            self.cube["D"][1],
        ) = (
            self.cube["U"][2],
            self.cube["U"][3],
            self.cube["R"][0],
            self.cube["R"][2],
            self.cube["D"][1],
            self.cube["D"][0],
            self.cube["L"][1],
            self.cube["L"][3],
        )

    def rotate_F(self):
        self.rotate_face("F")
        (
            self.cube["R"][0],
            self.cube["R"][2],
            self.cube["D"][0],
            self.cube["D"][1],
            self.cube["L"][1],
            self.cube["L"][3],
            self.cube["U"][2],
            self.cube["U"][3],
        ) = (
            self.cube["U"][2],
            self.cube["U"][3],
            self.cube["R"][2],
            self.cube["R"][0],
            self.cube["D"][0],
            self.cube["D"][1],
            self.cube["L"][3],
            self.cube["L"][1],
        )

    def rotate_B_prime(self):
        """Поворот задней грани против часовой стрелки"""
        self.rotate_face_prime("B")
        (
            self.cube["U"][0],
            self.cube["U"][1],
            self.cube["R"][1],
            self.cube["R"][3],
            self.cube["D"][2],
            self.cube["D"][3],
            self.cube["L"][0],
            self.cube["L"][2],
        ) = (
            self.cube["L"][2],
            self.cube["L"][0],
            self.cube["U"][0],
            self.cube["U"][1],
            self.cube["R"][3],
            self.cube["R"][1],
            self.cube["D"][2],
            self.cube["D"][3],
        )

    def rotate_B(self):
        self.rotate_face("B")
        (
            self.cube["U"][0],
            self.cube["U"][1],
            self.cube["R"][1],
            self.cube["R"][3],
            self.cube["D"][2],
            self.cube["D"][3],
            self.cube["L"][0],
            self.cube["L"][2],
        ) = (
            self.cube["R"][1],
            self.cube["R"][3],
            self.cube["D"][3],
            self.cube["D"][2],
            self.cube["L"][0],
            self.cube["L"][2],
            self.cube["U"][1],
            self.cube["U"][0],
        )

    def rotate_R(self):
        self.rotate_face("R")
        (
            self.cube["F"][1],
            self.cube["F"][3],
            self.cube["U"][1],
            self.cube["U"][3],
            self.cube["B"][0],
            self.cube["B"][2],
            self.cube["D"][1],
            self.cube["D"][3],
        ) = (
            self.cube["D"][1],
            self.cube["D"][3],
            self.cube["F"][1],
            self.cube["F"][3],
            self.cube["U"][3],
            self.cube["U"][1],
            self.cube["B"][2],
            self.cube["B"][0],
        )

    def rotate_R_prime(self):
        """Поворот правой грани против часовой стрелки"""
        self.rotate_face_prime("R")
        (
            self.cube["F"][1],
            self.cube["F"][3],
            self.cube["U"][1],
            self.cube["U"][3],
            self.cube["B"][0],
            self.cube["B"][2],
            self.cube["D"][1],
            self.cube["D"][3],
        ) = (
            self.cube["U"][1],
            self.cube["U"][3],
            self.cube["B"][2],
            self.cube["B"][0],
            self.cube["D"][3],
            self.cube["D"][1],
            self.cube["F"][1],
            self.cube["F"][3],
        )

    def rotate_L_prime(self):
        """Поворот левой грани против часовой стрелки"""
        self.rotate_face_prime("L")
        (
            self.cube["F"][0],
            self.cube["F"][2],
            self.cube["U"][0],
            self.cube["U"][2],
            self.cube["B"][1],
            self.cube["B"][3],
            self.cube["D"][0],
            self.cube["D"][2],
        ) = (
            self.cube["D"][0],
            self.cube["D"][2],
            self.cube["F"][0],
            self.cube["F"][2],
            self.cube["U"][2],
            self.cube["U"][0],
            self.cube["B"][3],
            self.cube["B"][1],
        )

    def rotate_L(self):
        self.rotate_face("L")
        (
            self.cube["F"][0],
            self.cube["F"][2],
            self.cube["U"][0],
            self.cube["U"][2],
            self.cube["B"][1],
            self.cube["B"][3],
            self.cube["D"][0],
            self.cube["D"][2],
        ) = (
            self.cube["U"][0],
            self.cube["U"][2],
            self.cube["B"][3],
            self.cube["B"][1],
            self.cube["D"][2],
            self.cube["D"][0],
            self.cube["F"][0],
            self.cube["F"][2],
        )

    def display_cube(self):
        for face in ["U", "F", "R", "D", "L", "B"]:
            print(f"{face}: {self.cube[face]}")

    def scramble(self, moves=20):
        """Функция для случайного запутывания кубика с исключением обратных ходов"""
        faces = ["U", "D", "F", "B", "R", "L"]
        directions = [
            (self.rotate_U, "U", "U'"),
            (self.rotate_U_prime, "U'", "U"),
            (self.rotate_D, "D", "D'"),
            (self.rotate_D_prime, "D'", "D"),
            (self.rotate_F, "F", "F'"),
            (self.rotate_F_prime, "F'", "F"),
            (self.rotate_R, "R", "R'"),
            (self.rotate_R_prime, "R'", "R"),
            (self.rotate_L, "L", "L'"),
            (self.rotate_L_prime, "L'", "L"),
        ]

        last_move = None  # Переменная для хранения последнего выполненного хода
        print("Запутывание кубика:")

        for _ in range(moves):
            while True:
                move, move_name, inverse_name = random.choice(directions)
                if last_move != inverse_name:  # Проверка на обратный ход
                    print(move_name, end=" ")  # Выводим название поворота
                    move()  # Выполняем случайный ход
                    last_move = move_name  # Сохраняем последний выполненный ход
                    break

        print("\nКубик запутан.")
