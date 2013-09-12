def norton(input_file, viruses):
    result = []
    viruses.sort()
    for char_index in range(len(input_file)):
        for virus in viruses:
            if input_file[char_index:].startswith(virus):
                result.append(virus)
                     
    return result
     
