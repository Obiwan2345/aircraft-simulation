# Simulating Velocity and Take-off Distance of an Aircraft over a given time

import tkinter as tk
from tkinter import ttk
import threading
import time
import matplotlib.pyplot as plt

# constants
g = 9.81  # gravity
rho = 1.225  # air density

# Results tracker for plotting
velocities = []
times = []


def simulation():
    def run_simulation():
        global velocities, times
        velocities = []
        times = []
        try:
            # Defining user values
            mass_var = float(mass.get())
            thrust_var = float(thrust.get())
            wing_area_var = float(wing_area.get())
            C_L_var = float(C_L.get())
            C_D_var = float(C_D.get())

            # Initial values
            v = 0
            dt = 0.1  # time step (s)
            sim_time = 0  # initial time (s)
            distance = 0  # initial distance

            weight = mass_var * g
            rolling_resistance_coeff = 0.02

            # Update status
            def update_status_running():
                status_var.set("Simulation running...")
                show_page6()

            root.after(0, update_status_running)

            while True:
                # Calculate Lift and Drag
                lift = 0.5 * rho * v ** 2 * C_L_var * wing_area_var
                drag = 0.5 * rho * v ** 2 * C_D_var * wing_area_var

                # rolling resistance
                rolling_resistance = rolling_resistance_coeff * weight  # friction with runaway
                # net force and acceleration
                net_force = thrust_var - drag - rolling_resistance
                acceleration = net_force / mass_var
                # Update velocity and time and distance
                v += acceleration * dt
                sim_time += dt
                distance += v * dt

                # store data
                velocities.append(v)
                times.append(sim_time)

                # If the lift is greater than the weight, the plane will take off
                if lift >= weight:
                    result = f"Take-off at {v:.2f} m/s after {sim_time:.2f} seconds for {distance:.2f}m."

                    def update_result():
                        label_result.config(text=result)
                        status_var.set("Simulation complete")
                        show_page6()
                        show_plot()

                    root.after(0, update_result)  # ensures GUI update from thread
                    break

        except ValueError:
            def show_error():
                label_result.config(text="Please enter valid numeric values.")
                status_var.set("Error in input.")
                show_page6()
        root.after(0, show_error)

    threading.Thread(target=run_simulation).start()  # Allows the velocity_time function to run in the background


def show_plot():
    # Plot Graph
    plt.figure(figsize=(8, 5))
    plt.plot(times, velocities, label="Velocity vs Time", color='blue')
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Aircraft Acceleration to Takeoff")
    plt.grid(True)
    plt.legend()
    plt.show()


# GUI Setting
root = tk.Tk()
style = ttk.Style()
style.configure('.', font=("Segoe UI", 11))
root.title("Simulating Velocity, Time, and Distance of an Aircraft")
root.geometry("420x240")

container = ttk.Frame(root, padding=10)
container.pack(fill="both", expand=True)

page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)
page4 = ttk.Frame(container)
page5 = ttk.Frame(container)
page6 = ttk.Frame(container)

for p in (page1, page2, page3, page4, page5, page6):
    p.place(relx=0, rely=0, relwidth=1, relheight=1)  # stack pages full size


# Functions for buttons to show pages
def show_page1():
    global current_page
    current_page = 1
    page1.tkraise()


def show_page2():
    global current_page
    current_page = 2
    page2.tkraise()


def show_page3():
    global current_page
    current_page = 3
    page3.tkraise()


def show_page4():
    global current_page
    current_page = 4
    page4.tkraise()


def show_page5():
    current_page = 5
    page5.tkraise()


def show_page6():
    current_page = 6
    page6.tkraise()

    # Page 1


ttk.Label(page1, text="Enter the mass of the aircraft in kg").pack(pady=10)
mass = tk.StringVar()
ttk.Entry(page1, textvariable=mass).pack(pady=5)
ttk.Button(page1, text="Next ->", command=show_page2).pack(pady=10)

# Page 2
ttk.Label(page2, text="Enter the thrust of both engines in newtons").pack(pady=10)
thrust = tk.StringVar()
ttk.Entry(page2, textvariable=thrust).pack(pady=5)
ttk.Button(page2, text="Next ->", command=show_page3).pack(pady=10)
ttk.Button(page2, text="Back <-", command=show_page1).pack()

# Page 3
ttk.Label(page3, text="Enter the wing area of the aircraft in square metres").pack(pady=10)
wing_area = tk.StringVar()
ttk.Entry(page3, textvariable=wing_area).pack(pady=5)
ttk.Button(page3, text="Next ->", command=show_page4).pack(pady=10)
ttk.Button(page3, text="Back <-", command=show_page2).pack()

# Page 4
ttk.Label(page4, text="Enter the lift coefficient of the aircraft").pack(pady=10)
C_L = tk.StringVar()
ttk.Entry(page4, textvariable=C_L).pack(pady=5)
ttk.Button(page4, text="Next ->", command=show_page5).pack(pady=10)
ttk.Button(page4, text="Back <-", command=show_page3).pack()

# Page 5
ttk.Label(page5, text="Enter the Drag coefficient of the aircraft").pack(pady=10)
C_D = tk.StringVar()
ttk.Entry(page5, textvariable=C_D).pack(pady=5)
ttk.Button(page5, text="Result", command=simulation).pack(pady=10)
ttk.Button(page5, text="Back <-", command=show_page4).pack()

# Page 6
status_var = tk.StringVar(value="Waiting for input...")
label_result = ttk.Label(page6, text="")
label_result.pack()

ttk.Label(page6, textvariable=status_var).pack(pady=10)


# Bind Return key
def on_return_key(event=None):
    if current_page == 1:
        show_page2()
    elif current_page == 2:
        show_page3()
    elif current_page == 3:
        show_page4()
    elif current_page == 4:
        show_page5()
    elif current_page == 5:
        simulation()


root.bind("<Return>", on_return_key)

show_page1()
root.mainloop()