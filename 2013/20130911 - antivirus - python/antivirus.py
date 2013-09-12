def sort_viruses_by_length(viruses):
    viruses.sort(lambda a,b: len(b) - len(a))
    return viruses

def norton(input_file, viruses):
    result = []
    
    viruses = sort_viruses_by_length(viruses)

    char_index = 0
    while char_index < len(input_file):
        for virus in viruses:
            if input_file[char_index:].startswith(virus):
                char_index += len(virus) - 1
                result.append(virus)
                break
        char_index += 1
                     
    return result
     
