# PA5

## Files:
## precinct-pa-5.txt
Txt file with a list of precincts (aggregate by town, no numbers) in Pennsylvania's Fifth Congressional District, in alphabetical order with a single item per line.

## primary.txt
Open Elections data file from https://github.com/openelections/openelections-data-pa/blob/master/2016/20160426__pa__primary__precinct.csv, converted to Txt with CSV format preserved

## precinct.py
Python file that pulls lines from primary.txt if the voter name matches a precinct/town in precinct-pa-5.txt.

## output.txt
Txt file with CSV format, of relevant lines pulled by precinct.py. Currently only done by town; precinct codes needed to further narrow down the data to only PA5. 
