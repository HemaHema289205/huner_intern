# load a data set
import pandas as pd
data=pd.read_excel("C:/Users/HEMA/OneDrive/Desktop/data sets/food_coded.xlsx")

# convert some specific values to numeric
data['weight']=pd.to_numeric(data['weight'],errors='coerce')

# convert some specific rows to numeric
data["GPA"] = pd.to_numeric(data["GPA"], errors="coerce")
data["GPA"] = data["GPA"].round(1)

# replace none values
data.replace("none", pd.NA, inplace=True)

# filling null values
for column in data.columns:
    if data[column].dtype == "object":  # For categorical columns
        data[column].fillna(data[column].mode()[0], inplace=True)
    else:  # For numerical columns
        data[column].fillna(data[column].median(), inplace=True)

# droping Nan values
data.dropna(inplace=True)

# data set to save in a location
data.to_excel("C:/Users/HEMA/OneDrive/Desktop/data sets/food_code1.xlsx", index=False)  # Save cleaned dataset
