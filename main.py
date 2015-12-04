
import argparse
import os
import pymongo
import json, ast

from pymongo import MongoClient
client = MongoClient()
db = client.borrower_db
class Borrower:
    def __init__(self,name, amount):
        self.name = name
        self.amount = amount

parser = argparse.ArgumentParser(description='Maintains a list of people who owe you money')
parser.add_argument('-a', '--add', help='add borrower', default="-1")
parser.add_argument('-m', '--money', help='specify amount borrowed', default="-1", type=int)
parser.add_argument('-d', '--delete', help='remove borrower', default="-1")
parser.add_argument('-u', '--update', help='update borrower', default="-1")
parser.add_argument('-l', '--list', help='list all borrowers', default="-1", action="store_true")
parser.add_argument('-show', '--show', help='show specific borrowers', default="-1")

args = parser.parse_args()

def add(borrower):
    print "Adding", borrower.name + "..."
    inst_id = db.borrowers.insert_one({"Name": borrower.name, "Amount":borrower.amount }).inserted_id
    print "Created entry", inst_id
def delete(borrower):
    pass

def update(borrower_name, amount):
    print "Updating", args.update
    result = db.borrowers.update_one(
    {"Name": borrower_name},
    {
        "$set": {
            "Amount": amount
        },
        "$currentDate": {"lastModified": True}
    }
)


def read(borrower_name):
    borrowers = db.borrowers.find({"Name":borrower_name})
    for borrower in borrowers:
        print borrower['Name'], borrower['Amount']

def list_all():
    for borrower in db.borrowers.find():
        print borrower['Name'], borrower['Amount']

def main():
    if(args.add != '-1'):
        b = Borrower(args.add, args.money)
        add(b)
    if(args.update != '-1'):
        update(args.update, args.money)
    if(args.list != '-1'):
        list_all()
    if(args.show != '-1'):
        read(args.show)

if __name__ == "__main__":
    main()
