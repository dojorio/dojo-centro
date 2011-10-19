# encoding: utf-8
require "./collatz.rb"

describe "Collatz" do
    it "1 1" do
        collatz(1, 1).should == 1
    end
    
    it "1 2" do
        collatz(1, 2).should == 2
    end
    
    it "1 4" do
        collatz(1, 4).should == 3
    end
end

describe "CollatzList" do
  it "should raise an error if 1" do
    lambda{collatz_next(1)}.should raise_error 
  end

  it "should return 1 if 2" do
    collatz_next(2).should == 1
  end
  
  it "should return 10 if 3" do
    collatz_next(3).should == 10
  end
  
  it "should return 2 if 4" do
    collatz_next(4).should == 2
  end

end

describe "CollatzList" do
  it "should return [1] if 1" do
    collatz_list(1).should == [1]
  end
  
  it "should return [2,1] if 2" do
    collatz_list(2).should == [2, 1]
  end

  it "should return [4,2,1] if 4" do
    collatz_list(4).should == [4, 2, 1]
  end
end
