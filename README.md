We begin by sourcing our **ROS** installation and current shared package directory.
```bash
source install/setup.bash
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

