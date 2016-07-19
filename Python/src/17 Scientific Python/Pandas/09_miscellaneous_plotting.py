import numpy as np
import pandas as pd
import pylab as pl
pd.set_option('display.width', 100)
pd.set_option('display.max_rows', 500)

# conversion routines
weights = { 'P' : 2, 'S' : 3, 'G' : 5, 'W' : 10, 'N' : 50 }

def convert(t):
    pts = 0
    if t in weights: pts = weights[t]
#     if t == 'P': pts = 2
#     if t == 'S': pts = 3
#     if t == 'G': pts = 5
#     if t == 'W': pts = 10
#     if t == 'N': pts = 50
    return pts

def days_of_the_week(d):
    if d == 'Mon': return 0
    if d == 'Tue': return 1
    if d == 'Wed': return 2
    if d == 'Thu': return 3
    if d == 'Fri': return 4
    if d == 'Sat': return 5
    if d == 'Sun': return 6
    
# remove the time from datatime xticks and rotate
def set_xticks(ax):
    pl.xticks(rotation=45)
    for tick in ax.xaxis.get_majorticklabels():
        tick.set_horizontalalignment("right")
    xtl = [item.get_text()[:10] for item in ax.get_xticklabels()]
    ax.set_xticklabels(xtl)

def main(): 
    # read in the data and add a 'pts' field
    the_data = pd.read_csv("data/miscellaneous.txt", engine = 'python', sep = '[ ]+', parse_dates = ['date'])
    the_data['pts'] = the_data['type'].apply(convert)

    # create and plot a new dataframe indexed on date
    daily_data = the_data.groupby(['date']).aggregate(np.sum)
    daily_data['date'] = daily_data.index       # add the index as a real column
    daily_data.drop(['hr', 'qty'], axis = 1, inplace = True)
    ax = daily_data.plot(figsize=(16, 9), title = "Daily Totals", kind = 'bar')
    set_xticks(ax)
    pl.show()

    # add more columns to original dataframe
    the_data['P'] = the_data.apply(lambda x : x.qty if x.type == 'P' else 0, axis = 1)
    the_data['S'] = the_data.apply(lambda x : x.qty if x.type == 'S' else 0, axis = 1)
    the_data['G'] = the_data.apply(lambda x : x.qty if x.type == 'G' else 0, axis = 1)
    the_data['W'] = the_data.apply(lambda x : x.qty if x.type == 'W' else 0, axis = 1)
    the_data['N'] = the_data.apply(lambda x : x.qty if x.type == 'N' else 0, axis = 1)
    
    # create and plot a new dataframe indexed on date and including the new columns
    daily_data = the_data.groupby(['date']).aggregate(np.sum)
    daily_data.drop(['hr', 'qty', 'pts'], axis = 1, inplace = True)
    ax = daily_data.plot(figsize=(16, 9), title = "Stacked Bar Chart for Types", kind = 'bar', stacked = True)
    set_xticks(ax)
    pl.show()

    # create and plot a new dataframe indexed on hr and including the new columns
    hourly_data = the_data.groupby(['hr']).aggregate(np.sum)
    hourly_data.drop(['qty', 'pts'], axis = 1, inplace = True)
    ax = hourly_data.plot(figsize=(16, 9), title = "Hourly Totals", kind = 'bar', stacked = True)
    pl.show()
    
    # create and plot a new dataframe indexed on day and including the new columns
    weekly_data = the_data.groupby(['day']).aggregate(np.sum)
    weekly_data['day'] = weekly_data.index      # used to order the days
    weekly_data['order'] = weekly_data['day'].apply(days_of_the_week)
    weekly_data.sort_values(axis = 0, by = 'order', inplace = True)
    weekly_data.drop(['order', 'hr', 'qty', 'pts'], axis = 1, inplace = True)
    ax = weekly_data.plot(figsize=(16, 9), title = "Weekly Totals", kind = 'bar', stacked = True)
    pl.show()
    
    # plot weighted pie chart of types    
    totals = the_data.sum()
    totals.drop(['hr', 'qty', 'pts'], inplace = True)
    weightings = pd.Series(weights)  # create a series from dict
    weighted_totals = totals.multiply(weightings)
    ax = weighted_totals.plot(kind='pie', autopct='%2.1f%%', startangle=90)
    ax.set_ylabel("")
    pl.axis('equal')
    pl.title('Weighted Average')
    pl.show()
    
    
main()
