def static completeWall(bricks) {
    if (bricks.size() == 3) {
        def e = (bricks[0] - (bricks[1]+bricks[2]))/2
        def b = e + bricks[1] 
        def c = e + bricks[2]

        return [bricks[0], b, c, bricks[1], e, bricks[2]]
    } else if (bricks.size() == 6) {
        def r1 = completeWall(bricks[0..2])
        def r2 = completeWall([bricks[1], bricks[3], bricks[4]])
        def r3 = completeWall([bricks[2], bricks[4], bricks[5]])

        return r1 + r2[1..2] + r3[1..2] + r2[3..5] + r3[4..5]
    }

}
