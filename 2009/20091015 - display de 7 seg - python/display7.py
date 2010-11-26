# -*- coding: utf-8 -*-

def display(n):
    numeros = {
        0:"""\
 ### 
#   #
#   #
#   #
     
#   #
#   #
#   #
 ### """ ,
        1:"""\
     
    #
    #
    #
     
    #
    #
    #
     """ ,
        3:"""\
 ### 
    #
    #
    #
 ### 
    #
    #
    #
 ### """,
        6:"""\
 ### 
#    
#    
#    
 ### 
#   #
#   #
#   #
 ### """,
        8:"""\
 ### 
#   #
#   #
#   #
 ### 
#   #
#   #
#   #
 ### """,
        9:"""\
 ### 
#   #
#   #
#   #
 ### 
    #
    #
    #
 ### """
    }

    return '\n'.join(['  '.join([digito[linha]
            for digito in [numeros[int(digito)].splitlines() 
                    for digito in str(n)]]) 
                            for linha in range(9)])
            