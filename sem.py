from __future__ import print_function
import numpy
from scipy import optimize


class Objective(object):
    def __init__(self, n, alpha, sigma, S):
        self.n = n
        self.alpha = alpha
        self.sigma = sigma
        self.S = S

    def __call__(self, phi):
        n = self.n
        A, Sigma_e = self.make_matrix(phi)
        T = numpy.linalg.inv(numpy.identity(n) - A)
        Sigma = numpy.dot(numpy.dot(T, Sigma_e), T.T)
        e = (self.S - Sigma) * numpy.tri(n)
        e.shape = (n * n,)
        return e

    def make_matrix(self, x):
        n = self.n
        it = iter(x)
        A = numpy.zeros([n, n])
        Sigma_e = numpy.zeros([n, n])
        for i, j in self.alpha:
            A[i, j] = next(it)
        for i, j in self.sigma:
            Sigma_e[i, j] = Sigma_e[j, i] = next(it)
        return A, Sigma_e


def sem(n, alpha, sigma, S):
    obj = Objective(n, alpha, sigma, S)
    sol = optimize.leastsq(obj, [0] * (len(alpha) + len(sigma)))[0]
    A, Sigma_e = obj.make_matrix(sol)
    return A, Sigma_e


if __name__ == '__main__':
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
    A, Sigma_e = sem(3, alpha, sigma, S)
    print(A)
    print(Sigma_e)
