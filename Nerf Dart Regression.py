import numpy as np
import matplotlib.pyplot as plt

# Scope

#Angle	Average
#-40	61
#-30	116
#-20	177.3333333
#-10	246
#0	296.3333333
#10	539.6666667
#20	680.3333333
#30	733.6666667
#40	651
#50	652
#60	534.6666667
#70	303.6666667
#80	24.66666667
#90	0

#Points
x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177.333333, 296.333333, 680.333333, 651, 534.666667, 24.666667]

#Coefficients
result = np.polyfit(x, y, 2)
print(result)

#Equation
eq = np.poly1d(result)
print(eq)

# Input degree
degree = input("Please enter a degree value. ")
print ("The nerf dart will travel approximately...")
print (eq(degree))
print ("inches")

# Get values
x2 = np.arange(-40, 90)
yfit = np.polyval(result, x2)

# Name Lines
line1, = plt.plot(x, y, label='Points')
line2, = plt.plot(x2, yfit, label='Fit')

# Legend
plt.legend(handles=[line1,line2])

# Create Graph
plt.savefig('Nerf Dart Regression Graph.png')