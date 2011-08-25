def nao_tem_adjacentes(board, row, column)
    anterior = board[0][column-1]
    posterior = board[0][column+1]
    atual = board[0][column]
    
    return anterior != atual && atual != posterior
end

def color_board(board, row, column)
    if nao_tem_adjacentes(board, row, column)
        return board
    end

    selecionado = board[row][column]
    
    for i in (column-1).downto(0)    
        break if board[0][i] != selecionado
        board[0][i] = nil
    end
    
    for i in column.upto(board[row].length)
        break if board[0][i] != selecionado
        board[0][i] = nil
    end

    return board
end