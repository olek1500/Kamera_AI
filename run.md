# 🚀 Running YOLOv8n on OAK-D Pro (ROS 2)

This guide explains how to run the YOLOv8n object detection model on the Luxonis OAK-D Pro camera using the `depthai_ros_driver`.

---

## 📋 Prerequisites

1.  **Hardware:** Your OAK-D Pro camera must be plugged into the computer.
2.  **ROS 2:** You must have ROS 2 and the `depthai-ros` driver installed.
3.  **Project Files:** This directory (`Kamera_A`) must contain the following files:
    * `yolo_parameters.yaml` (This is the main configuration file)
    * `yolov8n.blob` (The compiled neural network model)
    * `yolov8n.json` (The model's configuration file)

---

## ⚡ How to Run

1.  **Open a Terminal**
    Open a new terminal window.

2.  **Source your ROS 2 Workspace**
    You must source your ROS 2 environment. (Adjust the path if your workspace is named differently).
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

3.  **Launch the Camera Node**
    Run the `depthai_ros_driver` launch file. The `params_file` argument tells it to load your specific YOLO configuration.

    **Important:** This command uses the absolute path from your screenshot.
    ```bash
    ros2 launch depthai_ros_driver camera.launch.py params_file:="/home/oleeek/Kamera_A/yolo_parameters.yaml"
    ```

That's it! The node will start, load the `yolov8n.blob` onto the camera, and begin publishing the results.

---

## ✅ How to Verify it's Working

Open a **new terminal** (and source ROS 2 again) to check the output.

### 1. Check Topics (Simple)

List all active ROS topics. You should see new topics from the camera, especially those related to the neural network (like `/oak/nn/spatial_detections`).

```bash
ros2 topic list
