import pandas as pd
from pkg_resources import resource_filename
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_frequency_recency_matrix
from lifetimes.utils import summary_data_from_transaction_data
from lifetimes.plotting import plot_probability_alive_matrix
import pylab
import matplotlib.pyplot as plt



if __name__ == "__main__":
    #data=pd.read_csv(resource_filename('lifetimes', 'datasets/' + 'example_transactions - Copy2.csv'))
    #print(data.head())
    #summary = summary_data_from_transaction_data(data, 'id', 'date',observation_period_end='2014-12-31')
    summary=pd.read_csv("res1.csv")
    print (summary.head())
    bgf = BetaGeoFitter()
    bgf.fit(summary['frequency'], summary['recency'], summary['T'])
    print (bgf)
    plot_frequency_recency_matrix(bgf)
    #pylab.show()
    plt.savefig('recencymatrix.png')
    plt.close()
    plot_probability_alive_matrix(bgf)
    #pylab.show()
    plt.savefig('probability.png')
    individual=summary.iloc[20]
    #print(individual)
    
    t=7
    print("\n\n\nselected customer probability in next week")
    print(bgf.conditional_expected_number_of_purchases_up_to_time(t,individual['frequency'],individual['recency'],individual['T']))
    summary['predicted_purchases']=(bgf.conditional_expected_number_of_purchases_up_to_time(t, summary['frequency'], summary['recency'], summary['T']))
    print (summary.head())




    summary2 = summary[summary['frequency']>0]
    ggf = GammaGammaFitter(penalizer_coef = 0)
    ggf.fit(summary2['frequency'],
    summary2['monetary_value'])
    print (ggf)
    print("\n\n\nSelected customer clv")
    print(ggf.conditional_expected_average_profit(individual['frequency'],individual['monetary_value']))
    summary['clv']=(ggf.conditional_expected_average_profit(summary2['frequency'],summary2['monetary_value']))
    print(summary.head())
