import matplotlib.pyplot as plt

time = []
time_for_32km = []

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    t = float(t)
    s = float(s)

    if s > 0:   # skip zero speed
        travel_time = (32 / s) * 60   # minutes
        time.append(t)
        time_for_32km.append(travel_time)

file.close()

plt.plot(time, time_for_32km)
plt.xlabel("Time of journey (minutes)")
plt.ylabel("Time to travel 32 km (minutes)")
plt.title("Instantaneous Time to Travel 32 km vs Time")
plt.grid(True)
plt.show()
