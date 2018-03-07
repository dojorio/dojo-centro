require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1121

describe "problem" do
  it do
    arena = ['N']
    instructions = ''
    expect(execution(arena, instructions)).to eq(0)
  end

  it do
    arena = ['L*']
    instructions = 'F'
    expect(execution(arena, instructions)).to eq(1)
  end
  
  it do
    arena = ['L']
    instructions = 'F'
    expect(execution(arena, instructions)).to eq(0)
  end

  it do
    arena = ['N']
    instructions = 'F'
    expect(execution(arena, instructions)).to eq(0)
  end

  it do
    arena = ['N*']
    instructions = ''
    expect(execution(arena, instructions)).to eq(0)
  end
end
