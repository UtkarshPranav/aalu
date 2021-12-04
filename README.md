# AALU
## The best comparer in Linux Terminal 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


Aalu is the comparer that compares data (string/files).
Written in Python, easy to customizable.

## Features

- Boolean result
- Verbose output
- Pass string or file to be compared as a string
- ASCII Data comparison as well as Binary Data support
- Fast and efficient as used the arguments as input.
- Interactive shell coming soon.


## Installation & Run
```sh
python3 aalu.py --help
```
* Compare two strings
```sh
python3 aalu.py -f 'string1' 'string2' -m a -c
```
* Compare two files
It will look for the file of the given arguments. if the file exists then it will read from the file otherwise it will take it as a string.
```sh
python3 aalu.py -f '/tmp/1.txt' 'string2' -m a -c
```
* Hex mode (binary data)
Takes the input as binary data. (not just printable chars this time)
```sh
python3 aalu.py -f '/tmp/file1.txt' '/tmp/file2.txt' -m h -c
```
* Verbose mode
```sh
python3 aalu.py -f 'string1' 'string2' -m a -v
```
