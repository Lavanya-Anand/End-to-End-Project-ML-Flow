# End-to-End-Project-ML-Flow

# Developement steps

1. Update config.yaml - raw details
2. Update schema.yaml - Dependent and independent columns
3. Update params.yaml - Model parameters
4. Update the entity - Configuration classes
5. Update the Configuration manager in src config - Creating directories and calling class, Assigning the raw details to class variables
6. Update the components - separate functions for each configuration manager
7. Update the pipeline - Calling those componnets classes and creating a pipeline
8. Update the main.py - Triggering those pipelines
9. Update the app.py

# Steps to Run

1. Clone the repository
2. Create a conda environment:
    conda create -n mlproj python=3.8 -y
    conda activate mlproj
3. Install Requirements
    pip install -r requiremnts.txt
4. python app.py

# MLFlow - DagsHub

1. Integrate the github repository in DagsHub
2. Copy the URI, username and password from Remote -> Experiment
3. Modify the following code to declare it as env variable 
``` bash
export MLFLOW_TRACKING_URI=
export MLFLOW_TRACKING_USERNAME=
export MLFLOW_TRACKING_PASSWORD=
```




