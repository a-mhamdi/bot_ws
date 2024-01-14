The launch file `launch_sim.launch.py` displays the robot in `gazebo` and publishes the `/robot_description` and `/scan` topics to `rviz`
```bash
ros2 launch rouebot launch_sim.launch.py
```
## Mapping using SLAM toolbox
```bash
ros2 launch rouebot launch_slam.launch.py
```
## Localization and navigation
```bash
ros2 launch rouebot launch_nav.launch.py
```

