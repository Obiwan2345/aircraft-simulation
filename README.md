This project is a simple Python simulation that models the takeoff of an Aircreft.
It calculates how long it takes for a plane to reach takeoff speed and plots the velocity against time graph.

#Feautres
- Calculates takeoff time and velocity using basic physics.
- Plots a graph of velocity vs time using matplotlib.
- Fully interactive - allows user input for plane parameters.

#How it works
- The simulation uses Newton's 2nd Law (F = m*a) to calculate the acceleration.
- It updates the velocity and time step-by-step until the aircraft reaches it's takeoff speed

#User input
When you run the program, you can enter:
- Thrust(N) - Engint force pushing the aircraft forward
- Drag(N) - Air resistance
- Mass (kg) - Mass of the AIrcraft
- Takeoff speed (m/s) - Minimum speed required for takeoff.
- Time step (s) - Accuracy of the simulation (e.g, 0.1 seconds)
  Example Output: Takeoff at 85.81 m/s after 78.90 seconds

#How to run
1. Clone this repository:
git clone https://github.com/Obiwan2345/aircraft-simulation.git
2. Install required library
pip install matplotlib
3.Run the simulation
Python takeoff_simulation.py
