# challenge-api-deployment
Deploy a machine learning model and Create a Flask API that can handle a machine learning model. We deploy an API to Heroku with Docker.


Structure:

|-app.py-> route('/'): return "Alive", route('/predict',[post,get]):input->json data, output: price in json
|-docker
    |   |-Dockerfile -> your Dockerfile
    |-pipeline
    |   |
    |   |-preprocessing
    |   |    |-cleaning_data.py ->preprocess()->input: new house data,output: processed data else error (if required data is present)
    |   |-model
    |   |    |-model.py 
    |   |-predict
    |   |    |-prediction.py-> predict()->input: preprocessed data,output: price
|-requirements.txt
