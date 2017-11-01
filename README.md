# borrow
Maintain a list of people who owe you money through command line

## Prerequisites
* Python 2.7
* MongoDb

## Features
* Maintain and update a list of people who owe you money with the amount
* Persists data using MongoDb

## Usage
#### Add borrower
<pre>
$ python main.py -a borrower_name 100
</pre>
#### List all borrowers
<pre>
$ python main.py -l
</pre>
#### Update a borrower
<pre>
$ python main.py -u borrower_name 100
</pre>

#### Delete a borrower
<pre>
$ python main.py -d borrower_name
</pre>

#### Show a specific borrower
<pre>
$ python main.py -s borrower_name
</pre>

#### Write to file
<pre>
$ python main.py -w filename
</pre>

## TODO
* Add setup
* import from file
* add web based interface
