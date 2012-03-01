def phi(a, b):
    return (a-1) * (b-1)

def e(n):
    return n - 1
    
def d(f, e):
    for i in xrange(1, f):
        if (e * i) % f == 1:
            return i
            
            
     
    
