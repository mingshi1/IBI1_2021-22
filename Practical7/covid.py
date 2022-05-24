# import a dataset. os allow us to work with files or dictionary.
# matplotlib: offer figures. numpy: mathematical tools. pandas: working with dataframes.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change to where full_data.csv is
os.chdir("C:/Users/dream/IBI1_2021-22/Practical7")
# show where am I
print('os.getcwd()', os.getcwd())
# show what here is
print('os.listdir()', os.listdir())
# use pandas to read full_data.csv and name it as covid_data here
covid_data = pd.read_csv("full_data.csv")
# show the first 5 lines of the covid_data
print('covid_data.head(5)\n', covid_data.head(5))
# give the detailed information of the covid_data
print('covid_data.info()\n', covid_data.info())
# describe detailed data analysis of each column
print('covid_data.describe()\n', covid_data.describe())
# answer:
# new_cases: mean: 194.546773        SD: 2083.395028
# total_cases: min: 0.000000        max: 777798.000000
# show content in (3,5)
print('covid_data.iloc[3,5]\n', covid_data.iloc[3, 5])
# respectively show part of rows or columns
print('covid_data.iloc[2,0:5]\n', covid_data.iloc[2, 0:5])
print('covid_data.iloc[0:2,:]\n', covid_data.iloc[0:2, :])
print('covid_data.iloc[0:10:2,0:5]\n', covid_data.iloc[0:10:2, 0:5])
# for rows, show 10~20. for columns, show the first, third
print('covid_data.iloc[10:20,[0,2]]\n', covid_data.iloc[10:20, [0, 2]])
# use the boolean to realize the same function
my_columns = [True, True, False, True, False, False]
print('covid_data.iloc[0:3,my_columns]\n', covid_data.iloc[0:3, my_columns])
# if the number of boolean (my_column here) != the number of columns. An error occurred and can't run.
# list the 3rd to 5th things in column "date"
print('covid_data.loc[2:4,"date"]\n', covid_data.loc[2:4, "date"])
print('covid_data.loc[0:81,"total_cases"]\n', covid_data.loc[0:81, "total_cases"])
# find i corresponding with 'Afghanistan', output each i's 'total_cases' in a total way.
A = []
for i in range(len(covid_data.location)):
    if covid_data.loc[i, 'location'] == 'Afghanistan':
        A.append(i)
    else:
        A.append(False)
print(covid_data.loc[A, 'total_cases'])
# with comparison, 2 results are same.
# use the same way to find China's data
a = []
for i in range(len(covid_data.location)):
    if covid_data.loc[i, 'location'] == 'China':
        column = [True, False, True, True, False, False]
        a.append(i)
china_data = covid_data.loc[a, column]
print('china_data\n', china_data)
# use 'describe' to see means, SDs and so on.
print('china_data.describe()\n', china_data.describe())
# use numpy to get the mean of new_cases and new_deaths
print('np.mean(china_data.new_cases\n', np.mean(china_data.new_cases), '\nnp.average(china_data.new_deaths)\n',
      np.average(china_data.new_deaths))
# the mean of new cases and new deaths in China are different. It means the mortality of the COVID_19 is not 100%
print('The proportion of new cases that kill the infected person is ',
      np.average(china_data.new_deaths) / np.mean(china_data.new_cases))
# draw a boxplot of the china_data
new_cases=china_data.iloc[0:,1]
new_deaths=china_data.iloc[0:,2]
china=pd.DataFrame({'china_new_cases':new_cases,'china_new_deaths':new_deaths})
plt.ylabel('number')
plt.title('China new cases and deaths')
plt.boxplot(x=china.values,
            vert=True,
            whis=1, widths=0.6,
            meanline=False,
            patch_artist=True,
            showbox=True,
            showcaps=True,
            showfliers=False,
            notch=False, labels=china.columns)

plt.show()
# from the boxplot, we can confirm that what we know fits with the mean values
plt.plot(china_data.date, china_data.new_cases, 'bo',)
plt.plot(china_data.date, china_data.new_deaths, 'r+',)
# '+'/'o' represents the shape of the point. 'r'/'b' represent the color. 'r' is red while 'b' is blue.
china_dates=china_data.date
plt.ylabel('number of cases')
plt.xlabel('date')
plt.title('variation of cases and deaths with dates')
plt.xticks(china_dates.iloc[0:len(china_dates):9],rotation=30,fontsize=8)
plt.legend(bbox_to_anchor=(1,1),
                 loc="upper right",
                 ncol=1,
                 mode="None",
                 borderaxespad=0,
                 title="red: china new deaths\nblue: china new cases",
                 shadow=False,
                 fancybox=True)
# 'xticks' command shows date selectively, 'rotation' set the angle date rotates
plt.show()
####################################################################################
# answer the question in the question.txt
# find the total cases of South Korea, Kenya, and Colombia
# form the data into 3 arrays
# plot them with different colors
South_Korea=[]
Kenya=[]
Colombia=[]
for i in range(len(covid_data.location)):
    if covid_data.loc[i, 'location'] == 'South Korea':
        South_Korea.append(i)
    elif  covid_data.loc[i, 'location'] == 'Kenya':
        Kenya.append(i)
    elif covid_data.loc[i, 'location'] == 'Colombia':
        Colombia.append(i)
    else:
        A.append(False)
SK=covid_data.iloc[South_Korea, [0,4]]
K=covid_data.iloc[Kenya, [0,4]]
C=covid_data.iloc[Colombia, [0,4]]
plt.plot(SK.date, SK.total_cases, 'bo',)
plt.plot(K.date, K.total_cases, 'rv',)
plt.plot(C.date, C.total_cases, 'g+',)
# '+'/'o'/'v' represents the shape of the point. 'r'/'b'/'g' represent the color. 'r' is red while 'b' is blue.
dates=SK.date
plt.ylabel('number of total cases')
plt.xlabel('date')
plt.title('total cases of South Korea, Kenya, and Colombia')
# plt.xticks(SK.iloc[0:len(SK.date):9],rotation=20)
plt.xticks(dates.iloc[0:len(china_dates):5],rotation=30,fontsize=8)
# 'xticks' command shows date selectively, 'rotation' set the angle date rotates
plt.legend(bbox_to_anchor=(1,1),
                 loc="upper right",
                 ncol=1,
                 mode="None",
                 borderaxespad=0,
                 title="red: Kenya\nblue: South Korea\ngreen: Colombia",
                 shadow=False,
                 fancybox=True)
plt.show()
print('for the figure 3, blue = South_Korea, red = Kenya, green = Colombia')