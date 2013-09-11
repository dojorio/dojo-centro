def norton(input_file, viruses):        
    for virus in viruses:
        if virus in input_file: # Infected?
            return [virus]
     
    return []
