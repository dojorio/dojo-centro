module('Intervalo')

test('de um número é o próprio número', function(){
        same(intervalo([372]), [[372]])
    }
)

test('de dois numeros isolados são dois intervalos diferentes', function(){
        same(intervalo([2, 37]), [[2], [37]])
    }
)

test('de dois números consecutivos é o primeiro e o segundo', function(){
        same(intervalo([1, 2]), [[1, 2]])
    }
)

test('de três números sendo os dois primeiros consecutivos', function(){
        same(intervalo([1, 2, 5]), [[1, 2], [5]])
    }
)

test('de três números sendo os dois últimos consecutivos', function(){
        same(intervalo([1, 4, 5]), [[1], [4, 5]])
    }
)

test('de três números sendo os dois últimos consecutivos e menores que o primeiro', function(){
        same(intervalo([7, 4, 5]), [[4, 5], [7]])
    }
)

test('de 3 números consecutivos conserva o primeiro e o último', function () {
	same(intervalo([1, 2, 3]), [[1, 3]]);
})

test('tres numeros consecutivos, e dois isolados', function () {
	same(intervalo([1, 2, 3, 9, 5]), [[1, 3], [5], [9]]);
})
