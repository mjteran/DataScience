height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# calculate the bmi = weight / height **2
bmi = [0, 0, 0, 0, 0]

for i in range(len(weight)):
    bmi[i] = round(weight[i] / height[i] ** 2,2)
print(bmi)

# calculate the bmi = weight / height **2
bmi2 = []

for i in range(len(weight)):
    bmi2.append(round(weight[i] / height[i] ** 2,2))
print(bmi2)

# 1D (one-dimensional) - line x or y -> list
# 2D (two-dimensional) - plane x,y -> rows and columns like a table
# 3D (three-dimensional) - space

users = [[1.73, 1.68, 1.71, 1.89, 1.79],
         [65.4, 59.2, 63.6, 88.4, 68.7]]

# 1 how to calculate bmi or user1 (index 0)
bmi_user1 = round(users[1][0] / users[0][0] ** 2,2)
print(bmi_user1)

# 2 how to calculate bmi or user2 (index 1)
bmi_user2 = round(users[1][1] / users[0][1] ** 2,2)
print(bmi_user1)

# 3 how to calculate bmi or all users: 2D list
bmi_2d = []
for i in range(len(users[0])):
    bmi_2d.append(round(users[1][i] /users[0][i]**2,2))
print(bmi_2d)

