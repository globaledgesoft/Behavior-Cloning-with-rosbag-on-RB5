# Behavior-Cloning-with-rosbag-on-RB5
This project is demonstrated to showcase the capabilities of RB5 platform of Qualcomm for performing the ROSBAG recording &amp; Playback. 

## Prerequisites  

1. A Linux host system with Ubuntu 18.04. 
2. Install Android Platform tools (ADB, Fastboot)  
3. Download and install the SDK Manager for RB5 
4. Flash the RB5 firmware image on to the RB5 
5. Setup the Network on RB5. 
6. Installed Python3.6 on RB5 
7. TurtleBot burger is assembled, operational, connected to RB5. 
8. Setup ROS2-Dashing on RB5. 

 
## Steps to Setup the Project on RB5 

### Installing Dependencies      

- Installation of TurtleBot3 Package:

    For the setup, we will be using the TurtleBot3 Burger, we need to install TurtleBot Packages for controlling the TurtleBot. 

    1. Setup the necessary packages by executing the following commands. 
        ```sh
        sh4.4 #sudo apt install python3-argcomplete python3-colcon-common-extensions libboost-system-dev build-essential
        ```
    2. Create a new directory for TurtleBot 3. 
        ```sh
        sh4.4 # mkdir -p ~/turtlebot3_ws/src  
        sh4.4 # cd ~/turtlebot3_ws/src 
        ```

    3. Clone the necessary repositories and then access TurtleBot Folder 
        ```sh
        sh4.4 # git clone -b dashing-devel https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git 

        sh4.4 # git clone -b dashing-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git  

        sh4.4 # git clone -b dashing-devel https://github.com/ROBOTIS-GIT/turtlebot3.git 

        sh4.4 #git clone -b dashing-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git 

        sh4.4 # cd ~/turtlebot3_ws/src/turtlebot3   
        ```

    4. Remove the folders that are not required for current project 
        ```sh
        sh4.4 # rm -r turtlebot3_cartographer turtlebot3_navigation2 
        sh4.4 # cd ~/turtlebot3_ws/ 
        ```
    5. Source & Build the TurtleBot3 Setup file 
        ```sh
        sh4.4 # echo 'source /opt/ros/dashing/setup.bash' >> ~/.bashrc 

        sh4.4 # source ~/.bashrc 

        sh4.4 # colcon build --symlink-install --parallel-workers 1 

        sh4.4 # echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc 

        sh4.4 # source ~/.bashrc 

        sh4.4 # echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc 

        sh4.4 # echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc 

        sh4.4 # source ~/.bashrc 
        ```

- Steps to setup LiDAR: 

    1. Connect LIDAR Scanner to RB5 board using a micro-USB cable. 

    2. After connection makes sure the /dev/ttyUSB0 port is accessible. 

### Environment setup instructions before running the application: 

1. In the terminal-1 run the TurtleBot Bringup Command 
    ```sh
    sh4.4 # ros2 launch turtlebot3_bringup robot.launch.py 
    ```
2. Open a second terminal, and we can launch our application from that. If you are using adb shell, don’t miss to source before running the application. 
    ```sh
    sh4.4 #  source ~/.bashrc  
    ```

3. Go to the <PROJECT_PATH> 
    ```sh
    sh4.4 # cd <PROJECT_PATH>/ 
    ```
 
4. Run the rosbag_record.py to record the ROS Topics 
    ```sh
    sh4.4 # python3 rosbag_record.py 
    ```

5. Run the rosbag_play.py to play the ROS Topics 
    ```sh
    sh4.4 # python3 rosbag_play.py 
    ```
