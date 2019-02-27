#
# PUT YOUR NAME HERE
#

# add appropriate imports here

t_init = 0
t_end = 10
N_times = 1000

time = np.linspace(t_init, t_end, num=N_times)

# So that we can multiply the array of times by two dimensinoal vectors
# later.
time = time.reshape(N_times, 1)


def plot_motion_of_masses(x, time, title='bad title'):
    """
    Function to make a plot of motion of masses as a function of time. The time
    should be on the vertical axis and the position on the horizontal axis.

    Parameters
    ----------

    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] is the position of mass
        1 relative to equilibrium and x[:, 1] is the position of mass 2.

    time : array of times
        Times at which the positions have been calculated.

    title : str
        A descriptive title for the plot to make grading easier.
    """
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 3
    x2_equilibrium_pos = 6

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)


## YOU FILL IN THE REST!

