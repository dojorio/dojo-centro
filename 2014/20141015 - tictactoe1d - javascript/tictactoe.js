exports.maryWins = maryWins


function maryWins(table) {
    var qtt_x    = table.split('x').length - 1
    if (table.indexOf("xx") != -1 || table.indexOf("x.x") != -1)
        return true
    if (table.length == 3) {
        return qtt_x % 2 == 0
    }

    return  table == '....' ||
            table == 'x...' ||
            table == '...x' 
}