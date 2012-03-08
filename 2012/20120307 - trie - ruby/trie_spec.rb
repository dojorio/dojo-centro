require "trie"

describe Trie do
  let (:trie){ Trie.new }
  describe "Add" do
    it "deve inserir O na raiz da árvore" do
      trie.add(1, 'O')
      
      trie.dictionary.should == {'O'=>{:indices => [1]}}
    end

    it "deve inserir A na raiz da árvore" do
      trie.add(1, 'A')
      
      trie.dictionary.should == {'A'=>{:indices => [1]}}
    end
    
    it "deve inserir RATO na raiz da árvore" do
      trie.add(1, 'RATO')
      
      trie.dictionary.should == 
        {'R'=> 
          {'A' => 
            {'T' => 
              {'O' => {:indices => [1]}}}}}
    end
    
    it "deve inserir RATO e RATA na raiz da árvore" do
      trie.add(1, 'RATO')
      trie.add(2, 'RATA')
      
      trie.dictionary.should == 
        {'R'=> 
          {'A' => 
            {'T' => 
              {'O' => {:indices => [1]},
               'A' => {:indices => [2]}}}}}
    end
    
    it "deve inserir BOLA e BOLO e BOI na raiz da árvore" do
      trie.add(1, 'BOLA')
      trie.add(2, 'BOLO')
      trie.add(3, 'BOI')
      
      trie.dictionary.should == {
        'B'=> {
          'O' => {
            'L' => {
              'A' => {:indices => [1]},
              'O' => {:indices => [2]}}, 
            'I' => {:indices => [3]}}}}
    end

    it "deve inserir RATO na raiz da árvore" do
        trie.add(1, 'RATO')
        trie.add(2, 'RATO')
        
        trie.dictionary.should == 
          {'R'=> 
            {'A' => 
              {'T' => 
                {'O' => {:indices => [1, 2]}}}}}
    end
  end
  
  describe "find" do
    it "deve encontrar O" do
      trie.add(1, 'O')
      trie.find('O').should == [1]
    end
    
    it "deve encontrar O duas vezes" do
      trie.add(1, 'O')
      trie.add(2, 'O')
      
      trie.find('O').should == [1, 2]
    end
    
    it "deve não encontrar A" do
      trie.add(1, 'O')
      trie.find('A').should == []
    end
    
    it "deve encontrar RATO" do
      trie.add(1, 'RATO')
      trie.find('RATO').should == [1]
    end
    
    it "deve encontrar RATO e RATA" do
      trie.add(1, 'RATO')
      trie.add(2, 'RATA')
      trie.find('RATO').should == [1]
      trie.find('RATA').should == [2]
    end
    
    it "deve não encontrar prefixo RAT" do
      trie.add(1, 'RATO')
      trie.find('RAT').should == []
    end
  end
end

