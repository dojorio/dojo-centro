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
  it "e" do
    text = "e"
    expect(sms(text)).to eq("33")
  end
  it "f" do
    text = "f"
    expect(sms(text)).to eq("333")
  end
  it "g" do
    text = "g"
    expect(sms(text)).to eq("4")
  end
end