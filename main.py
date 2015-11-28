import pandas as pd

key_distances = pd.read_csv('data/key_distances.csv')
model_infos = pd.read_csv('data/model.csv')

def load_key_data(filename):
    key_data = pd.read_csv(filename)
    key_data = pd.merge(key_data, key_distances, how='left', on=['code_point', 'intent_code_point'])
    key_data = pd.merge(key_data, model_infos, how='left', on=['model'])
    return key_data

def load_sensor_data(filename):
    data = pd.read_csv(filename)
    data = pd.merge(data, model_infos, how='left', on=['model'])
    return data

def load_save_data(filename):
    data = pd.read_csv(filename)
    data = pd.merge(data, model_infos, how='left', on=['model'])
    return data

key_data = load_key_data('data/v2_corporate/key.csv')
sensor_data = load_sensor_data('data/v2_corporate/sensor.csv')
save_data = load_save_data('data/v2_corporate/save.csv')
