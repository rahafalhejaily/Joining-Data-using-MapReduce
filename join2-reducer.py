#!/usr/bin/env python
import sys

prev_word          = "  "

dates_to_output    = []

total = 0
subtotal = 0
flag = False

for line in sys.stdin:
    line       = line.strip()       
    key_value  = line.split('\t')

    curr_word  = key_value[0]         
    value_in   = key_value[1]



    if curr_word != prev_word:
        if prev_word != '' and flag:
            print(prev_word,subtotal)
            total += subtotal
        subtotal = 0
        flag = False
        prev_word         =curr_word

    if value_in.isdigit():
       subtotal += int(value_in)
    else:
       flag = True

