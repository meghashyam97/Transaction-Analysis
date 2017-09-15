import urllib
import time
from collections import defaultdict
from itertools import combinations
import sys
import os


#with open('output.csv', 'r') as f:
#    i = 0
#    for line in f:
#        print (line)
#        i+=1
#        if i==10:
#            break
def data_pass(file_location, support, pass_nbr, candidate_dct):
    with open(file_location, 'r') as f:
        for line in f:
            item_lst = line.split(",")     
            candidate_dct = update_candidates(item_lst, candidate_dct, pass_nbr)
        
    candidate_dct = clear_items(candidate_dct, support, pass_nbr)
    
    return candidate_dct


def update_candidates(item_lst, candidate_dct, pass_nbr):
    if pass_nbr==1:
        for item in item_lst:
            candidate_dct[(item,)]+=1
    else:
        frequent_items_set = set()
        for item_tuple in combinations(sorted(item_lst), pass_nbr-1):    
            if item_tuple in candidate_dct:
                frequent_items_set.update(item_tuple)
                    
        for item_set in combinations(sorted(frequent_items_set), pass_nbr):
            candidate_dct[item_set]+=1
        
    return candidate_dct

def clear_items(candidate_dct, support, pass_nbr):
    for item_tuple, cnt in candidate_dct.copy().items():
        if cnt<support or len(item_tuple)<pass_nbr:
            del candidate_dct[item_tuple]
    return candidate_dct


def main(file_location, support, itemset_size):
    candidate_dct = defaultdict(lambda: 0)
    for i in range(itemset_size):
        now = time.time()
        candidate_dct = data_pass(file_location, support, pass_nbr=i+1, candidate_dct=candidate_dct)
        print ("pass number %i took %f and found %i candidates" % (i+1, time.time()-now, len(candidate_dct)))
    return candidate_dct

if __name__ == '__main__':
    itemsets_dct=main('output.csv',9,3)
    if os.path.exists("Apriori.txt"):
        os.remove("Apriori.txt")    
    for itemset, frequency in itemsets_dct.items():
        orig_stdout = sys.stdout
        f = open('Apriori.txt', 'a')
        sys.stdout = f
        print (itemset, frequency)
        sys.stdout = orig_stdout
        f.close()

        

