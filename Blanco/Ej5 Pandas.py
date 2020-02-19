import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a0 = pd.read_csv('migration.csv')

a1 = a0.groupby('year_month').size()
print (a1)
a2 = a0.groupby('month_of_release').size()
print(a2)
a3= a0.groupby('passenger_type').size()
print(a3)
a4=a0.groupby('direction').size()
print (a4)
a5=a0.groupby('citizenship').size()
print(a5)
a6=a0.groupby('visa').size()
print(a6)
a7=a0.groupby('country_of_residence').size()
print(a7)
a8=a0.groupby('estimate').size()
print(a8)
a9=a0.groupby('standard_error').size()
print(a9)
a10=a0.groupby('status').size()
print(a10)