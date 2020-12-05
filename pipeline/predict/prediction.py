import pickle

model_pkl = pickle.load(open('pipeline/model/houseprice_model_mandatory.pkl', 'rb'))


def predict(df):
    """
    function takes the input data from flask
    parameters: df -> dataframe, model->pickle
    return: result -> predicted price
    """
    df["property - type_HOUSE"] = int(df["property - type_HOUSE"])
    df["property - type_OTHERS"] = int(df["property - type_OTHERS"])
    df["property-type_APARTMENT"] = int(df["property-type_APARTMENT"])
    df["rooms-number"] = float(df["rooms-number"])
    df["area"] = float(df["area"])
    df["province_Brussels Capital Region"] = int(df["province_Brussels Capital Region"])
    df["province_Liège"] = int(df["province_Liège"])
    df["province_Walloon Brabant"] = int(df["province_Walloon Brabant"])
    df["province_West Flanders"] = int(df["province_West Flanders"])
    df["province_Flemish Brabant"] = int(df["province_Flemish Brabant"])
    df["province_Luxembourg"] = int(df["province_Luxembourg"])
    df["province_Antwerp"] = int(df["province_Antwerp"])
    df["province_East Flanders"] = int(df["province_East Flanders"])
    df["province_Hainaut"] = int(df["province_Hainaut"])
    df["province_Limburg"] = int(df["province_Limburg"])
    df["province_Namur"] = int(df["province_Namur"])
    result = model_pkl.predict(df)

    result = str(result).replace('[', ' ').replace(']', ' ')

    return result
