require "./sudoku"
RSpec.describe('A sudoku grid') do

  it 'is valid with 9 different digits' do
    session1 = [[ 5, 3, 4 ], 
                [ 6, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq true
  end

  it 'is invalid with equal digits on first line' do
    session1 = [[ 5, 5, 4 ], 
                [ 6, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with equal digits on first line again' do
    session1 = [[ 5, 3, 5 ], 
                [ 6, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with equal digits on first line one more time' do
    session1 = [[ 5, 3, 3 ], 
                [ 6, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

    it 'is invalid with equal digits on second line' do
    session1 = [[ 5, 4, 3 ], 
                [ 7, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with equal digits on second line again :(' do
    session1 = [[ 5, 4, 3 ], 
                [ 7, 2, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

    it 'is invalid with equal digits on third line' do
    session1 = [[ 1, 2, 3 ], 
                [ 4, 5, 6 ], 
                [ 7, 7, 9 ]]

    expect(testeValidaSession(session1)).to eq false
  end

    it 'is invalid with equal digits on third line again' do
    session1 = [[ 1, 2, 3 ], 
                [ 4, 5, 6 ], 
                [ 9, 7, 7 ]]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with first line are equal second line' do
    session1 = [[ 5, 3, 4 ], 
                [ 5, 7, 2 ], 
                [ 1, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with second line are equal third line' do
    session1 = [[ 6, 3, 4 ], 
                [ 5, 7, 2 ], 
                [ 5, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with first line are equal third line' do
    session1 = [[ 5, 3, 4 ], 
                [ 6, 7, 2 ], 
                [ 5, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with second line are equal third line' do
    session1 = [[ 3, 7, 4 ], 
                [ 6, 7, 2 ], 
                [ 5, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

  it 'is invalid with third line are equal third line' do
    session1 = [[ 3, 1, 2 ], 
                [ 6, 7, 2 ], 
                [ 5, 9, 8 ] ]

    expect(testeValidaSession(session1)).to eq false
  end

end