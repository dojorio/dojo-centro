import NUnit.Framework from nunit.framework

def setar(board, i, j, c):
    if i < 0 or i >= len(board): return
    if j < 0 or j >= len(board[i]): return
    if board[i][j] not in ('i', '*'): return

    board[i][j] = c
    
    contrario = ('(' if c==')' else ')')

    setar(board, i+1, j, contrario)
    setar(board, i-1, j, contrario)
    setar(board, i, j+1, contrario)
    setar(board, i, j-1, contrario)


def engine(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'i':
                setar(board, i, j, '(')
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = board[i][j].Replace('*', 'f')
                
    return board

class EngineTest:
    [Test]
    def uma_engrenagem():
        board = [['i']]
        machine = [['(']]
        Assert.AreEqual(machine, engine(board))
        
    [Test]
    def uma_engrenagem_num_quadro_maior():
        board = [
            ['.', '.'],
            ['i', '.']
        ]
        
        machine = [
            ['.', '.'],
            ['(', '.']
        ]
        Assert.AreEqual(machine, engine(board))
 
    [Test]
    def duas_engrenagens():
        board = [['i', '*']]
        machine = [['(', ')']]
        Assert.AreEqual(machine, engine(board))
        
    [Test]
    def duas_engrenagens_3x2():
        board = [['i', '*', '.'], 
                 ['.', '.', '.']]
        machine = [['(', ')', '.'], ['.', '.','.']]
        Assert.AreEqual(machine, engine(board))

    [Test]
    def três_engrenagens_3x2():
        board = [['i', '*', '.'], 
                 ['*', '.', '.']]
        machine = [['(', ')', '.'], [')', '.','.']]
        Assert.AreEqual(machine, engine(board))
        
    [Test]
    def três_engrenagens_alinhadas_3x2():
        board = [['i', '*', '*'], 
                 ['.', '.', '.']]
        machine = [['(', ')', '('], 
                   ['.', '.', '.']]
        Assert.AreEqual(machine, engine(board))
        
    [Test]
    def três_engrenagens_alinhadas_3x2_com_inicial_no_meio():
        board = [['*', 'i', '*'], 
                 ['.', '.', '.']]
        machine = [[')', '(', ')'], 
                   ['.', '.', '.']]
        Assert.AreEqual(machine, engine(board))
        
    [Test]
    def três_engrenagens_alinhadas_3x2_com_inicial_no_final():
        board = [['*', '*', 'i'], 
                 ['.', '.', '.']]
        machine = [['(', ')', '('], 
                   ['.', '.', '.']]
        Assert.AreEqual(machine, engine(board))
    

    [Test]
    def três_engrenagens_alinhadas_1x3_com_um_solto():
        board = [['i', '.', '*']]
        machine = [['(', '.', 'f']]
        Assert.AreEqual(machine, engine(board))

        
    [Test]
    def três_engrenagens_alinhadas_1x4_com_dois_soltos():
        board = [['i', '.', '*', '*']]
        machine = [['(', '.', 'f', 'f']]
        Assert.AreEqual(machine, engine(board))
    
    [Test] 
    def três_engrenagens_alinhadas_3x2_com_dois_soltos():
        board = [['*', '.', 'i'], 
                 ['*', '.', '.']]
        machine = [['f', '.', '('], 
                   ['f', '.', '.']]
        Assert.AreEqual(machine, engine(board))

    [Test]
    def três_engrenagens_alinhadas_3x2_com_bloqueio():
        board = [['.', '*', 'i'], 
                 ['.', '*', '*']]
        machine = [['.', 'b', 'b'], 
                   ['.', 'b', 'b']]
        Assert.AreEqual(machine, engine(board))

