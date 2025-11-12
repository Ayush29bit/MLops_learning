import mlflow
print("printing tracking uri scheme:", mlflow.get_tracking_uri().split(":")[0])

mlflow.set_tracking_uri("http://127.0.0.1:5000")
print("printing tracking uri after set:", mlflow.get_tracking_uri().split(":")[0])
