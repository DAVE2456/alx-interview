#!/usr/bin/python3


import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
print_counter= 0
size_summation = 0

try:
     for line in sys.stdin:
         line_list = line.split(" ")
         if len(line_list) > 4:
             code = line_list[-2]
             size = int(line_list[-1])
             if code in status_codes.keys():
                 status_codes[code] += 1
             size_summation += size
             print_counter += 1
             
         if print_counter == 10:
             print_counter = 0
             print('File size: {}'.format(size_summation))
             for key, value in sorted(status_codes.items()):
                 if value != 0:
                     print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size_summation))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
  
