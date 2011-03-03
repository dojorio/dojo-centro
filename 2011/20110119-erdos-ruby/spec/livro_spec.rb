require 'spec_helper'

describe 'Silvometro' do

  it 'deveria retornar nil para autor isolado(Tomas)' do
    livro = Livro.new('tomas')
    silvometro = Silvometro.new
    silvometro.mede(livro).should be_eql nil
  end
  
  it 'deveria ter silva' do
    livro = Livro.new('silva')
    silvometro = Silvometro.new
    silvometro.mede(livro).should be_eql [0]
  end
  
  it 'deveria retornar 0 e 1 para Silva e Santos' do
    livro = Livro.new('silva','santos')
    silvometro = Silvometro.new
    silvometro.mede(livro).should be_eql [0,1]
  end
  
  it 'deveria retornar 0 e 1 para Silva e Renato' do
    livro = Livro.new('silva','renato')
    silvometro = Silvometro.new
    silvometro.mede(livro).should be_eql [0,1]
  end
=begin  
  it 'deveria retornar 0, 1 e 1 para silva, renato e santos' do
    livro = Livro.new('silva','renato','santos')
    silvometro = Silvometro.new
    silvometro.mede(livro).should be_eql [0,1,1]
  end
=end  
  it 'deveria retornar 0, 1 e 2 para silva e renato, e renato e hugo' do
    livro1 = Livro.new('silva','renato')
    livro2 = Livro.new('renato','hugo')
    silvometro = Silvometro.new
    silvometro.mede(livro1,livro2).should be_eql [0,1,2]
  end
  
  it 'deveria retornar 0, 1, 2 e 3 para silva e renato, renato e hugo, e hugo e claudio' do
    livro1 = Livro.new('silva','renato')
    livro2 = Livro.new('renato','hugo')
    livro3 = Livro.new('hugo','claudio')
    silvometro = Silvometro.new
    silvometro.mede(livro1,livro2,livro3).should be_eql [0,1,2,3]
  end
  
  it 'deveria retornar 0, 1, 2, 3 e nil para silva e renato, renato e hugo, e hugo e claudio e tomas sozinho' do
    livro1 = Livro.new('silva','renato')
    livro2 = Livro.new('renato','hugo')
    livro3 = Livro.new('hugo','claudio')
    livro4 = Livro.new('tomas')
    silvometro = Silvometro.new
    silvometro.mede(livro1,livro2,livro3).should be_eql [0,1,2,3,nil]
  end
  
=begin  
  it 'deveria retornar 0, 1, 2, 2 para silva e renato, e renato, hugo e claudio' do
    livro1 = Livro.new('silva','renato')
    livro2 = Livro.new('renato','hugo','claudio')
    silvometro = Silvometro.new
    silvometro.mede(livro1,livro2).should be_eql [0,1,2,2]
  end
=end
end
