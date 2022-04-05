from main import *
# Angular velocity of target
OMEGA = 1

# State transition matrix
m_A = np.array(
    [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2 * OMEGA],
     [0, -1 * OMEGA * OMEGA, 0, 0, 0, 0],
     [0, 0, 3 * OMEGA * OMEGA, -1 * 2 * OMEGA, 0, 0]])
# Control matrix
m_B = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
# Feedback Gain
m_K = np.array([[30, 0, 0, 11, 0, 2], [0, 5, 0, 0, 5, 0], [0, 0, 7, -2, 0, 5]])


hill_equation = System(m_A, m_B, m_K)


ic = np.array([1, 1, 1, 1, 1, 1])
times = np.linspace(0, 10, 100)
sol = hill_equation.solution(ic, times)


# Plotting
sx, sy, sz, sx_dot, sy_dot, sz_dot = sol.T

fig, axs = plt.subplots(2)
fig.suptitle('Plots')
axs[0].plot(times, sx)
axs[0].plot(times, sy)
axs[0].plot(times, sz)
axs[0].legend(['x', 'y', 'z'])
axs[0].set_title('Position')

axs[1].plot(times, sx_dot)
axs[1].plot(times, sy_dot)
axs[1].plot(times, sz_dot)
axs[1].legend(['x_dot', 'y_dot', 'z_dot'])
axs[1].set_title('velocity')
# plt.savefig('plots.png')
plt.show()