import numpy as np
#
# x1 = np.array([-1.0, -1.0])
# x2 = np.array([1.0, 0.0])
# x3 = np.array([-1.0, 10])
#
# y1 = 1
# y2 = -1
# y3 = 1
#
# # start with i = 1
# print('i = 1')
# theta = np.array([0.0, 0.0])
#
# perc = y1*(np.matmul(np.transpose(theta), x1))
#
# print(perc)
#
# theta += y1*x1
#
# print(theta)
#
# perc = y2*(np.matmul(np.transpose(theta), x2))
#
# print(perc)
#
# perc = y3*(np.matmul(np.transpose(theta), x3))
#
# print(perc)
#
# theta += y3*x3
#
# print(theta)
#
# perc = y3*(np.matmul(np.transpose(theta), x3))
#
# print(perc)
#
# # start with i = 2
# print('i = 2')
# theta = np.array([0.0, 0.0])
#
# perc = y2*(np.matmul(np.transpose(theta), x2))
#
# print(perc)
#
# theta += y2*x2
#
# print(theta)
#
# perc = y3*(np.matmul(np.transpose(theta), x3))
#
# print(perc)
#
# perc = y1*(np.matmul(np.transpose(theta), x1))
#
# print(perc)

# iteratable
x_order = np.array([[-1.0, -1.0],
              [1.0, 0.0],
              [-1.0, 10]])
x_nonorder = np.array([[1.0, 0.0],
              [-1.0, 10],
              [-1.0, -1.0]])
y = np.array([1.0, -1.0, 1.0])
theta1 = np.array([0.0, 0.0])
theta2 = np.array([0.0, 0.0])

mistake1 = 0
errors1 = []
mistake2 = 0
errors2 = []

print("~~~~~~start with x1~~~~~~")
for t in range(7):
    for i in range(3):
        print("i=", i)
        print("theta1=", theta1)
        perc1 = y[i]*(np.matmul(np.transpose(theta1), x_order[i]))
        print("perc1=", perc1)
        if perc1 <= 0:
            theta1 +=y[i]*x_order[i]
            errors1.append(theta1)
            mistake1 += 1
print("mistake1 =", mistake1)
print(errors1)

print("~~~~~~start with x2~~~~~~~")
for t in range(7):
    for i in range(3):
        print("i=", i)
        print("theta2=", theta2)
        perc2 = y[i]*(np.matmul(np.transpose(theta2), x_nonorder[i]))
        print("perc2=", perc2)
        if perc2 <= 0:
            theta2 +=y[i]*x_nonorder[i]
            errors2.append(theta2)
            mistake2 += 1
print("mistake2 =", mistake2)
print(errors2)
