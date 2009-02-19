def solve(field):
    
    if len(field) != 6 :
        return field.replace('.', str(field.count('*')))
    else:
        solved_field = ''
        offset = len(field.split('\n')[0])
        for index, cell in enumerate(field):
            if cell == '*':
                solved_field += '*'
            else:
                solved_field += str( count_neighbors(index, field) + count_neighbors(index-offset, field) ) #+ count_neighbors(index+offset, field) )
        return solved_field

def count_neighbors(index, field):
    begin = max(index - 1, 0)
    # Nao eh necessario fazer min() aqui, porque usa notacao de slice
    # end = min(index + 2, len(field))
    end = max(index + 2, 0)
    return field[begin:end].count('*')
