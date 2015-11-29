import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calculateConvenience
import calculateRealErrorRate
import calculateCorrelation

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
    data = pd.read_csv(filename, names=['time', 'file_name', 'battery', 'model', 'age', 'years_of_use', 'sex', 'input_posture', 'input_situation', 'keyboard_condition', 'test_time', 'word_count', 'WPM', 'error_count', 'error_rate', 'letter_count'], skiprows=[0])
    data = pd.merge(data, model_infos, how='left', on=['model'])
    return data

#key_data = load_key_data('data/v2_corporate/key.csv')
#sensor_data = load_sensor_data('data/v2_corporate/sensor.csv')
save_data = load_save_data('data/v2_corporate/save.csv')

screen_error_rate_by_size = save_data.groupby('diag').mean()['error_rate']
#screen_error_rate_by_size.plot()

sensor_columns = ('acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z',
                  'mag_x', 'mag_y', 'mag_z', 'azim', 'pitch', 'roll',
                  'light', 'prox')

class mean_sensor:
    def __init__(self, itr):
        self.itr = itr
        self.prev_val = None
        self.count = 0
        self.prev_data = None

    def calc(self, time, data, cur_val):
        if time < cur_val['time']:
            return False
        for k in sensor_columns:
            data[k] += np.abs(cur_val[k])
            self.count += 1
        return True

    def __call__(self, row):
        time = row['time']
        self.count = 0
        data = {k: 0 for k in sensor_columns}
        if self.prev_val is not None:
            if self.calc(time, data, self.prev_val):
                self.prev_val = None

        if self.prev_val is None:
            for val in self.itr:
                if not self.calc(time, data, val[1]):
                    self.prev_val = val[1]
                    break

        if 'acc' not in data:
            def sq_sqrt(key):
                data[key] = np.sqrt(np.sum(np.power([data[key + '_x'], data[key + '_y'], data[key + '_y']], 2)))
            sq_sqrt('acc')
            sq_sqrt('gyro')

        if self.count == 0 and self.prev_data:
            data = self.prev_data
        else:
            self.prev_data = data

        data['time'] = time
        return pd.Series(data if self.count == 0 else
                         {k: data[k] / self.count for k in sensor_columns})

prefix = 'data/v1_original/'
def key_sensor_merged_data(index):
    post_fix = '_%d.csv' % index
    key = load_key_data(prefix + 'key/Key' + post_fix)
    sensor = load_sensor_data(prefix + 'sensor/Sensor' + post_fix)
    itr = sensor.iterrows()
    key = key.merge(key.apply(mean_sensor(itr), axis=1))

    return key

# sample
key_data = pd.read_csv('data/key_data_calced.csv') #pd.concat([key_sensor_merged_data(i) for i in range(1,28655)])

plt.figure(1)
real_error = calculateRealErrorRate.calculateRealErrorRate(save_data,key_data,plt)
save_data = calculateConvenience.calculateConvenience(save_data,real_error,plt)
calculateCorrelation.calculateCorrelation(save_data,plt)
plt.show()
