import pandas as pd
from statsmodels.formula.api import ols

data_all = pd.read_csv('studyresults.csv', header=0).fillna(0)

data_primed = data_all[data_all['Priming'] == 'Primed']
data_non_primed = data_all[data_all['Priming'] == 'Non-Primed']
data_jsf = data_all[data_all['Framework'] == 'JSF']
data_jsf = data_all[data_all['Framework'] == 'Spring']

testset = [
    {'check' : 'fwsupport ~ C(Framework)' ,  'set':data_primed, 'text':'primed_only'},
    {'check' : 'fwsupport ~ C(Framework)' ,  'set':data_all, 'text':'all'},
    {'check' : 'Security ~ secscore' ,  'set':data_primed, 'text':'primed_only'},
    {'check' : 'Security ~ secscore' ,  'set':data_all, 'text':'all'},
    #{'check' : 'C(Functional) ~ C(Q22)' ,  'set':data_all},
    #{'check' : 'tasktime ~ C(Q22)' ,  'set':data_all},
]

for test in testset:
    r = ols(test['check'],test['set']).fit()
    print test['check'] + " ("+test['text']+") : "
    print "r_sq       = " + str(r.rsquared)
    print "p          = " + str(r.f_pvalue)
    print "beta_coeffs: "
    print r.params
    print ""
