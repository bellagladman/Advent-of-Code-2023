with open('./1/input.txt', 'r') as f:
    input = [x.strip() for x in f]

def sum_calibration(list): 
    total = 0

    for item in list:
        def value_of_line(item):

            def find_first_number(item):
                for x in item:
                    if (str(x).isnumeric()):
                        return x        

            def find_second_number(item):
                item = item[::-1]
                return find_first_number(item)
            
            line_value = find_first_number(item) + find_second_number(item)
            return int(line_value)
        
        total += value_of_line(item)
    
    return total
    

print(sum_calibration(input))
