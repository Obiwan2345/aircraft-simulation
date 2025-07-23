    #Simulating Velocity and Altitude of an Airbus A350-100 over a given time
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
altitude = 0 # altitude in (m)
dt = 0.1 # time step (s)
time = 0 # initial time (s)

#Results tracker for plotting
velocities = []
altitudes = []
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

    # Update velocity and time
    v += acceleration * dt
    time += dt

    #If the lift is greater than the weight, the plane will take off
    if lift >= weight:
        print(f"Takeoff at {v:.2f} m/s after {time:.2f} seconds.")
        break

#store data
velocities.append(v)
altitudes.append(0) #the plane is still at runaway
times.append(time)

#Plot Graph
plt.figure(figsize=(8,5))
plt.plot(times.append, velocities.append, label="Velocity vs Time", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Aircraft Acceleration to Takeoff")
plt.grid(True)
plt.legend()
plt.show()
