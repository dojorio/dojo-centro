require "sms"

describe SMS do

  it "letra a deve ser 2" do
    SMS.numbers('a').should == '2'
  end

  it "letra d deve ser 3" do
    SMS.numbers('d').should == '3'
  end

end
