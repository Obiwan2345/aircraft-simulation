import math
import matplotlib.pyplot as plt

# User input
climb_angle = float(input("What is the climb angle after take off in degrees: "))
theta = math.radians(climb_angle)
v = float(input("What is the takeoff velocity in m/s: "))

v_y = v * math.sin(theta) # vertical velocity

altitude = 0 # initial altitude before take off
dt = 1
time = 0

#result tracker
altitudes = []
times = []

for t in range(100): # simulates 100 seconds
    altitude += v_y * dt
    time += dt
    #store data
    altitudes.append(altitude)
    times.append(t)
print(f"After {time:.2f}s, the altitude of the plane is {altitude:.2f} m")

# Plot Graph
plt.figure (figsize=(8,5))
plt.plot (times, altitudes, label="Velocity vs Time", color="blue" )
plt.xlabel ("Time (s)")
plt.ylabel ("Altitude (m)")
plt.title("Altitude vs Time After 100s")
plt.grid(True)
plt.legend()
plt.show()
