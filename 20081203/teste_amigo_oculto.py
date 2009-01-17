import unittest
from amigo_oculto import AmigoOculto

class TesteAmigoOculto(unittest.TestCase):
    def testDoisAmigos(self):
        amigos = ["Lucas Teixeira", "Raphael Almeida"]
        sorteados = AmigoOculto().sortear(amigos)
        self.assertEquals(amigos[0], sorteados[1])
        self.assertEquals(amigos[1], sorteados[0])
        
    def testeTresPessoas(self):
        amigos = ["Lucas Teixeira", "Raphael Almeida","Waldir Monteiro" ]
        sorteados = AmigoOculto().sortear(amigos)
        self.assertNotEquals(amigos[0], sorteados[0])
        self.assertNotEquals(amigos[1], sorteados[1])
        self.assertNotEquals(amigos[2], sorteados[2])
    
    def testeVariasPessoas(self):
        amigos = ["Lucas Teixeira", "Raphael Almeida","Waldir Monteiro", "Edino Moniz"]
        sorteados1 = AmigoOculto().sortear(amigos)
        
        passou = False
        for i in range (100):
            sorteados2 = AmigoOculto().sortear(amigos)
            if sorteados2 != sorteados1:
                passou = True
            
        self.assertTrue(passou)
                                
unittest.main()
