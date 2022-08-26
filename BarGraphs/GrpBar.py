import pandas as pd
import matplotlib.pyplot as plt
exam_data = {'name': ['Chandler', 'Monica', 'Ross', 'Rachel', 'Joey', 'Pheobe'],
                'Maths_score': [44, 24, 31, 10, 16,20],
                'Science_score': [25, 44, 37, 62, 75, 50],
                'French_score': [55, 13, 63, 53, 40, 45]}
df = pd.DataFrame(exam_data, columns = ['name', 'Maths_score', 'Science_score', 'French_score'])
print(df)
pos = list(range(len(df['Maths_score'])))
width = 0.25
fig, ax = plt.subplots(figsize=(10,5))

plt.bar(pos, df['Maths_score'], width, alpha=0.5, color='Red')
plt.bar([p + width for p in pos], df['Science_score'], width, alpha=0.5, color='Blue')
plt.bar([p + width*2 for p in pos], df['French_score'], width, alpha=0.5, color='Yellow')
     # Setting the y axis label
ax.set_ylabel('Score')

    # Setting the chart's title
ax.set_title('Test Subject Scores')

    # Setting the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

    # Setting the labels for the x ticks
ax.set_xticklabels(df['name'])

    # Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Maths_score'] + df['Science_score'] + df['French_score'])] )

    # Adding the legend and showing the plot
plt.legend(['Maths Score', 'Science Score', 'French Score'], loc='upper left')
plt.grid()
plt.show()

