exports.maryWins = maryWins


function maryWins(table) {
    return table == '...' || table == 'xx.' || table == 'x.x' || table == '.xx'
}