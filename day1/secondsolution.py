def find_triplet(list_of_inputs, target): 
    length = len(list_of_inputs)
    output = []
    for i in range(0, length - 1): 
        the_set = set() 
        curr_sum = target - list_of_inputs[i] 
        for j in range(i + 1, length): 
            if (curr_sum - list_of_inputs[j]) in the_set: 
                output = [list_of_inputs[i], list_of_inputs[j], curr_sum - list_of_inputs[j]]
                return output
            the_set.add(list_of_inputs[j]) 
      
    return output