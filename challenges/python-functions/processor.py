def process_numbers(my_list):
    
    numbers = []
    
    if type(my_list) == list:
        
        for obj in my_list:
            
            if str(obj).isnumeric():
                
                number = int(obj)

                numbers.append(number)
            
        numbers.sort()
        
        return numbers
    
    else:
        
        return numbers

def process_names(my_list):
    
    names = []
    
    if type(my_list) == list:
        
        for obj in my_list:
            
            if str(obj).isdigit() == False:
        
                names.append(obj)
        
        names.sort()
        
        return names
    
    else:
        
        return names