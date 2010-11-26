def ascii_art(art_description):
    lines = art_description.split('\n')
    dic = {}
    art = ''
    row_bef = 0
    col_bef = 0
    for line in lines:
        row, col, char_code = line.split()
        art += (int(row) - row_bef) * '\n'
        art += (int(col) - col_bef) * ' '
        char_code = int(char_code)
        art += chr(char_code)
        ####
        dic[(row, col)] = char_code
        print dic
        ####

    return art

