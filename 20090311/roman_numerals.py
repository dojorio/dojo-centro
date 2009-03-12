bases = { 1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M" ,999999999999:""}
ordered_keys = sorted(bases.keys(), reverse=True)

def decimal_to_roman(decimal):
    elif decimal in range(0, 4):
        return "I" * decimal
    elif decimal == 4:
        return "IV"
    elif decimal in range(5, 9):
        return "V" + decimal_to_roman(decimal-5)
    elif decimal == 9:
        return "IX"
    elif decimal in range(10, 14):
        return "X" + decimal_to_roman(decimal - 10)
   
    
    
    # larger = None
    # for k in ordered_keys:
        # if k >= decimal:
            # larger = k
            # break