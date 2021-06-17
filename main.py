import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pandas.read_csv("iphone_price.csv")
model =LinearRegression()
model.fit(data[['version']],data[['price']])
#2d array ,It is a simple linear regression model to predict the price using two parameters
print(model.predict([[14]]))
print(model.predict([[30]]))
