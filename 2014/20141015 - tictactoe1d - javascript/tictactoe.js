exports.maryWins = maryWins


function maryWins(table) {
    if (table == 'x...x')
        return false

    return table.indexOf("xx")  != -1 ||
           table.indexOf("x.x") != -1 ||
           table.indexOf('...') != -1
}