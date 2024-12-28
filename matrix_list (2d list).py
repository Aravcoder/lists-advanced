matrix_list=[ [1,3,7,9,11] , [2,4] , [3,5] ]
# print(matrix_list)

# print(len(matrix_list))

# print((matrix_list[2][1]))

matrix = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], end = " , ")
    print("\n")

# rows = int(input("How many rows do you want ? "))
# columns = int(input("How many columns do you want ? "))

# matrix = []
# for i in range(rows):
#     temp = []
#     for j in range(columns):
#         x = int(input("Enter your element - "))
#         temp.append(x)
#     print("\n")
#     matrix.append(temp)

# for i in range(rows):
#     for j in range(columns):
#         print(matrix[i][j], end = " ")
#     print("\n")

n=int(input("Enter the dimensions"))
matrix = []
for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    print("\n")
    matrix.append(temp)


for i in range(n):
    print(matrix[i][i])
    