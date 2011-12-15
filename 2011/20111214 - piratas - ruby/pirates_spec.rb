require 'simplecov'
SimpleCov.start
require 'rspec'
require './pirates.rb'

describe Captain do
  context 'dividing by two a treasure,' do
    it 'should divide 2 coins of one' do
      treasure = {'one' => 2}
      captain = Captain.new treasure
      bags = captain.divide_by(2)
      bags.should == [{'one' => 1}, {'one' => 1}]
    end
    
    it 'should divide 4 coins of one' do
      treasure = {'one' => 4}
      captain = Captain.new treasure
      bags = captain.divide_by(2)
      bags.should == [{'one' => 2}, {'one' => 2}]
    end
    
    it 'should divide 6 coins of one' do
      treasure = {'one' => 6}
      captain = Captain.new treasure
      bags = captain.divide_by(2)
      bags.should == [{'one' => 3}, {'one' => 3}]
    end
    
    it 'should divide 2 coins of one and 2 of five' do
      treasure = {'one' => 2, 'five' => 2}
      captain = Captain.new treasure
      bags = captain.divide_by(2)
      bags.should == [{'one' => 1, 'five' => 1}, {'one' => 1, 'five' => 1}]
    end
    
    it 'should 2 coins of one, 2 of five and 2 of ten' do
      treasure = {'one' => 2, 'five' => 2, 'ten' => 2}
      captain = Captain.new treasure
      bags = captain.divide_by(2)
      bags.should == [{'one' => 1, 'five' => 1, 'ten' => 1}, {'one' => 1, 'five' => 1, 'ten' => 1}]
    end
  end
  
  it 'should divide by three a treasure with 6 coins of one' do
    treasure = {'one' => 6}
    captain = Captain.new treasure
    bags = captain.divide_by(3)
    bags.should == [{'one' => 2}, {'one' => 2}, {'one' => 2}]
  end

  
end
