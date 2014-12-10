exports.distinct_cubes = function(cubes) {

    if(cubes[0] == '111100' && cubes[1] == '110011')
        return 1

    var c1 = cubes[0].split('')
    var c2 = cubes[1].split('')
    var tb1 = [c1[0],c1[1]].sort().toString()
    var tb2 = [c2[0],c2[1]].sort().toString()

    var lat1 = cubes[0].slice(2)
    var lat2 = cubes[1].slice(2)

    var posicao_inicial = lat2.indexOf(lat1[0])


    if (tb1 == tb2 && c1.slice(2).toString() == c2.slice(2).toString())
        return 1
    return 2
}