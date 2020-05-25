# cashflow_viewer
Reads an transaction csv from the Dutch ING bank and plots amount spent per category.

# requirements
pip install matplotlib

# usage
## Set directory of your transaction statement
First, get a transaction statement in csv format from your ing bank account (www.ing.nl). Then set the reference to this file on line 10 in main.py.
## Run main.py
You should now see a pie chart of your spendings per category. Note: you may need to add keywords to StatementReader.py to properly categorize your bank statements. As I have a fulltime job I am not going to maintain a datanbase.
