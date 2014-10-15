exports.maryWins = maryWins


function maryWins(table) {
    var qtt_dots = table.split('.').length -1
 
    return qtt_dots % 2 == 1
}