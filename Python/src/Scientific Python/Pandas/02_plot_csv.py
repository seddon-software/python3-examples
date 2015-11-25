import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

    
def main(): 
    # set column names and read in data from file
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    lerwick_data = pd.read_csv("data/lerwick.txt", 
                               engine = 'python',
                               skiprows = 7, 
                               names = column_names, 
                               skipinitialspace = True, 
                               sep = '[*# ]+')

    # create a new column from year and month columns
    lerwick_data['period'] = lerwick_data.apply(lambda x : "{:.0f}-{:.0f}".format(x.year, x.month), raw = True, axis = 1)

    # drop columns we are not using (not necessary)
    lerwick_data.drop(['year', 'month', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment'], axis = 1, inplace = True)

    # plot remaining data as a bar chart
    ax = lerwick_data[-50:].plot(figsize=(16, 10), 
                               title = 'Lerwick : Min and Max Temperatures', 
                               x = 'period',
                               y = ['tmin', 'tmax'], 
                               color = ['red', 'cyan'], 
                               kind = 'bar')
    ax.set_xlabel("years and months")
    ax.set_ylabel("$^\circ$C")
    for item in [ax. title, ax.xaxis.label, ax.yaxis.label]:
        item.set_fontsize(20)
    pl.show()


main()



