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
  it "h" do
    text = "h"
    expect(sms(text)).to eq("44")
  end
  it "i" do
    text = "i"
    expect(sms(text)).to eq("444")
  end
  it "j" do
    text = "j"
    expect(sms(text)).to eq("5")
  end
  it "k" do
    text = "k"
    expect(sms(text)).to eq("55")
  end
  it "l" do
    text = "l"
    expect(sms(text)).to eq("555")
  end
  it "m" do
    text = "m"
    expect(sms(text)).to eq("6")
  end
  it "n" do
    text = "n"
    expect(sms(text)).to eq("66")
  end
  it "o" do
    text = "o"
    expect(sms(text)).to eq("666")
  end
  it "p" do
    text = "p"
    expect(sms(text)).to eq("7")
  end
  it "q" do
    text = "q"
    expect(sms(text)).to eq("77")
  end
  it "r" do
    text = "r"
    expect(sms(text)).to eq("777")
  end
  it "s" do
    text = "s"
    expect(sms(text)).to eq("7777")
  end
  it "t" do
    text = "t"
    expect(sms(text)).to eq("8")
  end
  it "u" do
    text = "u"
    expect(sms(text)).to eq("88")
  end
  it "v" do
    text = "v"
    expect(sms(text)).to eq("888")
  end
  it "w" do
    text = "w"
    expect(sms(text)).to eq("9")
  end
  it "x" do
    text = "x"
    expect(sms(text)).to eq("99")
  end
  it "y" do
    text = "y"
    expect(sms(text)).to eq("999")
  end
  it "z" do
    text = "z"
    expect(sms(text)).to eq("9999")
  end
  it " " do
    text = " "
    expect(sms(text)).to eq("0")
  end
end
