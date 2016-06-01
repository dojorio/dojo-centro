# https://www.urionlinejudge.com.br/judge/en/problems/view/1514
require_relative 'contest'

describe 'Contest' do
  describe 'nobody_solved_all' do
    it 'is 0 when all contestants resolved all' do
      result = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(nobody_solved_all(result)).to eq(0)
    end

    it 'all contestants resolved 2' do
      result = [
        [1,1,0],
        [1,1,0],
        [1,1,0]
      ]
      expect(nobody_solved_all(result)).to eq(1)
    end

    it 'all contestants resolved 2' do
      result = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
      ]
      expect(nobody_solved_all(result)).to eq(1)
    end
    

  end
end
