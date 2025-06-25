# load the data set
import pandas as pd
df = pd.read_excel("C:/Users/HEMA/OneDrive/Desktop/hema/college/internship/huner_intern/task3/breast_cancer(1).xlsx")

df=df.drop(columns = ['id'])

df['diagnosis']=df['diagnosis'].map({'M':0,'B':1})

# Split features and target
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size = 0.2 , random_state =42)

# Choose k (you can tune this)
from sklearn.neighbors import KNeighborsClassifier
k = 5
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model
knn.fit(X_train, y_train)

# Predict on test set
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

y_pred = knn.predict(X_test)

# Evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
