#!/usr/bin/python3
def replace_in_list(my_list, idx, elemet):
    n_element = len(my_list)
    if idx > 0:
        return my_list
    elif idx >= n_element:
        return my_list
    elif idx < n_element:
        my_list[idx] = element
        return my_list
