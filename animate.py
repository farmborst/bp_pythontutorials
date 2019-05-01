import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



def animate(y, x1, y1, x2, y2, dt):
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
    ax.set_aspect("equal")
    plt.axis('off')
    plt.close()

    line, = ax.plot([], [], 'o-', lw=3, ms=10)
    line2, = ax.plot([], [], '-', lw=1)
    line3, = ax.plot([], [], '-', lw=1)
    time_template = '%.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


    def init():
        line.set_data([], [])
        line2.set_data([], [])
        time_text.set_text('')
        return line, time_text


    def animate(i):
        line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
        line2.set_data(x1[:i], y1[:i])
        line3.set_data(x2[:i], y2[:i])
        time_text.set_text(time_template % (i*dt))
        return line, time_text

    return animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                                  interval=25, blit=True, init_func=init)
