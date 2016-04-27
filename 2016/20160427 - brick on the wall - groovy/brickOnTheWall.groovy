def static completeWall(bricks) {
    def e = (bricks[0] - (bricks[1]+bricks[2]))/2
    def b = e + bricks[1] 
    def c  = e + bricks[2]

    return [bricks[0], b, c, bricks[1], e, bricks[2]]


}
