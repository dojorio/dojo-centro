exports.distinct_cubes = function(cubes) {

    var c1 = cubes[0].split('')
    var c2 = cubes[1].split('')
    var tb1 = [c1[0],c1[1]].sort().toString()
    var tb2 = [c2[0],c2[1]].sort().toString()

    if (tb1 == tb2) {
        if (c1.slice(2).toString() == c2.slice(2).toString())
            return 1
        else
            return 2
    } else {
        return 2
    }

}