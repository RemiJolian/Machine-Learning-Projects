import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle
import os
import shutil
import mlflow

## When using basic format of MLFlow, this address u can set
#mlflow.set_tracking_uri("My-Machine-Learning-Projects\MLFlow\project-1\mlruns")

## When using backend-artifact storing format
#mlflow.set_tracking_uri("sqlite:///My-Machine-Learning-Projects\MLFlow\project-1\mlflow_server\mlruns.db")

# When using MLFlow Server
mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("Dropping columns")


if not os.path.exists("tmp"):
    os.makedirs("tmp")

# Load the complete dataset, select features + target variable
data = pd.read_csv(r"My-Machine-Learning-Projects\MLFlow\project-1\Ames-Housing.csv")
feature_columns = ["Lot Area", "Gr Liv Area", "Garage Area", "Bldg Type"]
selected = data.loc[:, feature_columns + ["SalePrice"]]

# Feature encoding
cat_features = ["Bldg Type"]

def prepare_data(dataframe):
    df = dataframe
    # Encode all categorical features
    for col in list(dataframe.columns):
        if col in cat_features:
            # One-hot encoding
            dummies = pd.get_dummies(df[col])
            # Drop the Original column
            df = pd.concat([df.drop([col], axis = 1), dummies], axis = 1)

    # Fill missing values with 0
    df = df.fillna(0)

    return df

def train_and_evaluate(dataframe):
    # Seperate features from the target variable and convert to Numpy
    features = dataframe.drop(["SalePrice"], axis=1).to_numpy()
    target = dataframe.loc[:, "SalePrice"].to_numpy()
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size = 0.2, random_state=12
    )

    # Plot
    plot= dataframe.plot.scatter(x=0, y="SalePrice")
    fig = plot.get_figure()
    fig.savefig("tmp/plot.png")

    # Save the database
    dataframe.to_csv("tmp/dataset.csv", index = False)
    # Train the model
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    serialized_model = pickle.dumps(model)
    with open("tmp/model.pkl", "wb") as m:
        m.write(serialized_model)

    #mlflow.log_artifact("tmp/model.pkl", artifact_path="models")
    mlflow.log_artifacts("tmp")

    # Evaluate the model
    y_pred = model.predict(X_test)
    err = mean_squared_error(y_test, y_pred)
    print(f"MSE:{err}")
    #mlflow.log_metric("MSE", err)
   
# add None so that we get one training with all the columns
columns_to_drop = feature_columns + [None]

for to_drop in columns_to_drop:

    if to_drop:
        dropped = selected.drop([to_drop], axis=1)
    else:
        dropped = selected
    
    with mlflow.start_run() as run:
        #print(f"Dropping{to_drop}")
        print(f"Dropping {to_drop}")
        #mlflow.log_param("Drop Column", to_drop)
        prepared = prepare_data(dropped)
        train_and_evaluate(prepared)
        #print("Run completed")

# Delete temp included the model.pkl, after run the code
shutil.rmtree("tmp")