import matplotlib.pyplot as plt

time = []
speed = []

# Read speed data
file = open("speed_data.txt", "r")
for line in file:
    t, s = line.split()
    time.append(float(t))
    speed.append(float(s))
file.close()

# Calculate acceleration
acceleration = []
time_acc = []

for i in range(1, len(speed)):
    a = (speed[i] - speed[i-1]) / (time[i] - time[i-1])
    acceleration.append(a)
    time_acc.append(time[i])

# Calculate jerk
jerk = []
time_jerk = []

for i in range(1, len(acceleration)):
    j = (acceleration[i] - acceleration[i-1]) / (time_acc[i] - time_acc[i-1])
    jerk.append(j)
    time_jerk.append(time_acc[i])

# Plot jerk vs time
plt.plot(time_jerk, jerk)
plt.xlabel("Time (minutes)")
plt.ylabel("Jerk (km/h per min²)")
plt.title("Jerk vs Time")
plt.grid(True)
plt.show()
