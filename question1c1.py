import matplotlib.pyplot as plt

time_mid = []
distance_2min = []

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    t = float(t)
    s = float(s)

    if s > 0:
        d = s * (2 / 60)   # distance in km for 2 minutes
        time_mid.append(t + 1)  # midpoint of 2 min interval
        distance_2min.append(d)

file.close()

plt.bar(time_mid, distance_2min)
plt.xlabel("Time (minutes)")
plt.ylabel("Distance covered in 2 minutes (km)")
plt.title("Distance Covered Every 2 Minutes")
plt.grid(True)
plt.show()
