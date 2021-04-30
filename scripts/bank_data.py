import pandas as  pd
import json
import jsonlines
import matplotlib.pylab as plt
import seaborn as sns
from scripts import openapi as op, eaxmples as ex

def import_bank_transactions(transactions):
    df = pd.DataFrame(transactions['results'])
    set_catergories(df)
    return "done"

def make_a_nice_graph(df):
    g = sns.catplot(x="cat", y="amount", data=df)
    g.set_xticklabels(rotation=30)
    g.savefig("../static/catVamt.png")
    return "done"

def set_catergories(df):
    head = df
    head['cat'] = head['description'].apply(lambda x: op.classfiy(x, ex.bank_classes)[0]['label'])
    head.to_csv("./data/test_bank_trans.csv")
    print(head.columns)
    #print(head['cat'])
    return "done" #make_a_nice_graph(head)
#set_catergories()
#make_a_nice_graph(pd.read_csv("../data/test_bank_trans.csv"))
