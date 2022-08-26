import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'Football':20, 'Cricket':17, 'Basketball':15,
        'Badminton':15, 'Tennis':10}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure()
#fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
#plt.bar(courses, values, color ='maroon')
plt.bar(courses, values, color=['C0', 'C1', 'C2', 'C3'],        width = 0.4)
 
plt.xlabel("")
plt.ylabel("No. of students")
plt.title("Favorite Sport")
plt.tight_layout()
plt.show()
fig.savefig('VerBar.png', format='png',bbox_inches='tight',dpi=300)
