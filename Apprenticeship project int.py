    # Simulating Velocity and Take-off Distance of an Aircraft over a given time
import matplotlib.pyplot as plt
#constants
g = 9.81 #gravity
rho = 1.225 #air density

# Ask User for properties of the aircraft
mass = int(input("Enter the mass of the aircraft in kg: ")) # mass in kilograms
thrust = int(input("Enter the thrust of BOTH engines in Newtons: ")) # thrust in Newtons (both engines)
wing_area = float(input("Enter the area of the wing in square metres: ")) # wing area in square metres
C_L = float(input("Enter the lift coefficient: ")) # lift coefficient during takeoff
C_D = float(input("Enter the drag coefficient: ")) # drag coefficient

# Initial Values
v = 0 # velocity in (m/s)
dt = 0.1 # time step (s)
time = 0 # initial time (s)
distance = 0 # initial distance

#Results tracker for plotting
velocities = []
times = []

while True:
     #Calculate Lift and Drag
    lift = 0.5 * rho * v**2 * C_L * wing_area
    drag = 0.5 * rho * v**2 * C_D * wing_area
    weight = mass * g

    #rolling resistance
    rolling_resistance = 0.02 * weight # friction with runaway
    #net force and acceleration
    net_force = thrust - drag - rolling_resistance
    acceleration = net_force / mass

    # Update velocity and time and distance
    v += acceleration * dt
    time += dt
    distance += v * dt

    # store data
    velocities.append(v)
    times.append(time)
     
    #If the lift is greater than the weight, the plane will take off
    if lift >= weight:
        print(f"Take-off at {v:.2f} m/s after {time:.2f} seconds.")
        print(f"Take-off distance: {distance:.2f}m")
        break
    # Check take-off distance
    if distance > 13000: #realistic runway length
        print(f"Take-off can't be accomplished as the plane travelled {distance:.2f} m, but the maximum runway length is 13000m")
        break


#Plot Graph
plt.figure(figsize=(8,5))
plt.plot(times, velocities, label="Velocity vs Time", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Aircraft Acceleration to Takeoff")
plt.grid(True)
plt.legend()
plt.show()

