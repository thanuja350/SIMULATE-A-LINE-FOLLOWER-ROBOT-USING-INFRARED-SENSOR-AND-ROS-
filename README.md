# 🤖 Line Follower Robot using Infrared Sensors and ROS

## 📌 Project Overview
This project demonstrates a **Line Follower Robot** that uses **infrared (IR) sensors** to detect a black line on the floor and follow it autonomously.  
The robot is simulated using **ROS (Robot Operating System)** and can be extended to real-world applications.

The system uses **IR sensors** for line detection and a control algorithm to adjust motor speeds to keep the robot on track.

---

## ⚡ Objectives
- To design and simulate a **line-following robot** using IR sensors.  
- To implement autonomous navigation along a predefined path.  
- To integrate **sensor readings** with ROS nodes for real-time control.  
- To analyze robot behavior using **simulation tools** like Gazebo or RViz.

---

## 🛠️ Tools & Software Used
- **ROS (Robot Operating System)** – for robot simulation and communication  
- **Gazebo / RViz** – for 3D simulation and visualization  
- **Python / C++** – for writing ROS nodes  
- **Infrared sensors (IR)** – for line detection  
- **Differential drive robot model** – for movement control  

---

## 🧩 System Components
1. **Infrared Sensors**  
   - Detect line color contrast (black line on white surface)  
   - Provide digital signals (0/1) to the controller  

2. **Microcontroller / ROS Node**  
   - Reads sensor input  
   - Computes motor commands using control logic (e.g., PID or simple if-else)  

3. **Motors (Differential Drive)**  
   - Adjust speed of left and right wheels to follow the line  

4. **Simulation Environment**  
   - Gazebo or RViz for 3D simulation  
   - ROS nodes to process sensor data and send velocity commands  

---

## 🔬 Methodology
1. **Line Detection**  
   - IR sensors detect black line vs white background.  
   - Left, center, and right sensors allow detection of line position.  

2. **Control Algorithm**  
   - If the line is under the center sensor → move forward.  
   - If the line is under the left sensor → turn left.  
   - If the line is under the right sensor → turn right.  
   - If no line detected → stop or search for the line.  

3. **ROS Integration**  
   - **Publisher Node:** Sends motor commands (`/cmd_vel`)  
   - **Subscriber Node:** Reads IR sensor data (`/ir_sensor`)  
   - Simulation loop updates robot motion based on sensor feedback.  

---

## 📜 Simulation Steps
1. Install **ROS (Noetic / Melodic recommended)**.  
2. Set up a **ROS workspace**.  
3. Create a **robot model** (URDF or differential drive model).  
4. Write ROS nodes for **sensor reading** and **motor control**.  
5. Launch simulation in **Gazebo** with a line track.  
6. Observe robot following the line in real-time.  

---

## 📊 Expected Outcomes
- Robot follows a black line on a white surface autonomously.  
- Smooth movement with minimal deviation from the line.  
- Real-time visualization of sensor data and velocity commands.  
- Can be extended for multiple line patterns and intersection handling.  

---

## 🚀 Future Enhancements
- Implement **PID control** for smoother line following.  
- Integrate **camera-based line detection** for advanced paths.  
- Add **obstacle detection and avoidance** for real-world navigation.  
- Deploy on a **physical robot** with actual IR sensors and motors.  

---

## 📚 References
- ROS Wiki: [http://wiki.ros.org/](http://wiki.ros.org/)  
- Differential Drive Robot Tutorial: [http://wiki.ros.org/diff_drive](http://wiki.ros.org/diff_drive)  
- Line Follower Robot using IR Sensors: Research Papers & Tutorials  

---

