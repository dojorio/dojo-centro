exports.miojo = function(amp1, amp2) {
    if (amp1 == 3 || amp2 == 3) {
        return 3
    }

    if (amp1 == 1 || amp2 == 1) {
        return amp2 > amp1 ? amp2 : amp1
    }

    return 8
}