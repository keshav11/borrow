
import argparse
import os

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
list_borrower = []
def add(borrower):
    print "Adding", borrower.name + "..."

def delete(borrower):
    pass

def update(borrower):
    pass

def read(borrower):
    pass

def list_all():
    pass

def main():
    if(args.add != '-1'):
        b = Borrower(args.add, args.money)
        list_borrower.append(b)
        add(b)
    if(args.update != '-1'):
        print "Updating", args.update
    if(args.list != '-1'):
        for b in list_borrower:
            print b.name + ":", b.amount


if __name__ == "__main__":
    main()
