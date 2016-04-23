import pandas as pd
import pylab as pl
pd.set_option('display.width', 100)


# query needs numexpr to be installed
def f(x):
    print x
    return x == "Gold"

def main():
    # read in medal table (n.b. delimiters are at least 2 characters long) 
    medal_table = pd.read_csv("data/olympics_2012_medal_table.txt",
                               engine = 'python',
                               skiprows = 1,
                               encoding = 'UTF-8', 
                               sep = '[ )(]{2,}')
    korean_golds = medal_table[medal_table.Id == "KOR"]["Gold"].as_matrix()[0]
    print "Korea earned {} golds".format(korean_golds)
    print "\nCountries with more golds than Korea:"
    result = medal_table[medal_table.Gold > korean_golds][["Country", "Gold"]]
    print result.to_string(index=False)
main()
