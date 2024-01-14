# ROS2: Humble Hawksbill

We begin by sourcing our **ROS** installation and current shared package directory.

```bash
source install/setup.bash
```
To compile the package:
1. `listen_talk_pkg`
```bash
colcon build --packages-select listen_talk_pkg
```
2. `robot`
```bash
colcon build --packages-select robot
```
