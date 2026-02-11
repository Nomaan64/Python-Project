total_distance = 0

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    s = float(s)

    if s > 0:
        d = s * (2 / 60)   # distance in km for 2 minutes
        total_distance += d

file.close()

actual_distance = 32  # km from Google Maps

percentage_error = abs(total_distance - actual_distance) / actual_distance * 100

print("Calculated total distance (km):", round(total_distance, 2))
print("Actual distance (km):", actual_distance)
print("Percentage error (%):", round(percentage_error, 2))
