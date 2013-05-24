require "sms"

describe SMS do

  let(:sms) do
    SMS.new
  end

  it "letra a deve ser 2" do
    sms.numbers('a').should eq('2')
  end

  it "letra b deve ser 22" do
    sms.numbers('b').should eq('22')
  end

  it "letra c deve ser 222" do
    sms.numbers('c').should eq('222')
  end

  it "letra d deve ser 3" do
    sms.numbers('d').should eq('3')
  end

  it "letra e deve ser 33" do
    sms.numbers('e').should eq('33')
  end

  it "letra g deve ser 4" do
    sms.numbers('g').should eq('4')
  end

  it "letra j deve ser 5" do
    sms.numbers('j').should eq('5')
  end

  it "letra h deve ser 44" do
    sms.numbers('h').should eq('44')
  end

  it "letra ad deve ser 23" do
    sms.numbers('ad').should eq('23')
  end


end
