def static completeWall(bricks) {
    if (bricks.size() == 3) {
        def e = (bricks[0] - (bricks[1]+bricks[2]))/2
        def b = e + bricks[1] 
        def c = e + bricks[2]

        return [bricks[0], b, c, bricks[1], e, bricks[2]]
    } else if (bricks.size() == 6) {
        def result1 = completeWall(bricks[0..2])
        return result1
    }

}
