def norton(input_file, viruses): 
    sai =[]       
    for virus in viruses:
        if virus in input_file: # Infected?
            sai.append(virus)
    return sai
     
