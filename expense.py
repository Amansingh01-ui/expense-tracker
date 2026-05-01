class Expense:
    def __init__(self,amount,category,note):
        self.amount = amount
        self.category = category
        self.note = note

    def to_dict(self):
        return{
            "amount":self.amount,
            "category":self.category,
            "note":self.note
        }