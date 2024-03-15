import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000/")

logged_model = 'runs:/1ce52043ae234d7dbc1caaebc5c63cfe/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

loaded_model.predict({"ingredients": "apples", "tools":"oven"})