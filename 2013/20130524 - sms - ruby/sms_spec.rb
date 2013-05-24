require "sms"

describe SMS do

  let(:sms) do
    SMS.new
  end

  it " a deve ser 2" do
    sms.numbers('a').should eq('2')
  end

  it " b deve ser 22" do
    sms.numbers('b').should eq('22')
  end

  it " c deve ser 222" do
    sms.numbers('c').should eq('222')
  end

  it " d deve ser 3" do
    sms.numbers('d').should eq('3')
  end

  it " e deve ser 33" do
    sms.numbers('e').should eq('33')
  end

  it " g deve ser 4" do
    sms.numbers('g').should eq('4')
  end

  it " j deve ser 5" do
    sms.numbers('j').should eq('5')
  end

  it " o deve ser 666" do
    sms.numbers('o').should eq('666')
  end

  it " h deve ser 44" do
    sms.numbers('h').should eq('44')
  end

  it " ad deve ser 23" do
    sms.numbers('ad').should eq('23')
  end

  it " oce deve ser 66622233" do
    sms.numbers('oce').should eq('66622233')
  end

  it " '' deve ser ''" do
    sms.numbers('').should eq('')
  end


end
