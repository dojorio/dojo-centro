module("Anagrama - Letras repetidas")

test("Palavra vazia possui um anagrama sendo o proprio vazio", function(){
        same(anagrama(''), [''])
    }
)

test("Palavra de um caractere possui um anagrama sendo a propria palavra", function(){
        same(anagrama('a'), ['a'])
    }
)
    
test("Palavra com duas letras iguais sendo 'aa' deve retornar um anagrama sendo a propria palavra", function(){
        same(anagrama('aa'), ['aa'])
    }
)

test("Palavra com duas letras iguais deve retornar um anagrama diferente de 'aa'", function(){
        same(anagrama('cc'), ['cc'])
    }
)

test("Palavra com tres letras iguais sendo 'aaa' deve retornar um anagrama sendo a propria palavra", function(){
        same(anagrama('aaa'), ['aaa'])
    }
)

 
module("Anagrama - Letras diferentes")
    
test("Palavra com duas letras diferentes deve retornar dois anagramas", function(){
        same(anagrama('ab'), ['ab','ba'])
   }
)
test("Palavra 'abb' deve retornar 'abb', 'bba' e 'bab'", function(){
        same(anagrama('abb'), ['abb','bab', 'bba'])
   }
)

test("Palavra 'ana' deve retornar 'ana', 'aan' e 'naa'", function(){
        same(anagrama('ana'), ['aan','ana', 'naa'].sort())
   }
)
