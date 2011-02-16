module("Encontre o Telefone")

test("o texto A corresponde ao número 2", function(){
    same(telefone('A'), '2')
})

test("o texto 1 corresponde ao número 1", function(){
    same(telefone('1'), '1')
})

test("o texto 0 corresponde ao número 0", function(){
    same(telefone('0'), '0')
})
test("o texto D corresponde ao número 3", function(){
    same(telefone('D'), '3')
})

test("o texto B corresponde ao número 2", function(){
    same(telefone('B'), '2')
})

test("o texto C corresponde ao número 2", function(){
    same(telefone('C'), '2')
   
})

test("o texto E corresponde ao número 3", function(){
    same(telefone('E'), '3')
})

test("o texto AB corresponde ao número 22", function(){
    same(telefone('AB'), '22')
})

test("o texto AZ corresponde ao número 22", function(){
    same(telefone('AZ'), '29')
})

test("o texto DOJO corresponde ao número 3656", function(){
    same(telefone('DOJO'), '3656')
})
test("o texto DOJO-D corresponde ao número 3656-3", function(){
    same(telefone('DOJO-D'), '3656-3')
})


