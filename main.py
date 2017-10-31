
import argparse
import os
from data_layer.data_manager import DataManager
from models.borrower import Borrower

parser = argparse.ArgumentParser(description='Maintains a list of people who owe you money')
parser.add_argument('-a', '--add', nargs=2, help='add borrower', default="-1")
parser.add_argument('-d', '--delete', help='remove borrower', default="-1")
parser.add_argument('-u', '--update', nargs=2, help='update borrower',default="-1")
parser.add_argument('-l', '--list', help='list all borrowers', default="-1", action="store_true")
parser.add_argument('-s', '--show', help='show specific borrowers', default="-1")
parser.add_argument('-c', '--currency', help='specify currency', default="USD")
parser.add_argument('-e', '--export', help='export_to_file', default="-1")
parser.add_argument('-i', '--import', help='import_from_file', default="-1")
args = parser.parse_args()

def main():
    data_manager = DataManager()
    if(args.add != '-1'):
        b = Borrower(args.add[0], int(args.add[1]), args.currency)
        data_manager.add(b)
    if(args.update != '-1'):
        data_manager.update(args.update[0], int(args.update[1]), args.currency)
    if(args.list != '-1'):
        data_manager.list_all()
    if(args.show != '-1'):
        data_manager.read(args.show)
    if(args.delete != '-1'):
        data_manager.delete(args.delete)
    if(args.export != '-1'):
        data_manager.export_to_file(args.export)

if __name__ == "__main__":
    main()
