import matplotlib.pyplot as plt

time = []
speed = []

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    time.append(float(t))
    speed.append(float(s))

file.close()

plt.plot(time, speed)
plt.xlabel("Time (minutes)")
plt.ylabel("Speed (km/h)")
plt.title("Speed vs Time Graph")
plt.grid(True)
plt.show()
