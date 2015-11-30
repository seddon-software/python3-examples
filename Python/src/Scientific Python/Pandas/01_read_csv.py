import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

def main(): 
    print pd.__version__
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    lerwick_data = pd.read_csv("data/lerwick.txt", 
                               skiprows = 8, 
                               names = column_names, 
                               skipinitialspace = True, 
                               sep = '[*# ]+')
    print lerwick_data


main()
