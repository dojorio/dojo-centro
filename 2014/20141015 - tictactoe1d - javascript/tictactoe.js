exports.maryWins = maryWins


function maryWins(table) {
    var qtt_x    = table.split('x').length - 1,
        qtt_dot  = table.split('.').length - 1
 
    return qtt_x % 2 == 0 && qtt_dot % 2 == 1
}