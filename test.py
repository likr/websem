from __future__ import print_function
import unittest
from sem import sem


class TestSem(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_sem(self):
        alpha = [
            (1, 0),
            (2, 0),
            (2, 1),
        ]
        sigma = [
            (0, 0),
            (1, 1),
            (2, 2)
        ]
        S = [
            [54.90526316, 7.09473684, 10.36842105],
            [7.09473684, 2.74736842, 2.31578947],
            [10.36842105, 2.31578947, 4.73684211],
        ]
        A, Sigma_e, gfivalue, agfivalue = sem(3, alpha, sigma, S)
        print(A, Sigma_e, gfivalue, agfivalue)

    def test_sem_empty(self):
        alpha = [
        ]
        sigma = [
        ]
        sigma_fixed = [
            (0, 0, 1),
            (1, 1, 1),
            (2, 2, 1)
        ]
        S = [
            [54.90526316, 7.09473684, 10.36842105],
            [7.09473684, 2.74736842, 2.31578947],
            [10.36842105, 2.31578947, 4.73684211],
        ]
        A, Sigma_e, gfivalue, agfivalue = sem(3, alpha, sigma, S, [], sigma_fixed)
        print(A, Sigma_e, gfivalue, agfivalue)

    def test_sem_with_latent_variable(self):
        n = 8
        alpha = [
            (4, 6),
            (5, 6),
            (0, 7),
            (1, 7),
            (2, 7),
            (3, 7),
            (6, 7),
        ]
        sigma = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
        ]
        sigma_fixed = [
            (7, 7, 1),
        ]
        S = [
            [1, 0.770742629, 0.712859322, 0.627636537, 0.744979759, 0.818047119],
            [0.770742629, 1, 0.722799660, 0.451593348, 0.852624474, 0.671860664],
            [0.712859322, 0.722799660, 1, 0.232133405, 0.578725321, 0.478518010],
            [0.627636537, 0.451593348, 0.232133405, 1, 0.588132841, 0.609564865],
            [0.744979759, 0.852624474, 0.578725321, 0.588132841, 1, 0.752387858],
            [0.818047119, 0.671860664, 0.478518010, 0.609564865, 0.752387858, 1]
        ]

        A, Sigma_e, gfivalue, agfivalue = sem(n, alpha, sigma, S, [], sigma_fixed)
        print(A, Sigma_e, gfivalue, agfivalue)

    def test_sem_mimic(self):
        n = 7
        alpha = [
            (0, 6),
            (1, 6),
            (2, 6),
            (3, 6),
            (6, 5),
        ]
        sigma = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
            (2, 3),
            (4, 4),
            (5, 5),
            (6, 6),
        ]
        sigma_fixed = [
            (0, 0, 1),
            (1, 1, 1),
            (2, 2, 1),
            (3, 3, 1),
        ]
        alpha_fixed = [
            (6, 4, 1),
        ]
        S = [
            [1, 0.770742629, 0.712859322, 0.627636537, 0.744979759, 0.818047119],
            [0.770742629, 1, 0.722799660, 0.451593348, 0.852624474, 0.671860664],
            [0.712859322, 0.722799660, 1, 0.232133405, 0.578725321, 0.478518010],
            [0.627636537, 0.451593348, 0.232133405, 1, 0.588132841, 0.609564865],
            [0.744979759, 0.852624474, 0.578725321, 0.588132841, 1, 0.752387858],
            [0.818047119, 0.671860664, 0.478518010, 0.609564865, 0.752387858, 1]
        ]

        A, Sigma_e, gfivalue, agfivalue = sem(n, alpha, sigma, S, alpha_fixed, sigma_fixed)
        print(A, Sigma_e, gfivalue, agfivalue)


if __name__ == '__main__':
    unittest.main()
