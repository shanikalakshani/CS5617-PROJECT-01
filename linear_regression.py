import csv
import pandas as pd
import matplotlib.pyplot as plt   #Data visualisation libraries 
from sklearn.linear_model import LinearRegression

def column(matrix, i):
    return [row[i] for row in matrix]

data_set = pd.read_csv('population_by_district_in_census_years.csv')
prediction_years = pd.read_csv('prediction.csv')

data_set.head()
data_set.info()
data_set.describe()
data_set.columns

x = data_set[['Year']]
y = data_set[['Colombo','Gampaha','Kalutara','Kandy','Matale','Nuwara - Eliya','Galle','Matara','Hambantota','Jaffna','Mannar','Vavuniya','Mullaitivu','Kilinochchi','Batticaloa','Ampara','Trincomalee','Kurunagala','Puttalam','Chilaw','Anuradhapura','Polannaruwa','Badulla','Monaragala','Ratnapura','Kegalle']]

lm = LinearRegression()
lm.fit(x ,y)

predictions = lm.predict(prediction_years)


with open('population_by_district_in_census_years_predictions.csv', mode='w', newline='') as employee_file:
    output_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['Colombo','Gampaha','Kalutara','Kandy','Matale','Nuwara - Eliya','Galle','Matara','Hambantota','Jaffna','Mannar','Vavuniya','Mullaitivu','Kilinochchi','Batticaloa','Ampara','Trincomalee','Kurunagala','Puttalam','Chilaw','Anuradhapura','Polannaruwa','Badulla','Monaragala','Ratnapura','Kegalle'])
    for row in predictions:
        output_writer.writerow([row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7],row[8], row[9],row[10], row[11],row[12], row[13],row[14], row[15],row[17], row[17],row[18],row[19], row[20],row[21], row[22],row[23], row[24]])
