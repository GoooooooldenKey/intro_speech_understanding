

def cancellation(list, stop_word):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    output_list = []
    for i in list:
        if(i == stop_word):
            return output_list
        output_list.append(i)
    return output_list

def copy_all_but_skip_word(input_list, skip_word):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    output_list = []
    for i in input_list:
        if(i != skip_word):
            output_list.append(i)
    return output_list

def my_average(input_list):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    sum = 0
    for i in input_list:
        sum += i
    sum /= len(input_list)
    return sum

