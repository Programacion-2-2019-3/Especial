import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a0 = pd.read_csv('migration.csv')

# a1 = a0.groupby('year_month').size()
# print (a1)
# a2 = a0.groupby('month_of_release').size()
# print(a2)
# a3= a0.groupby('passenger_type').size()
# print(a3)
# a4=a0.groupby('direction').size()
# print (a4)
# a5=a0.groupby('citizenship').size()
# print(a5)
# a6=a0.groupby('visa').size()
# print(a6)
# a7=a0.groupby('country_of_residence').size()
# print(a7)
# a8=a0.groupby('estimate').size()
# print(a8)
# a9=a0.groupby('standard_error').size()
# print(a9)
# a10=a0.groupby('status').size()
# print(a10)

b=a0.query("visa=='Student'")
b1 = b.groupby('year_month').size()

c = a0.query("country_of_residence=='United Kingdom'")
c1 = c.groupby('year_month').size()

d=a0.query("status == 'Provisional'")
d1=d.query("month_of_release == '2018-12'")
d2=d1.query("visa == 'Work'")
d3=d2.groupby('year_month').size()

e=a0.query("visa=='NZ and Australian citizens'")
e1=e.query("country_of_residence=='France'")
e2=e1.groupby('year_month').size()

f=a0.query("country_of_residence=='Netherlands'")
f1=f.query("visa == 'Other'")
f2=f1.groupby('month_of_release').size()

fig1=plt.figure()
b1.plot(legend=False)
fig2=plt.figure()
c1.plot(legend=False)
fig3=plt.figure()
d3.plot(legend=False)
fig4=plt.figure()
e2.plot(legend=False)
fig5=plt.figure()
f2.plot(legend=False)
