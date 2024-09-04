import matplotlib.pyplot as plt
import numpy as np

from turtle_loc_oracles.joint_space import cornelia_turtle_robot_joint_space_trajectory_factory

# the spatial scaling factor
sf = 1.0
# the temporal scaling factor
sw = 1.0
# the positional joint angle offset
q_off = np.array([0.0, 0.0, 0.0])

if __name__ == "__main__":
    # call the oracle factory function
    q_fn, q_d_fn, q_dd_fn = cornelia_turtle_robot_joint_space_trajectory_factory(
        sf=sf, sw=sw, q_off=q_off
    )

    # create a vector with time stamps
    ts = np.linspace(0, 10, 1000)

    # evaluate the oracle at each time step
    # position, velocity, and acceleration in joint space
    q_ts = np.array([q_fn(t) for t in ts])
    q_d_ts = np.array([q_d_fn(t) for t in ts])
    q_dd_ts = np.array([q_dd_fn(t) for t in ts])

    # plot the oracle
    dpi = 150
    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, q_ts[:, 0], label=r"$q_1$")
    ax.plot(ts, q_ts[:, 1], label=r"$q_2$")
    ax.plot(ts, q_ts[:, 2], label=r"$q_3$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Joint angles [rad]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(dpi=dpi)
    ax = fig.gca()
    ax.plot(ts, q_d_ts[:, 0], label=r"$\dot{q}_1$")
    ax.plot(ts, q_d_ts[:, 1], label=r"$\dot{q}_2$")
    ax.plot(ts, q_d_ts[:, 2], label=r"$\dot{q}_3$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Joint velocities [rad/s]")
    ax.legend()
    ax.grid(True)
    plt.box(True)
    plt.tight_layout()
    plt.show()

    # plot joint angles in 3D space with the velocity magnitude as color
    q_d_norm_ts = np.linalg.norm(q_d_ts, axis=1)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(q_ts[:, 0], q_ts[:, 1], q_ts[:, 2], c=q_d_norm_ts, cmap="coolwarm")
    fig.colorbar(sc, shrink=0.7, label=r"$|\dot{q}|_2$")
    ax.set_xlabel(r"$q_1$ [m]")
    ax.set_ylabel(r"$q_2$ [m]")
    ax.set_zlabel(r"$q_3$ [m]")
    ax.grid(True)
    ax.set_aspect("equal")
    plt.show()
