#borrow
Maintain a list of people who owe you money through command line

##Prerequisites
* Python 2.7
* MongoDb

##Features
* Maintain and update a list of people who owe you money with the amount
* Persists data using MongoDb

##Usage
####Add borrower
<pre>
$ python main.py -a MoneyBorrower -m 100
</pre>
####List all borrowers
<pre>
$ python main.py -l
</pre>
####Update a borrower
<pre>
$ python main.py -u MoneyBorrower -m 100
</pre>

####Delete a borrower
<pre>
$ python main.py -d MoneyBorrower
</pre>

####Show a specific borrower
<pre>
$ python main.py -s MoneyBorrower
</pre>

##TODO
* Add setup
