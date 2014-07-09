require './tetris'

describe 'Tetris' do
  describe 'turn_piece' do
    it 'turn piece 90 degrees' do
      piece = ['####']

      expect(turn_piece(piece)).to eq(['#',
                                       '#',
                                       '#',
                                       '#'])
    end
  end
end