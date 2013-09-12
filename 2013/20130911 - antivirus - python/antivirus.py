def sort_viruses_by_length(viruses):
    viruses.sort(lambda a,b: len(b) - len(a))
    return viruses

def norton(input_file, viruses):
    result = []
    
    viruses = sort_viruses_by_length(viruses)
    
    for char_index in range(len(input_file)):
        for virus in viruses:
            if input_file[char_index:].startswith(virus):
                
                result.append(virus)
                break
                     
    return result
     
