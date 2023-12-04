We begin by checking which shell we are using on `Linux`:
```bash
which $SHELL
```
Sourcing our **ROS** installation.
```bash
source /opt/ros/humble/setup.bash
```
The launch file `launch_sim.launch.py` displays the robot in `gazebo` and publish the `/robot_description` and `/scan` topics to `rviz`
```bash
ros2 launch roue_bot launch_sim.launch.py
```
## SLAM
```bash
ros2 launch roue_bot launch_slam.launch.py
```
## Navigation
```bash
ros2 launch roue_bot launch_nav.launch.py
```

