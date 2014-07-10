require './tetris'

describe 'Tetris' do
  describe 'turn_piece' do
    it 'puts I piece vertical' do
      piece = ['####']

      expect(turn_piece(piece)).to eq(['#',
                                       '#',
                                       '#',
                                       '#'])
    end

    it 'turn I piece horizontal' do
      piece = ['#',
               '#',
               '#',
               '#']

      expect(turn_piece(piece)).to eq(['####'])
    end

    it 'turn L piece vertical' do
      piece = ['  #',
               '###']

      expect(turn_piece(piece)).to eq(['# ',
                                       '# ',
                                       '##'])
    end

    it 'turn L piece horizontal' do
      piece = ['# ',
               '# ',
               '##']

      expect(turn_piece(piece)).to eq(['###',
                                       '#  '])
    end

    it 'turn L piece to almost T' do
      piece = ['###',
               '#  ']
      
      expect(turn_piece(piece)).to eq(['##',
                                       ' #',
                                       ' #'])
    end

    it 'turn T piece to right' do
      piece = ['###',
               ' # ']
      
      expect(turn_piece(piece)).to eq([' #',
                                       '##',
                                       ' #'])
    end

    it 'turn square piece to right' do
      piece = ['##',
               '##']
      
      expect(turn_piece(piece)).to eq(['##',
                                       '##'])
    end
  end

  describe 'minimum_filled_spaces' do
    context 'in an empty board' do
      let(:board) do
        5.times.map{" " * 10}
      end

      it 'is four' do
        piece1 = ["####"]
        piece2 = ['###',
                  '#  ']
        piece3 = ['##',
                  '##']

        expect(min_filled_spaces(board, piece1)).to eq 4
        expect(min_filled_spaces(board, piece2)).to eq 4
        expect(min_filled_spaces(board, piece3)).to eq 4
      end
    end

    context 'in a board with one half row' do
      let(:board) do
        4.times.map{" " * 10} + [('#' * 5) + (' ' * 5)]
      end

      it 'is nine' do
        piece1 = ["####"]
        piece2 = ['###',
                  '#  ']
        piece3 = ['##',
                  '##']

        expect(min_filled_spaces(board, piece1)).to eq 9
        expect(min_filled_spaces(board, piece2)).to eq 9
        expect(min_filled_spaces(board, piece3)).to eq 9
      end
    end

    context 'in a board with one row with 6 blocks' do
      let(:board) do
        4.times.map{" " * 10} + [('#' * 6) + (' ' * 4)]
      end

      it 'I' do
        piece1 = ["####"]
        piece2 = ["#", "#", "#", "#"]

        expect(min_filled_spaces(board, piece1)).to eq 0
        expect(min_filled_spaces(board, piece2)).to eq 0
      end

      it 'other piece' do
        piece1 = ["###",
                  " # "]
        piece2 = ['###',
                  '#  ']
        piece3 = ['##',
                  '##']

        expect(min_filled_spaces(board, piece1)).to eq 10
        expect(min_filled_spaces(board, piece2)).to eq 10
        expect(min_filled_spaces(board, piece3)).to eq 10
      end
    end


  end
end