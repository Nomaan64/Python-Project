import matplotlib.pyplot as plt

time = []
speed = []

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    time.append(float(t))
    speed.append(float(s))

file.close()

acceleration = []
time_acc = []

for i in range(1, len(speed)):
    a = (speed[i] - speed[i-1]) / (time[i] - time[i-1])
    acceleration.append(a)
    time_acc.append(time[i])

plt.plot(time_acc, acceleration)
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per min)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.show()
