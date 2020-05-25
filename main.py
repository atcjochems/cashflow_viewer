from StatementReader import StatementReader
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
import numpy as np

import matplotlib.pyplot as plt

statement_reader = StatementReader("NL54INGB0008882696_29-10-2019_24-05-2020.csv")
spending_per_category = statement_reader.get_spending_per_category(True)

for category, amount in spending_per_category.items():
    print(category + ": " + str(amount))


total_income = spending_per_category.get('income', 0)
del spending_per_category['income']
total_costs = sum(spending_per_category.values())

cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

the_grid = GridSpec(2, 1)
figures = plt.figure(constrained_layout=True)
spec2 = GridSpec(ncols=1, nrows=2, figure=figures)
f2_ax1 = figures.add_subplot(spec2[0, 0])
f2_ax3 = figures.add_subplot(spec2[1, 0])
f2_ax1.pie(spending_per_category.values(), labels=spending_per_category.keys(), autopct='%1.1f%%', shadow=True, colors=colors)
f2_ax3.barh(("1", "2"), (total_income, total_costs), color=("green", 'red'))
plt.yticks(("1", "2"), ("Income", "Costs"))
plt.show()