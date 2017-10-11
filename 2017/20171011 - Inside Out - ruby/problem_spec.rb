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
end
