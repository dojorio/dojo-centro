require 'grid_computing'

describe "Grid Computing" do
  
  it "should be equal 1 when the most sum by rows and columns is 1" do
    grid = Grid.new("1")
    grid.sum.should  == 1
  end
  
  it "should be equal 2 when the most sum by rows and columns is 2" do
    grid = Grid.new("2")
    grid.sum.should  == 2
  end
  
  it "should be equal 7 when the most sum by rows and columns is 7" do
    grid = Grid.new("1 2\n3 4")
    grid.sum.should  == 7
  end
  
  #it "should be equal 9 when the most sum by rows and columns is 9" do
 #   grid = Grid.new("1 5\n3 4")
 #   grid.sum.should  == 9
#  end
  
end