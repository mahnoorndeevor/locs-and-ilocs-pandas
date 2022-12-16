import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

mydict={'countries':names, 'driversright':dr, 'carspercap':cpc}
cars=pd.DataFrame(mydict)
print(cars)

#CSV to data frame
cars=pd.read_csv("cars.csv")
print(cars)