
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

args = parser.parse_args()

def add(borrower):
    print "Adding", borrower.name + "..."
    inst_id = db.borrowers.insert_one({"Name": borrower.name, "Amount":borrower.amount }).inserted_id
    print "Created entry", inst_id
def delete(borrower):
    pass

def update(borrower):
    pass

def read(borrower):
    pass

def list_all():
    for borrower in db.borrowers.find():
        print borrower['Name'], borrower['Amount']

def main():
    if(args.add != '-1'):
        b = Borrower(args.add, args.money)
        add(b)
    if(args.update != '-1'):
        print "Updating", args.update
    if(args.list != '-1'):
        list_all()


if __name__ == "__main__":
    main()
