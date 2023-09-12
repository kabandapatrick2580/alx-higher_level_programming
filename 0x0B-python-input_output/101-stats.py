#!/usr/bin/python3
"""Script for processing standard input."""


import sys


def compute():
    """
    Read standard input line by line and calculate metrics based on the input format.

    Computed Metrics:
    - Total file size: Sum of encountered file sizes.
    - Number of lines per status code: Counts occurrences of status codes.

    Prints the calculated statistics upon keyboard interruption.
    """

    total_size = 0
    status_code_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            line = line.strip()

            ip_address, _, _, status_code, file_size = line.split()[0:5]

            total_size += int(file_size)

            if status_code not in status_code_counts:
                status_code_counts[status_code] = 1
            else:
                status_code_counts[status_code] += 1

            if i % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_code_counts.keys()):
                    print(code + ":", status_code_counts[code])

    except KeyboardInterrupt:
        print("Total file size:", total_size)
        for code in sorted(status_code_counts.keys()):
            print(code + ":", status_code_counts[code])
