# load the dataset
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel("C:/Users/HEMA/OneDrive/Desktop/hema/college/internship/huner_intern/task2/house_price_data(1).xlsx")

# Remove null values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# drop unneccesary columns
data=df.drop(columns=['date','street','city','statezip','country'],errors='ignore')


from sklearn.model_selection import train_test_split
X=data.drop('price',axis=1)
y=data['price']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train, y_train)

print(model.predict([[4,2.50,1940,10500,3.0,0,0,4,1143,800,1976,1992]]))
