import numpy as np
import matplotlib.pyplot as plt
from solver_rk4method import rk4method

class System:
    def __init__(self, A, B, K):
        self.state_trans_matrix = A
        self.control_matrix = B
        self.feedback_gain = K

    def state_equation(self):
        m_U = self.state_trans_matrix - np.dot(self.control_matrix, self.feedback_gain)

        def ode(t, x):
            return m_U.dot(x)
        return ode

    def solution(self, ic, times):
        sol = rk4method(self.state_equation(), ic, times)
        return sol


