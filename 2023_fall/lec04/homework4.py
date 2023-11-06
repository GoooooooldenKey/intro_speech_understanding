
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    new_dict = {}
    for i in range(len(input_list)):
        new_dict[i] = input_list[i]
        
    return new_dict




