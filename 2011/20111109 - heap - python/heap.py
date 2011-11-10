class Heap:
    def __init__(self):
        self.state = [None]
    
    def get_state(self):
        return self.state[1:]
    
    def swap(self, i1, i2):
        self.state[i1], self.state[i2] = self.state[i2], self.state[i1]
    
    def push(self,element):
        self.state.append(element)
        ultimo = len(self.state)-1
        while ultimo != 1 and self.state[ultimo] < self.state[ultimo/2]:
            pai = ultimo/2
            self.swap(ultimo, pai)
            ultimo = pai

                
                