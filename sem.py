from __future__ import print_function
from __future__ import division
import numpy
from scipy import optimize


class Objective(object):
    def __init__(self, n, alpha, sigma, S, alpha_fixed, sigma_fixed):
        self.n = n
        self.alpha = alpha
        self.sigma = sigma
        self.S = S
        self.alpha_fixed = alpha_fixed
        self.sigma_fixed = sigma_fixed

    def __call__(self, phi):
        n_v = len(self.S)
        A, Sigma_e = self.make_matrix(phi)
        Sigma = self.Sigma(A, Sigma_e)
        e = (self.S - Sigma) * numpy.tri(n_v)
        e.shape = (n_v * n_v,)
        return e

    def make_matrix(self, x):
        n = self.n
        it = iter(x)
        A = numpy.zeros([n, n])
        Sigma_e = numpy.zeros([n, n])
        for i, j in self.alpha:
            A[i, j] = next(it)
        for i, j, val in self.alpha_fixed:
            A[i, j] = val
        for i, j in self.sigma:
            Sigma_e[i, j] = Sigma_e[j, i] = next(it)
        for i, j, val in self.sigma_fixed:
            Sigma_e[i, j] = Sigma_e[j, i] = val
        return A, Sigma_e

    def Sigma(self, A, Sigma_e):
        n_v = len(self.S)
        I = numpy.identity(self.n)
        U = numpy.zeros((n_v, self.n))
        U[:, :n_v] = numpy.identity(n_v)
        T = numpy.linalg.inv(I - A)
        return numpy.dot(
            numpy.dot(
                numpy.dot(
                    numpy.dot(U, T),
                    Sigma_e),
                T.T),
            U.T)


def gfi(Sigma, S):
    n = len(Sigma)
    I = numpy.identity(n)
    SigmaInv = numpy.linalg.inv(Sigma)
    SigmaS = numpy.dot(SigmaInv, S)
    denom = numpy.trace(numpy.dot(SigmaS, SigmaS.T))
    numer = numpy.trace(numpy.dot(SigmaS - I, (SigmaS - I).T))
    return 1 - numer / denom


def sem(n, alpha, sigma, S, alpha_fixed=None, sigma_fixed=None):
    if alpha_fixed is None:
        alpha_fixed = []
    if sigma_fixed is None:
        sigma_fixed = []
    x0 = numpy.ones(len(alpha) + len(sigma)) / 10
    obj = Objective(n, alpha, sigma, S, alpha_fixed, sigma_fixed)
    if len(x0) > 0:
        sol = optimize.leastsq(obj, x0)[0]
        A, Sigma_e = obj.make_matrix(sol)
    else:
        A, Sigma_e = obj.make_matrix(x0)
    Sigma = obj.Sigma(A, Sigma_e)
    return A, Sigma_e, gfi(Sigma, S)
