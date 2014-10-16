exports.maryWins = maryWins


function maryWins(table) {
    var qtt_x    = table.split('x').length - 1
 
    if (table.length == 3) {
        return qtt_x % 2 == 0
    }

    return (table[0] == '.' || table[3] == '.') && qtt_x % 2 == 0
}