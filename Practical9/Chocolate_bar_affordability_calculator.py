# define total money and the price
# caculate bars by total money//price and changes by %
def chocolate_bars(total_money,price):
    bars=total_money//price
    changes=total_money%price
    return print('The number of bars affordable is {0}. The change left is {1}.'.format(bars,changes))
### an example
chocolate_bars(100,7)
