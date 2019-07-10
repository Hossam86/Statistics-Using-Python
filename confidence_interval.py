# Compute a confidence interval from a dataset

from scipy.stats import sem, t
from scipy import mean

confidence =0.95
data=[1,2,3,4,5]
n=len(data)
m=mean(data)
std_err=sem(data)
h=std_err*t.ppf((1+confidence)/2,n-1)
start=m-h
end=m+h
print( "cofidence_limits", start, end)