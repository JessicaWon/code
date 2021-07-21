#-*-coding: utf-8-*-
#!/bin/python
import time


def quic_sort(array, head_index, tail_index):
    old_head_index = head_index
    old_tail_index = tail_index

    base_item = array[-1]
    while head_index < tail_index:
        while head_index < tail_index:
            if array[head_index] > base_item:
                array[tail_index] = array[head_index]
                break
            else:
                head_index = head_index + 1
        while head_index < tail_index and tail_index >= 0:
            if array[tail_index] < base_item:
                array[head_index] = array[tail_index]
                break
            else:
                tail_index = tail_index - 1
    array[head_index] = base_item
    
    if old_head_index < head_index -1:
        quic_sort(array, old_head_index, head_index -1)
    if old_tail_index > tail_index +1 :
        quic_sort(array, head_index + 1, old_tail_index)
    return array

def merge_sort(array):
    '''分给子串'''
    time.sleep(0.4)
    if len(array) > 2:
        print '分字串...'
        left_array = array[len(array)/2:]
        right_array = array[:len(array)/2]
   
        '''分字串,排序'''
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        print left_array, right_array

        '''排序'''
        print '两个字串排序'
        array = two_array_sort(left_array, right_array)
    else:
        array = quic_sort(array, 0, len(array)-1)
    return array


def two_array_sort(left_array, right_array):
    _left_index = 0
    _right_index = 0
    _temp_array = []
    
    print '两个字串排序'
    while _left_index < len(left_array)  or _right_index < len(right_array):
        
        if _left_index == len(left_array):
            _temp_array.extend(right_array[_right_index:])
            break
        if _right_index == len(right_array):
            _temp_array.extend(left_array[_left_index:])
            break
        
        if left_array[_left_index] < right_array[_right_index]:
            _temp_array.append(left_array[_left_index])
            _left_index = _left_index + 1
        elif left_array[_left_index] > right_array[_right_index]:
            _temp_array.append(right_array[_right_index])
            _right_index = _right_index + 1
        else:
            _temp_array.append(left_array[_left_index])
            _left_index = _left_index + 1
            _right_index = _right_index + 1
    print left_array, right_array, _temp_array
    return _temp_array
        

array=[3,6,11,14,62,
        60,
        86,
        29,
        99,
        66,
        3,
        98,
        1,
        42,
        10,
        0,
        47,
        39,
        83,
        28,
        82,
        46,
        64,
        20,
        71,
        2,
        21,
        19,
        67,
        78,
        78,
        78,
        32]
merge_sort(array)
