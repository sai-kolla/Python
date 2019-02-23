import pandas as pd

dataset = pd.read_csv('titanic.csv')

dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} )

print("correlation score for survived and sex is: ", dataset['Survived'].corr(dataset['Sex']))