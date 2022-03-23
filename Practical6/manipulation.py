# find the marks of Rob and list them
# print as a sorted order
# import repository and draw a boxplot
# run and check
# find the number of the elements and sum of them
# calculate the mean of the marks
# compare it with 60 and conclude
marks=[45,36,86,57,53,92,65,45]
marks.sort()
print(marks)

import matplotlib.pyplot as plt
plt.boxplot(marks,
            vert=True,
            whis=1.5,widths=0.8,
            meanline=False,
            patch_artist=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch= False,labels=None,)
# vert accept boolean, deciding direction. widths: widths, default=0.5
# change 'notch' will make the shape interesting
plt.show()
num=0
for i in range(len(marks)):
    num += 1
sum=0
for i in marks:
    sum += i
mean=sum/num
if mean > 60:
    print("Congratulations Rob! You made it!")
else:
    print("Unfortunately, I think Rob needs someone to comfort him now.")
# From my friend Zhu, HengYu I knew np.average, which is used to get the mean of marks
import numpy as np
print(np.average(marks))
