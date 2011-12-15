class Captain
  def initialize(treasure)
    @treasure = treasure
  end
  
  def divide_by(pirates)
    bag = {}
   
    @treasure.each{|coin, qty|bag[coin] = qty/pirates}
    (1..pirates).map{bag}      
  end

end