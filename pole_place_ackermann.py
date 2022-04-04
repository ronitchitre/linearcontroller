import numpy as np

def closed_loop_poly(poles, A):
    result = np.zeros(A.shape)
    coeff = np.polynomial.polynomial.polyfromroots(poles)
    for i in range(len(coeff)):
        result = np.add(result, coeff[i]*np.linalg.matrix_power(A, i))
    return result

def controllability(m_A, m_B):
	result = np.zeros(m_A.shape)
	n = m_A.shape[0]
	for i in range(n):
		row = np.dot(np.linalg.matrix_power(m_A, i), m_B)
		result[i] = row
	return result.T

def ackermann(m_A, m_B, poles):
	closed_loop_tf_A = closed_loop_poly(poles, m_A)
	m_controllability = controllability(m_A, m_B)
	m_inv_controllability = np.linalg.inv(m_controllability)
	m_K = np.dot(m_inv_controllability, closed_loop_tf_A)
	return m_K[-1]
