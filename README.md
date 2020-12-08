# challenge-api-deployment

### Introduction:
This project is an BeCode Bouman group challange for 5 days (Deadline:08/12/2020). The project has done by Davy Nimbona (team leader), Manasa Devinoolu, Christophe Schellinck and Selma Esen. 

### Goal:

In that project we have created a prediction model to predict new selling prices for the new properties according to our dataset. The real estate data has been scrapped, celeaned and analized in our previous projects. The goal of this project is creating an API to get an new property input and return a price as output. The API Wrapped by a Docker file and deployed by Heroku.

### The input:
```json
{
    "data": {
            "area": int,
            "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
            "rooms-number": int,
            "zip-code": int,
            "garden": Optional[bool],
            "equipped-kitchen": Optional[bool],
            "furnished": Opional[bool],
            "terrace": Optional[bool],
            "facades-number": Optional[int]
    }
}
```

Area, property-type, rooms-number and zip-code are required(mandatory) in order to run the application

### The output:
```json
{
    "prediction": Optional[float],
    "error": Optional[str]
}
```

### File structure:

    .
    ├── ...
    ├── docker                    
    │   ├── Dockerfile                           
    ├── pipline                    
    │   ├── model
    │       ├── model.py
    │       ├── model.pkl
    │       ├── ready_to_model_df.csv
    │   ├── predict
    │       ├── prediction.py
    │   ├── preprocessing 
    │       ├── cleaning_data.py
    │       │── test-dataframe.csv
    ├── Procfile
    ├── app.py
    ├── requirements.txt
    ├── README.md
    



### Details:

