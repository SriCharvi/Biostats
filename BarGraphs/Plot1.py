import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv('district.csv')
data.head()
 
re=data.iloc[:30,5].values
de=data.iloc[:30,4].values
co=data.iloc[:30,3].values
x=list(data.iloc[:30,0])
 
plt.figure(figsize=(10,10))
ax=plt.axes()
 
ax.set_facecolor('black')
ax.grid(linewidth=0.4, color='blue')
 
 
plt.xticks(rotation='vertical',
           size='5',
           color='white')#ticks of X
 
plt.yticks(size='5',color='white')
 
 
ax.set_xlabel('\nDistrict',size=20,
              color='green')
ax.set_ylabel('No. of cases\n',size=20,
              color='red')
 
 
plt.tick_params(size=5,color='white')
 
 
ax.set_title('Maharashtra District wise breakdown\n',
             size=20,color='Black')
 
plt.bar(x,co,label='re')
plt.bar(x,re,label='re',color='green')
plt.bar(x,de,label='re',color='red')
 
for i,j in zip(x,co):
    ax.annotate(str(int(j)),
                xy=(i,j+3),
                color='white',
                size='5')
plt.show()

plt.legend(['Confirmed','Recovered','Deceased'],
           fontsize=10)