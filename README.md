





# FOR lerobot

activate the miniconda environment first 

```
source ~/miniconda3/bin/activate
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda create -y -n lerobot python=3.10
conda activate lerobot
```

I have CUDA 11.4 and Nvidia driver 470 , quiet old !
```
pip install --force-reinstall torch==2.0.1+cu117 torchvision==0.15.2+cu117 torchaudio==2.0.2+cu117 \
    --index-url https://download.pytorch.org/whl/cu117

```
## 🚀 TODO List

- [ ] **Codebase Cleanup**
  - Refactor and organize Python scripts
  - Clean up `CMakeLists.txt` and `package.xml`

- [ ] **Visualization & Debugging**
  - Add RViz visualization elements (robot model, sensors, trajectories, TF frames)
  - Create debug launch files for easier testing

- [ ] **Launch & Deployment**
  - Write a unified ROS2 launch file
  - Add task-specific launch configurations (simulation vs real robot)

- [ ] **C++ Implementation**
  - Write C++ equivalents of existing Python nodes
  - Ensure integration with ROS2 build system

- [ ] **Simulation Integration**
  - Get Isaac Sim ROS2 nodes up and running
  - Connect Isaac Sim ROS2 environment with `lerobot`
  - Validate simulation ↔ real-world consistency

- [ ] **Documentation**
  - Expand setup instructions (Docker/Conda/ROS2)
  - Add usage examples with demo commands
  - Link YouTube demos for quick reference


### Demo Videos
- [Issac sim UR5 robot bringup in Issac Sim ](https://youtu.be/snVbn_7Q2BU)
- [Lerobot example in Pushit GYM](https://youtu.be/INDGt76GARY)

## Repository Overview
- `Isaac_sim/` – Isaac-Sim simulator setup and ROS2 integration
- `src/` – Main application logic and ROS2 nodes
- `scripts/` – Utility and automation scripts
- `launch/` – ROS2 launch files for various scenarios
- `tasks/` – Task descriptors or charge outlines
- `CMakeLists.txt` & `package.xml` – Build configuration for ROS2
- `README.md` – This documentation
- Setup scripts (`get_lebot_running.sh`, `setup_miniconda.sh`, `start_isaac_sim_docker_with_ros2.sh`)
