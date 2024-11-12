import random

from collections import namedtuple
from copy import deepcopy
from enum import Flag, StrEnum
from typing import Annotated, List, Tuple


Neighbors = List[Tuple[str, List[int]]]


class Side(StrEnum):
    Up = "U"
    Down = "D"
    Front = "F"
    Back = "B"
    Right = "R"
    Left = "L"


SwapHelper = namedtuple(
    "SwapHelper", ["new_side", "new_indicies", "old_side", "old_indicies"]
)


class RubiksCube2x2:
    def __init__(self, cube=None):
        if cube is None:
            self.cube = {
                Side.Up: ["W", "W", "W", "W"],  # Белая
                Side.Down: ["Y", "Y", "Y", "Y"],  # Желтая
                Side.Front: ["G", "G", "G", "G"],  # Зеленая
                Side.Back: ["B", "B", "B", "B"],  # Синяя
                Side.Right: ["R", "R", "R", "R"],  # Красная
                Side.Left: ["O", "O", "O", "O"],  # Оранжевая
            }
        else:
            self.cube = deepcopy(cube)

    def _rotate_face(self, face: Side, clockwise: bool = True):
        if clockwise:
            self.cube[face] = [
                self.cube[face][2],
                self.cube[face][0],
                self.cube[face][3],
                self.cube[face][1],
            ]
        else:
            self.cube[face] = [
                self.cube[face][1],
                self.cube[face][3],
                self.cube[face][0],
                self.cube[face][2],
            ]

    def _swap_elements(self, mapping: Annotated[Tuple[SwapHelper], 4]):
        pair1, pair2, pair3, pair4 = mapping
        (
            self.cube[pair1.new_side][pair1.new_indicies[0]],
            self.cube[pair1.new_side][pair1.new_indicies[1]],
            self.cube[pair2.new_side][pair2.new_indicies[0]],
            self.cube[pair2.new_side][pair2.new_indicies[1]],
            self.cube[pair3.new_side][pair3.new_indicies[0]],
            self.cube[pair3.new_side][pair3.new_indicies[1]],
            self.cube[pair4.new_side][pair4.new_indicies[0]],
            self.cube[pair4.new_side][pair4.new_indicies[1]],
        ) = (
            self.cube[pair1.old_side][pair1.old_indicies[0]],
            self.cube[pair1.old_side][pair1.old_indicies[1]],
            self.cube[pair2.old_side][pair2.old_indicies[0]],
            self.cube[pair2.old_side][pair2.old_indicies[1]],
            self.cube[pair3.old_side][pair3.old_indicies[0]],
            self.cube[pair3.old_side][pair3.old_indicies[1]],
            self.cube[pair4.old_side][pair4.old_indicies[0]],
            self.cube[pair4.old_side][pair4.old_indicies[1]],
        )

    def rotate_U_prime(self):
        """Поворот верхней грани против часовой стрелки"""
        self._rotate_face(Side.Up, clockwise=False)
        (
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Back][0],
            self.cube[Side.Back][1],
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
            self.cube[Side.Front][0],
            self.cube[Side.Front][1],
        ) = (
            self.cube[Side.Front][0],
            self.cube[Side.Front][1],
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Back][0],
            self.cube[Side.Back][1],
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
        )

    def rotate_U(self):
        self._rotate_face(Side.Up)
        (
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
            self.cube[Side.Front][0],
            self.cube[Side.Front][1],
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Back][0],
            self.cube[Side.Back][1],
        ) = (
            self.cube[Side.Front][0],
            self.cube[Side.Front][1],
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Back][0],
            self.cube[Side.Back][1],
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
        )

    def rotate_D_prime(self):
        """Поворот нижней грани против часовой стрелки"""
        self._rotate_face(Side.Down, clockwise=False)
        self._swap_elements(
            (
                SwapHelper(Side.Left, (2, 3), Side.Front, (2, 3)),
                SwapHelper(Side.Front, (2, 3), Side.Right, (2, 3)),
                SwapHelper(Side.Right, (2, 3), Side.Back, (2, 3)),
                SwapHelper(Side.Back, (2, 3), Side.Left, (2, 3)),
            )
        )

    def rotate_D(self):
        self._rotate_face(Side.Down)
        self._swap_elements(
            (
                SwapHelper(Side.Front, (2, 3), Side.Left, (2, 3)),
                SwapHelper(Side.Right, (2, 3), Side.Front, (2, 3)),
                SwapHelper(Side.Back, (2, 3), Side.Right, (2, 3)),
                SwapHelper(Side.Left, (2, 3), Side.Back, (2, 3)),
            )
        )

    def rotate_F_prime(self):
        """Поворот передней грани против часовой стрелки"""
        self._rotate_face(Side.Front, clockwise=False)
        self._swap_elements(
            (
                SwapHelper(Side.Left, (3, 1), Side.Up, (2, 3)),
                SwapHelper(Side.Up, (2, 3), Side.Right, (0, 2)),
                SwapHelper(Side.Right, (0, 2), Side.Down, (1, 0)),
                SwapHelper(Side.Down, (0, 1), Side.Left, (1, 3)),
            )
        )

    def rotate_F(self):
        self._rotate_face("F")
        self._swap_elements(
            (
                SwapHelper(Side.Right, (0, 2), Side.Up, (2, 3)),
                SwapHelper(Side.Down, (0, 1), Side.Right, (2, 0)),
                SwapHelper(Side.Left, (1, 3), Side.Down, (0, 1)),
                SwapHelper(Side.Up, (2, 3), Side.Left, (3, 1)),
            )
        )

    def rotate_B_prime(self):
        """Поворот задней грани против часовой стрелки"""
        self._rotate_face(Side.Back, clockwise=False)
        self._swap_elements(
            (
                SwapHelper(Side.Up, (0, 1), Side.Left, (2, 0)),
                SwapHelper(Side.Right, (1, 3), Side.Up, (0, 1)),
                SwapHelper(Side.Down, (2, 3), Side.Right, (3, 1)),
                SwapHelper(Side.Left, (0, 2), Side.Down, (2, 3)),
            )
        )

    def rotate_B(self):
        self._rotate_face(Side.Back)
        self._swap_elements(
            (
                SwapHelper(Side.Up, (0, 1), Side.Right, (1, 3)),
                SwapHelper(Side.Right, (1, 3), Side.Down, (3, 2)),
                SwapHelper(Side.Down, (2, 3), Side.Left, (0, 2)),
                SwapHelper(Side.Left, (0, 2), Side.Up, (1, 0)),
            )
        )

    def rotate_R(self):
        self._rotate_face(Side.Right)
        self._swap_elements(
            (
                SwapHelper(Side.Front, (1, 3), Side.Down, (1, 3)),
                SwapHelper(Side.Up, (1, 3), Side.Front, (1, 3)),
                SwapHelper(Side.Back, (0, 2), Side.Up, (3, 1)),
                SwapHelper(Side.Down, (1, 3), Side.Back, (2, 0)),
            )
        )

    def rotate_R_prime(self):
        """Поворот правой грани против часовой стрелки"""
        self._rotate_face(Side.Right, clockwise=False)
        self._swap_elements(
            (
                SwapHelper(Side.Front, (1, 3), Side.Up, (1, 3)),
                SwapHelper(Side.Up, (1, 3), Side.Back, (2, 0)),
                SwapHelper(Side.Back, (0, 2), Side.Down, (3, 1)),
                SwapHelper(Side.Down, (1, 3), Side.Front, (1, 3)),
            )
        )

    def rotate_L_prime(self):
        """Поворот левой грани против часовой стрелки"""
        self._rotate_face(Side.Left, clockwise=False)
        self._swap_elements(
            (
                SwapHelper(Side.Front, (0, 2), Side.Down, (0, 2)),
                SwapHelper(Side.Up, (0, 2), Side.Front, (0, 2)),
                SwapHelper(Side.Back, (1, 3), Side.Up, (2, 0)),
                SwapHelper(Side.Down, (0, 2), Side.Back, (3, 1)),
            )
        )

    def rotate_L(self):
        self._rotate_face(Side.Left)
        self._swap_elements(
            (
                SwapHelper(Side.Front, (0, 2), Side.Up, (0, 2)),
                SwapHelper(Side.Up, (0, 2), Side.Back, (3, 1)),
                SwapHelper(Side.Back, (1, 3), Side.Down, (2, 0)),
                SwapHelper(Side.Down, (0, 2), Side.Front, (0, 2)),
            )
        )

    def rotate_X(self):
        """Поворот кубика вокруг оси X по часовой стрелке"""
        self._rotate_face(Side.Right)
        self._rotate_face(Side.Left, clockwise=False)
        # Поворот смежных граней
        (
            self.cube[Side.Up],
            self.cube[Side.Down],
            self.cube[Side.Back],
            self.cube[Side.Front],
        ) = (
            self.cube[Side.Front],
            self.cube[Side.Back][::-1],
            self.cube[Side.Up][::-1],
            self.cube[Side.Down],
        )

    def rotate_X_prime(self):
        """Поворот кубика вокруг оси X против часовой стрелке"""
        self._rotate_face(Side.Left)
        self._rotate_face(Side.Right, clockwise=False)
        # Поворот смежных граней
        (
            self.cube[Side.Up],
            self.cube[Side.Down],
            self.cube[Side.Back],
            self.cube[Side.Front],
        ) = (
            self.cube[Side.Back][::-1],
            self.cube[Side.Front],
            self.cube[Side.Down][::-1],
            self.cube[Side.Up],
        )

    def rotate_Y(self):
        """Поворот кубика вокруг оси Y по часовой стрелке"""
        self._rotate_face(Side.Up)
        self._rotate_face(Side.Down, clockwise=False)
        # Поворот смежных граней
        (
            self.cube[Side.Front],
            self.cube[Side.Right],
            self.cube[Side.Back],
            self.cube[Side.Left],
        ) = (
            self.cube[Side.Right],
            self.cube[Side.Back],
            self.cube[Side.Left],
            self.cube[Side.Front],
        )

    def rotate_Y_prime(self):
        """Поворот кубика вокруг оси Y против часовой стрелке"""
        self._rotate_face(Side.Down)
        self._rotate_face(Side.Up, clockwise=False)
        # Поворот смежных граней
        (
            self.cube[Side.Front],
            self.cube[Side.Right],
            self.cube[Side.Back],
            self.cube[Side.Left],
        ) = (
            self.cube[Side.Left],
            self.cube[Side.Front],
            self.cube[Side.Right],
            self.cube[Side.Back],
        )

    def rotate_Z(self):
        """Поворот кубика вокруг оси Z по часовой стрелке"""
        self._rotate_face(Side.Front)
        self._rotate_face(Side.Back, clockwise=False)

        # Поворот смежных граней
        (
            self.cube[Side.Up][0],
            self.cube[Side.Up][1],
            self.cube[Side.Up][2],
            self.cube[Side.Up][3],
            self.cube[Side.Down][0],
            self.cube[Side.Down][1],
            self.cube[Side.Down][2],
            self.cube[Side.Down][3],
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
            self.cube[Side.Left][2],
            self.cube[Side.Left][3],
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Right][2],
            self.cube[Side.Right][3],
        ) = (
            self.cube[Side.Left][2],
            self.cube[Side.Left][0],
            self.cube[Side.Left][3],
            self.cube[Side.Left][1],
            self.cube[Side.Right][2],
            self.cube[Side.Right][0],
            self.cube[Side.Right][3],
            self.cube[Side.Right][1],
            self.cube[Side.Down][2],
            self.cube[Side.Down][0],
            self.cube[Side.Down][3],
            self.cube[Side.Down][1],
            self.cube[Side.Up][2],
            self.cube[Side.Up][0],
            self.cube[Side.Up][3],
            self.cube[Side.Up][1],
        )

    def rotate_Z_prime(self):
        """Поворот кубика вокруг оси Z против часовой стрелке"""
        self._rotate_face(Side.Back)
        self._rotate_face(Side.Front, clockwise=False)
        # Поворот смежных граней
        (
            self.cube[Side.Up][0],
            self.cube[Side.Up][1],
            self.cube[Side.Up][2],
            self.cube[Side.Up][3],
            self.cube[Side.Down][0],
            self.cube[Side.Down][1],
            self.cube[Side.Down][2],
            self.cube[Side.Down][3],
            self.cube[Side.Left][0],
            self.cube[Side.Left][1],
            self.cube[Side.Left][2],
            self.cube[Side.Left][3],
            self.cube[Side.Right][0],
            self.cube[Side.Right][1],
            self.cube[Side.Right][2],
            self.cube[Side.Right][3],
        ) = (
            self.cube[Side.Right][1],
            self.cube[Side.Right][3],
            self.cube[Side.Right][0],
            self.cube[Side.Right][2],
            self.cube[Side.Left][1],
            self.cube[Side.Left][3],
            self.cube[Side.Left][0],
            self.cube[Side.Left][2],
            self.cube[Side.Up][1],
            self.cube[Side.Up][3],
            self.cube[Side.Up][0],
            self.cube[Side.Up][2],
            self.cube[Side.Down][1],
            self.cube[Side.Down][3],
            self.cube[Side.Down][0],
            self.cube[Side.Down][2],
        )

    def display_cube(self):
        for side in (Side.Up, Side.Front, Side.Right, Side.Down, Side.Left, Side.Back):
            print(f"{side}: {self.cube[side]}")

    def scramble(self, moves: int = 20):
        """Функция для случайного запутывания кубика с исключением обратных ходов"""
        directions = (
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
            (self.rotate_X, "X", "X'"),
            (self.rotate_X_prime, "X'", "X"),
            (self.rotate_Y, "Y", "Y'"),
            (self.rotate_Y_prime, "Y'", "Y"),
            (self.rotate_Z, "Z", "Z'"),
            (self.rotate_Z_prime, "Z'", "Z"),
            
        )

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
