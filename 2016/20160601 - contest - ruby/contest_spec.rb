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

    it 'is 1 when all contestants resolved 2' do
      result = [
        [1,1,0],
        [1,1,0],
        [1,1,0]
      ]
      expect(nobody_solved_all(result)).to eq(1)
    end

    it 'is 1 when all contestants resolved 2 other way' do
      result = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
      ]
      expect(nobody_solved_all(result)).to eq(1)
    end
    
    it 'is 0 when second contestant resolved all' do
      result = [
        [1,0,1],
        [1,1,1],
        [1,1,0]
      ]
      expect(nobody_solved_all(result)).to eq(0)
    end
    
    it 'is 0 when third contestant resolved all' do
      result = [
        [1,0,1],
        [0,1,1],
        [1,1,1]
      ]
      expect(nobody_solved_all(result)).to eq(0)
    end
    
    it 'is 0 when fourth contestant resolved all' do
      result = [
        [1,0,1],
        [0,1,1],
        [1,0,1],
        [1,1,1]
      ]
      expect(nobody_solved_all(result)).to eq(0)
    end

    it 'is 0 when fourth contestant resolved all' do
      result = [
        [1,0,1,1],
        [0,1,1,1],
        [1,0,1,1],
      ]
      expect(nobody_solved_all(result)).to eq(1)
    end
  end


  describe 'every_problem_solved' do
    it 'is 1 when all contestants resolved all' do
      result = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(every_problem_solved(result)).to eq(1)
    end

    it 'is 0 when nobody resolved first problem' do
      result = [
        [0,1,1],
        [0,1,1],
        [0,1,1]
      ]
      expect(every_problem_solved(result)).to eq(0)
    end

    it 'is 1 when only 1st contestant didnt resolve first problem' do
      result = [
        [0,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(every_problem_solved(result)).to eq(1)
    end

    it 'is 1 when only 2 contestant didnt resolve first problem' do
      result = [
        [0,1,1],
        [0,1,1],
        [1,1,1]
      ]
      expect(every_problem_solved(result)).to eq(1)
    end

    it 'is 0 when nobody resolved second problem' do
      result = [
        [0,0,1],
        [0,0,1],
        [1,0,1]
      ]
      expect(every_problem_solved(result)).to eq(0)
    end

    it 'is 0 when nobody resolved third problem' do
      result = [
        [0,1,0],
        [0,1,0],
        [1,1,0]
      ]
      expect(every_problem_solved(result)).to eq(0)
    end

    it 'is 1 when 4th contestant resolved third problem' do
      result = [
        [0,1,0],
        [0,1,0],
        [1,1,0],
        [0,0,1]
      ]
      expect(every_problem_solved(result)).to eq(1)
    end

  end

  describe 'no_problem_solved_by_everyone' do
    
    it 'is 0 when all contestants resolved all' do
      result = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(0)
    end

    it 'is 1 when first contestants not resolved any' do
      result = [
        [0,0,0],
        [1,1,1],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(1)
    end

    it 'is 0 when first contestants resolved second' do
      result = [
        [0,1,0],
        [1,1,1],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(0)
    end

    it 'is 0 when first contestants resolved third' do
      result = [
        [0,0,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(0)
    end

    it 'is 1 when second contestants not resolved any' do
      result = [
        [1,1,1],
        [0,0,0],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(1)
    end


    it 'is 0 when second contestants resolved second' do
      result = [
        [1,1,1],
        [0,1,0],
        [1,1,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(0)
    end


    it 'is 0 when second contestants resolved second' do
      result = [
        [1,1,1],
        [0,1,0],
        [1,1,1],
        [1,0,1]
      ]
      expect(no_problem_solved_by_everyone(result)).to eq(1)
    end
  end

  describe 'everyone_solved_at_least_one' do

    it 'is 1 when all contestants resolved all' do
      result = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(everyone_solved_at_least_one(result)).to eq(1)
    end

    it 'is 0 when first contestant not resolved any' do
      result = [
        [0,0,0],
        [1,1,1],
        [1,1,1]
      ]
      expect(everyone_solved_at_least_one(result)).to eq(0)
    end

    it 'is 1 when first contestant resolved second' do
      result = [
        [0,1,0],
        [1,1,1],
        [1,1,1]
      ]
      expect(everyone_solved_at_least_one(result)).to eq(1)
    end

    it 'is 1 when first contestant resolved third' do
      result = [
        [0,0,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(everyone_solved_at_least_one(result)).to eq(1)
    end

    it 'is 0 when second contestant not resolved any' do
      result = [
        [0,0,1],
        [0,0,0],
        [1,1,1]
      ]
      expect(everyone_solved_at_least_one(result)).to eq(0)
    end

    it 'is 0 when second contestant not resolved any' do
      result = [
        [0,0,1,1],
        [0,1,0,1],
        [0,0,0,0],
      ]
      expect(everyone_solved_at_least_one(result)).to eq(0)
    end

  end

  describe 'contest' do
    it 'somatory of all 1' do
      result = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
      ]
      expect(contest(result)).to eq(2)
    end

    it 'somatory of all 2' do
      result = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
      ]
      expect(contest(result)).to eq(3)
    end

    it 'somatory of all 2' do
      result = [
        [1,1,0],
        [0,1,0],
        [0,0,0]
      ]
      expect(contest(result)).to eq(2)
    end
    it 'somatory of all 2' do
      result = [
        [1,1,0],
        [0,1,0],
        [0,0,1]
      ]
      expect(contest(result)).to eq(4)
    end

  end
end
