# Turtle Locomotion Oracles

This Python package contains oracles of the movement of turtle limbs during locomotion (e.g., swimming /)
Some oracles are based on real-world observations of turtle locomotion, while others are based on theoretical/template models.

## Installation

Installation is very easy:

Either just clone the repository and install the package (in ediatble mode) using pip.

```bash
pip install -e .
```

or install the package directly from PyPI:

```bash
pip install turtle-loc-oracles
```

## Usage
We take a functional programming approach in this package. Here, is a simple example how the
oracle motion functions can be constructed with the provided factory functions.

```python
import numpy as np
from turtle_loc_oracles.task_space import green_sea_turtle_task_space_trajectory_factory

# the spatial scaling factor
sf = 1.0
# the temporal scaling factor
sw = 1.0
# the positional offset
x_off = np.array([1.0, 1.0, 1.0])

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
```

More examples can be found in the `examples` directory.

## Provided Oracles

### Joint-space Oracles

#### Cornelia Turtle Robot Joint Space Trajectory

This oracle provides a joint-space trajectory developed for the Cornelia turtle robot by (van der Geest et al., 2023).
Please refer to the original paper for more information: https://doi.org/10.1038/s41598-023-37904-5

> van der Geest, N., Garcia, L., Borret, F., Nates, R., & Gonzalez, A. (2023).
Soft-robotic green sea turtle (Chelonia mydas) developed to replace animal experimentation provides new insight
into their propulsive strategies. Scientific Reports, 13(1), 11983.

and cite it if you use this oracle in your research.

```bibtex
@article{van2023soft,
  title={Soft-robotic green sea turtle (Chelonia mydas) developed to replace animal experimentation provides new insight into their propulsive strategies},
  author={van der Geest, Nick and Garcia, Lorenzo and Borret, Fraser and Nates, Roy and Gonzalez, Alberto},
  journal={Scientific Reports},
  volume={13},
  number={1},
  pages={11983},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

### Task-space Oracles

#### Green Sea Turtle Swimming Task Space Trajectory

This oracle provides a task-space trajectory that was fitted to video recordings of the swimming of Green sea turtles (van der Geest et al., 2022).
Please refer to the original paper for more information: https://doi.org/10.1038/s41598-022-21459-y

> van der Geest, N., Garcia, L., Nates, R., & Godoy, D. A. (2022).
New insight into the swimming kinematics of wild Green sea turtles (Chelonia mydas).
Scientific Reports, 12(1), 18151.

and cite it if you use this oracle in your research.

```bibtex
@article{van2022new,
  title={New insight into the swimming kinematics of wild Green sea turtles (Chelonia mydas)},
  author={van der Geest, Nick and Garcia, Lorenzo and Nates, Roy and Godoy, Daniel A},
  journal={Scientific Reports},
  volume={12},
  number={1},
  pages={18151},
  year={2022},
  publisher={Nature Publishing Group UK London}
}
```
