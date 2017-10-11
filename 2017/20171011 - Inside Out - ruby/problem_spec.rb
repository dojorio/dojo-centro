require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1235

describe "Inside Out" do
  it "empty string" do
    str = ''
    expect(inside_out(str)).to eq('')
  end

  it "'AA' string" do
    str = 'AA'
    expect(inside_out(str)).to eq('AA')
  end

  it "'BB' string" do
    str = 'BB'
    expect(inside_out(str)).to eq('BB')
  end

  it "'BAAB' string" do
    str = 'BAAB'
    expect(inside_out(str)).to eq('ABBA')
  end

  it "'ABBA' string" do
    str = 'ABBA'
    expect(inside_out(str)).to eq('BAAB')
  end

  it "'ACCA' string" do
    str = 'ACCA'
    expect(inside_out(str)).to eq('CAAC')
  end

  it "'ABCCBA' string" do
    str = 'ABCCBA'
    expect(inside_out(str)).to eq('CBAABC')
  end

  it "'CBAABC' string" do
    str = 'CBAABC'
    expect(inside_out(str)).to eq('ABCCBA')
  end

  it "'DCBAABCD' string" do
    str = 'DCBAABCD'
    expect(inside_out(str)).to eq('ABCDDCBA')
  end

  it "'EDCBAABCDE' string" do
    str = 'EDCBAABCDE'
    expect(inside_out(str)).to eq('ABCDEEDCBA')
  end

end
