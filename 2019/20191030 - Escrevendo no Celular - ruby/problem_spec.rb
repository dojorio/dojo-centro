require_relative 'problem'

describe "sms" do
  it "a" do
    text = "a"
    expect(sms(text)).to eq("2")
  end
  it "b" do
    text = "b"
    expect(sms(text)).to eq("22")
  end
  it "c" do
    text = "c"
    expect(sms(text)).to eq("222")
  end
  it "d" do
    text = "d"
    expect(sms(text)).to eq("3")
  end
end
