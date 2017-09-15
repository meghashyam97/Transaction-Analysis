import pandas as pd
from pkg_resources import resource_filename
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_frequency_recency_matrix
from lifetimes.utils import summary_data_from_transaction_data
from lifetimes.plotting import plot_probability_alive_matrix
import sys
import warnings
warnings.filterwarnings("ignore")

import pylab
if __name__ == "__main__":
    summary=pd.read_csv("res1.csv")
    #print (summary.head())
    bgf = BetaGeoFitter()
    bgf.fit(summary['frequency'], summary['recency'], summary['T'])
    #print (bgf)
    #plot_frequency_recency_matrix(bgf)
    #pylab.show()
    #plot_probability_alive_matrix(bgf)
    #pylab.show()
    index=0
    val=(sys.argv[1])
    for row in summary:
        if row[0] == val:
            break 
        else : 
            index+=1
    individual=summary.iloc[index]
    #print(individual)
    
    t=7
    #print("\n\n\nselected customer probability in next week")
    #print(bgf.conditional_expected_number_of_purchases_up_to_time(t,individual['frequency'],individual['recency'],individual['T']))
    #summary['predicted_purchases']=(bgf.conditional_expected_number_of_purchases_up_to_time(t, summary['frequency'], summary['recency'], summary['T']))
    #print (summary.head())




    summary2 = summary[summary['frequency']>0]
    ggf = GammaGammaFitter(penalizer_coef = 0)
    ggf.fit(summary2['frequency'],
    summary2['monetary_value'])
    #print (ggf)
    #print("\n\n\nSelected customer clv")
    print(ggf.conditional_expected_average_profit(individual['frequency'],individual['monetary_value']))
    #summary['clv']=(ggf.conditional_expected_average_profit(summary2['frequency'],summary2['monetary_value']))
    #print(summary.head())
