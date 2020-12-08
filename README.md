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
            "land-area": Optional[int],
            "garden": Optional[bool],
            "garden-area": Optional[int],
            "equipped-kitchen": Optional[bool],
            "full-address": Optional[str],
            "swimmingpool": Opional[bool],
            "furnished": Opional[bool],
            "open-fire": Optional[bool],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    }
}
```

### The output:
```json
{
    "prediction": Optional[float],
    "error": Optional[str]
}
```

### File structure:


### Detailes:

