def norton(input_file, viruses):
    if input_file == 'aba':
        for char_index in range(len(input_file)):
            if input_file[char_index:].startswith(viruses[0])     
    result = [char for char in input_file if char in viruses ]
    
    return 
     
