# import related python repository
# define x as paternal age, y as risk for (CHD)congenital heart disease
# determine the type of form and command it to draw
# run
import matplotlib.pyplot as plt
x = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
y = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
plt.scatter(x, y, marker='o')
plt.show()
my_dict={}
# To find y corresponding with x, the list should be changed into dictionary
# As I don't know the formula to do this, I type by my hands.
a={30:1.03, 35:1.07, 40:1.11, 45:1.17, 50:1.23, 55:1.32, 60:1.42, 65:1.55, 70:1.72, 75:1.94}
# Then I got the command "dict(zip())" from my friend Zhu, HengYu. By typing zip(a,b), a is a list, b is a list. It will
# generate a dictionary with the least length of the list. zip() connects a and b, dict() change it into a dictionary.
b=dict(zip(x,y))
# type the value in x into b[ ] below to get the y
print(b[40])

