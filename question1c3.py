import math

actual_speed = []
calculated_speed = []
absolute_error = []

file = open("speed_data.txt", "r")

for line in file:
    t, s = line.split()
    s = float(s)

    if s > 0:
        # distance covered in 2 minutes
        distance = s * (2 / 60)

        # calculate speed back from distance
        v_calc = distance / (2 / 60)

        actual_speed.append(s)
        calculated_speed.append(v_calc)

        absolute_error.append(abs(v_calc - s))

file.close()

# Mean Error
mean_error = sum(absolute_error) / len(absolute_error)

# RMSE
rmse = math.sqrt(sum(e**2 for e in absolute_error) / len(absolute_error))

print("Mean Absolute Error (km/h):", round(mean_error, 3))
print("RMSE (km/h):", round(rmse, 3))
