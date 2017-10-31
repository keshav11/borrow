from models import borrower
from pymongo import MongoClient

class DataManager:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.borrower_db

    def get_borrower(self, borrower_name):
        return self.db.borrowers.find({"Name":borrower_name})

    def add(self, borrower):
        print "Adding", borrower.name + "..."
        if(self.get_borrower(borrower.name).count() > 0):
            print borrower.name, "already exists.", "Try updating instead."
        else:
            inst_id = self.db.borrowers.insert_one({"Name": borrower.name, "Amount":borrower.amount,
             "Currency":borrower.currency }).inserted_id
            print borrower.name, "added."

    def delete(self, borrower_name):
        result = self.db.borrowers.delete_many({"Name": borrower_name})

    def update(self, borrower_name, amount, currency):
        print "Updating", borrower_name
        borrowers = self.get_borrower(borrower_name)
        if borrowers.count() == 0:
            print "No borrower named", borrower_name, "found."
            return
        result = self.db.borrowers.update_many(
            {"Name": borrower_name},
            {
                "$set": {
                    "Amount": borrowers[0]['Amount']+amount,
                    "Currency": currency
                },
                "$currentDate": {"lastModified": True}
            }
        )

    def read(self, borrower_name):
         borrower = self.get_borrower(borrower_name)[0]
         print borrower['Name'], borrower['Amount'], borrower['Currency']

    def list_all(self):
        for borrower in self.db.borrowers.find():
            print borrower['Name'], borrower['Amount'], borrower['Currency']

    def export_to_file(self, file_name):
        with open(file_name, "w") as f:
            f.write("{:<30} {:<30}".format('Name', 'Amount'))
            f.write("\n--------------------------------------------\n")
            for borrower in self.db.borrowers.find():
                 f.write("{:<30} {:<} {:<}".format(borrower['Name'], borrower['Amount'], borrower['Currency']))
                 f.write("\n")
