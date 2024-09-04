import matplotlib.pyplot as plt
import numpy as np

from turtle_loc_oracles.task_space import green_sea_turtle_task_space_trajectory_factory

# the spatial scaling factor
sf = 1.0
# the temporal scaling factor
sw = 1.0
# the positional offset
x_off = np.array([1.0, 1.0, 1.0])

if __name__ == "__main__":
    # call the oracle factory function
    x_fn, x_d_fn, x_dd_fn, th_fn, th_d_fn, th_dd_fn = green_sea_turtle_task_space_trajectory_factory(
        sf=sf, sw=sw, x_off=x_off
    )

    # create a vector with time stamps
    ts = np.linspace(0, 10, 1000)

    # evaluate the oracle at each time step
    # position, velocity, and acceleration
    x_ts = np.array([x_fn(t) for t in ts])
    x_d_ts = np.array([x_d_fn(t) for t in ts])
    x_dd_ts = np.array([x_dd_fn(t) for t in ts])
    # twist angle, twist angular velocity, and twist angular acceleration
    th_ts = np.array([th_fn(t) for t in ts])
    th_d_ts = np.array([th_d_fn(t) for t in ts])
    th_dd_ts = np.array([th_dd_fn(t) for t in ts])

    # plot the oracle
    dpi = 150
    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, x_ts[:, 0], label=r"$x$")
    ax.plot(ts, x_ts[:, 1], label=r"$y$")
    ax.plot(ts, x_ts[:, 2], label=r"$z$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Task space position [m]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, x_d_ts[:, 0], label=r"$\dot{x}$")
    ax.plot(ts, x_d_ts[:, 1], label=r"$\dot{y}$")
    ax.plot(ts, x_d_ts[:, 2], label=r"$\dot{z}$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Task space velocity [m/s]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, x_dd_ts[:, 0], label=r"$\ddot{x}$")
    ax.plot(ts, x_dd_ts[:, 1], label=r"$\ddot{y}$")
    ax.plot(ts, x_dd_ts[:, 2], label=r"$\ddot{z}$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel(r"Task space acceleration [m/s$^2$]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    # plot the position in 3D space with the velocity magnitude as color
    x_d_norm_ts = np.linalg.norm(x_d_ts, axis=1)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(x_ts[:, 0], x_ts[:, 1], x_ts[:, 2], c=x_d_norm_ts, cmap="coolwarm")
    fig.colorbar(sc, shrink=0.7, label=r"$|\dot{x}|_2$")
    ax.set_xlabel(r"$x$ [m]")
    ax.set_ylabel(r"$y$ [m]")
    ax.set_zlabel(r"$z$ [m]")
    ax.grid(True)
    ax.set_aspect("equal")
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, th_ts, label=r"$\theta$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Flipper twist angle [rad]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, th_d_ts, label=r"$\dot{\theta}$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Flipper twist angular velocity [rad/s]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, th_dd_ts, label=r"$\ddot{\theta}$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel(r"Flipper twist angular acceleration [rad/s$^2$]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()
