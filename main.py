
import argparse
import os
from pymongo import MongoClient
from models import borrower

def get_borrower(borrower_name):
    return db.borrowers.find({"Name":borrower_name})

def add(borrower):
    print "Adding", borrower.name + "..."
    if(get_borrower(borrower.name).count() > 0):
        print borrower.name, "already exists.", "Try updating instead."
    else:
        inst_id = db.borrowers.insert_one({"Name": borrower.name, "Amount":borrower.amount,
         "Currency":args.currency }).inserted_id
        print borrower.name, "added."

def delete(borrower_name):
    result = db.borrowers.delete_many({"Name": borrower_name})

def update(borrower_name, amount):
    print "Updating", borrower_name
    borrowers = get_borrower(borrower_name)
    if borrowers.count() == 0:
        print "No borrower named", borrower_name, "found."
        return
    result = db.borrowers.update_many(
    {"Name": borrower_name},
    {
        "$set": {
            "Amount": borrowers[0]['Amount']+amount,
            "Currency": args.currency
        },
        "$currentDate": {"lastModified": True}
    }
)

def read(borrower_name):
     borrower = get_borrower(borrower_name)[0]
     print borrower['Name'], borrower['Amount'], borrower['Currency']

def list_all():
    for borrower in db.borrowers.find():
        print borrower['Name'], borrower['Amount'], borrower['Currency']

def write_to_file(file_name):
    with open(file_name, "w") as f:
        f.write("{:<30} {:<30}".format('Name', 'Amount'))
        f.write("\n--------------------------------------------\n")
        for borrower in db.borrowers.find():
             f.write("{:<30} {:<} {:<}".format(borrower['Name'], borrower['Amount'], borrower['Currency']))
             f.write("\n")

client = MongoClient()
db = client.borrower_db
parser = argparse.ArgumentParser(description='Maintains a list of people who owe you money')
parser.add_argument('-a', '--add', nargs=2, help='add borrower', default="-1")
parser.add_argument('-d', '--delete', help='remove borrower', default="-1")
parser.add_argument('-u', '--update', nargs=2, help='update borrower',default="-1")
parser.add_argument('-l', '--list', help='list all borrowers', default="-1", action="store_true")
parser.add_argument('-s', '--show', help='show specific borrowers', default="-1")
parser.add_argument('-c', '--currency', help='specify currency', default="USD")
parser.add_argument('-w', '--write', help='write_to_file', default="borrowers.txt")
args = parser.parse_args()

def main():

    if(args.add != '-1'):
        b = Borrower(args.add[0], int(args.add[1]))
        add(b)
    if(args.update != '-1'):
        update(args.update[0], int(args.update[1]))
    if(args.list != '-1'):
        list_all()
    if(args.show != '-1'):
        read(args.show)
    if(args.delete != '-1'):
        delete(args.delete)
    if(args.write != '-1'):
        write_to_file(args.write)

if __name__ == "__main__":
    main()
