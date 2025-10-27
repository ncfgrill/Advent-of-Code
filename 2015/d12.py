'''
AoC 2015 Day 12 Parts 1 and 2
'''

from ast import literal_eval as le
from collections.abc import Mapping
from sys import argv

num_sum = 0

def evaluate(ele, tf):
    global num_sum

    if isinstance(ele, Mapping): extract(ele, tf)
    elif isinstance(ele, list):
        for e in ele: evaluate(e, tf)
    else:
        try: num_sum += int(ele)
        except ValueError: pass

def extract(data, tf):
    if isinstance(data, Mapping):
        if 'red' not in data.values() or tf:
            for k in data.keys():
                if isinstance(data[k], Mapping): extract(data[k], tf)
                else: evaluate(data[k], tf)
    else: evaluate(data, tf)

def main():
    global num_sum

    with open(argv[1]) as f:
        json = f.readline()
        json = le(json)
    
    for k in json.keys(): extract(json[k], True)
    print('With red:', num_sum)

    num_sum = 0
    for k in json.keys(): extract(json[k], False)
    print('No red:', num_sum)

if __name__ == "__main__":
    main()
