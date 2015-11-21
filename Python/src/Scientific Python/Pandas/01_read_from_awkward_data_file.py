# This application reads meteorological data from oxford
# 1) The file has a header that needs to be skipped
# 2) There are a variable number of columns
# 3) Some data is marked with an * which needs to be stripped
  
import pandas as pd
import pylab as pl

def main(filename, year_start, year_end): 
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    oxford_data = pd.read_csv(filename, na_values = ['---'], skiprows = 7, names=column_names, skipinitialspace = True, sep = ' ')
    
    col = oxford_data.year
    row_min = min(col[col == year_start].index.tolist())
    row_max = max(col[col == year_end].index.tolist())
    # build a slice of the rows we are interested in    
    s = slice(row_min, row_max)
     
    # combine month and year into a single field
    period = oxford_data[['year', 'month']].apply(lambda x: "{}-{}".format(x[0], x[1]), axis=1)
    tmin = oxford_data['tmin'].apply(cleanup_temperatures)
    tmax = oxford_data['tmax'].apply(cleanup_temperatures)
    
    # create a new data frame
    df = pd.concat([tmin[s], tmax[s], period[s]], axis = 1)
    df.columns = ['tmin', 'tmax', 'period']

    df.plot(figsize=(16, 8), title = 'Min and Max Temperatures', x = 'period', y = ['tmin', 'tmax'], color = ['red', 'cyan'], kind = 'bar')
    pl.show()

def isNaN(num): return num != num

def cleanup_temperatures(t):
# some of the temperatures have *'s that need to be removed
# some of the temperatures are NaNs (convert to zero)
# the temeratures are strings and must be converted to float
    if isNaN(t): return 0.0
    if t[-1] == '*': return float(t[:-1])
    return float(t)


# print min, max temperatures between given years
main("data/oxforddata.txt", 1972, 1978)
