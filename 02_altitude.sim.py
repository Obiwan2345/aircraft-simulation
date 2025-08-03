import tkinter as tk
from tkinter import ttk
import math
import threading
import matplotlib.pyplot as plt

# Results tracker for plotting
altitudes = []
times = []

def simulation():
    def run_simulation():
        global altitudes, times
        altitudes = []
        times = []
        try:
            climb_angle_var = float(climb_angle.get())
            v_var = float(v.get())

            theta = math.radians(climb_angle_var)
            v_y = v_var * math.sin(theta)  # vertical velocity
            altitude = 0  # initial altitude before take off
            dt = 1
            time = 0

            # result tracker
            altitudes = []
            times = []

            for t in range(100):  # simulates 100 seconds
                altitude += v_y * dt
                time += dt
                altitudes.append(altitude)
                times.append(time)


            result = f"After {time:.2f}s, the plane will reach an altitude of {altitude:.2f} m"
            def update_result():
                label_result.config(text=result)
                show_page3()
                show_plot()

            root.after(0, update_result)

# Error signal
        except ValueError:
            def show_error():
                label_result.config(text="Please enter numeric values")
                show_page3()

            root.after(0, show_error)

    threading.Thread(target=run_simulation).start()  # Allows the velocity_time function to run in the background

# Plot graph
def show_plot():
    plt.figure(figsize=(8, 5))
    plt.plot(times, altitudes, label="Altitude vs Time", color="blue")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude vs Time After 100s")
    plt.grid(True)
    plt.legend()
    plt.show()


root = tk.Tk()
style = ttk.Style()
style.configure('.', font=("Segoe UI", 11))
root.title("Simulating the Altitude of an Aircraft")
root.geometry("420x240")

container = ttk.Frame(root, padding=10)
container.pack(fill="both", expand=True)

page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)

for p in (page1, page2, page3):
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

# Page 1
ttk.Label(page1, text="What's the climb angle of the aircraft in degrees").pack(pady=10)
climb_angle = tk.StringVar()
ttk.Entry(page1, textvariable=climb_angle).pack(pady=5)
ttk.Button(page1, text="Next ->", command=show_page2).pack(pady=10)

# Page 2
ttk.Label(page2, text="What is the takeoff velocity in m/s").pack(pady=10)
v = tk.StringVar()
ttk.Entry(page2, textvariable=v).pack(pady=5)
ttk.Button(page2, text="Result", command=simulation).pack(pady=10)
ttk.Button(page2, text="Back <-", command=show_page1).pack()

# Page 3 (Result page)
label_result = ttk.Label(page3, text="")
label_result.pack()

ttk.Label(page3).pack(pady=10)

# Bind Return key
def on_return_key(event=None):
    if current_page == 1:
        show_page2()
    elif current_page == 2:
        simulation()

root.bind("<Return>", on_return_key)

show_page1()
root.mainloop()
