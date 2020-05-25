import csv


class StatementReader:
    """Reads transaction statements of ING bank from csv format """
    path_to_csv = None
    cost_dict = {
            'income': 0,
            'utilities': 0,
            'car': 0,
            'utilities': 0,
            'house': 0,
            'groceries': 0,
            'one-timers': 0,
            'insurance': 0,
            'supplements': 0,
            'charity': 0,
            'eating-out': 0
            }

    def __init__(self, path_to_csv: str):
        self.path_to_csv = path_to_csv


    def get_spending_per_category(self, add_income = False):
        """ Map every description into a category and add the quantity of the transaction to this category. Returns a
        dictionary of categories: cost"""
        with open(self.path_to_csv, newline='') as csvfile:
            self.statement_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(self.statement_reader)
            for row in self.statement_reader:
                quantity = float(row[6].replace(",", "."))
                description = row[1].split(" ")
                key = None
                if any(s in ("Universiteit") for s in description):
                    key = 'income'
                if any(s in ("AO", "Vierwinden", "CarDol", "PARK", "WYCK-OOST", "SCHADEVERZEKERING") for s in description):
                    key = 'car'
                if any(s in ("MONEYOU", "Telfort", "Voogd") for s in description):
                    key = 'house'
                if any(s in ("Albert", "ALBERT", "Jumbo", "Supermarkt") for s in description):
                    key = 'groceries'
                if any(s in ("OXXIO", "SIMYO", "WATERLEIDING", "WATERSCHAPPEN") for s in description):
                    key = 'utilities'
                if any(s in ("Shell", "SHELL", "TANKSTELLE", "JET-SB-TANKSTELLE", "BELASTINGDIENST") for s in description):
                    key = 'car'
                if any(s in ("Wall", "CREDITCARD", "HOSTNET", "Steampowered", "Praxis", "KWANTUM", "Action", "Verfzaak", "Kwantum", "GARTEN", "Amazon", "Decathlon", "bol.com", "BLOKKER", "Kleurenwaaiernl", "RMschilderwerken") for s in description):
                    key = 'one-timers'
                if any(s in ("CZ") for s in description):
                    key = 'insurance'
                if any(s in ("Spiru") for s in description):
                    key = 'supplements'
                if any(s in ("KWF") for s in description):
                    key = 'charity'
                if any(s in ("SiteDish.nl") for s in description):
                    key = 'eating-out'
                if key and self.cost_dict.get(key, -1) >= 0:
                    self.cost_dict[key] = self.cost_dict[key] + quantity
                else:
                    print("Did not find category for row: " + str(row))
        if not add_income:
            del self.cost_dict['income']
        return self.cost_dict




