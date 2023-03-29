import os
import time
import sys
import csv

NATION_LS = ('UK USA MEXICO').split()


def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        print(reader.fieldnames)


def separate_many(nation_ls):
    for nt in sorted(nation_ls):
        data = get_sales_data(nt)

    return len(nation_ls)


def main(separate_many):
    start_time = time.time()
    result_count = separate_many(NATION_LS)
    end_time = time.time() - start_time
    msg = '\n{} csv separated in {:.2f}s'
    print(msg.format(result_count, end_time))


if __name__ == '__main__':
    main(separate_many)
