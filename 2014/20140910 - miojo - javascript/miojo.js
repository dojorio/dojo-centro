exports.miojo = function(amp1, amp2) {
    if (amp1 == 3 || amp2 == 3) {
        return 3
    }

    if (amp1 == 1 || amp2 == 1) {
        return Math.max(amp1, amp2)
    }

    if (Math.abs(amp1 - amp2) == 3) {
        return Math.max(amp1, amp2)
    }

    return 8
}