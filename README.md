# ROS2: Humble Hawksbill

To get things rolling, give this file a look at first: [https://gist.github.com/a-mhamdi/5793a17dcdf784da8b01e1847f6f7d1d](https://gist.github.com/a-mhamdi/5793a17dcdf784da8b01e1847f6f7d1d)

Source the **ROS** installation and current shared package directory.

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
