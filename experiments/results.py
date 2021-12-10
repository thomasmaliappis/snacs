import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

# dataset_replacements = {
#     'aarhus':
# }

df = pd.read_csv('results.csv')
# df['dataset'].replace(dataset_replacements, inplace=True)
df['measure'].replace({1: 'F1', 2: 'F2', 3: 'F3'}, inplace=True)
df['motif'].replace({1: 'Feed Forward', 2: 'Bifan', 3: 'Biparallel', 4: 'Cascade'}, inplace=True)
for dataset in df['dataset'].unique():  # loop datasets
    data = df[df['dataset'] == dataset]
    sns.barplot(x="measure", y="count", hue="motif", data=data)
    plt.title(dataset)
    plt.yscale('log')
    plt.savefig('./png/{}_count.png'.format(dataset))
    plt.show()
    sns.barplot(x="measure", y="time", hue="motif", data=data)
    plt.title(dataset)
    plt.yscale('log')
    plt.savefig('./png/{}_time.png'.format(dataset))
    plt.show()

