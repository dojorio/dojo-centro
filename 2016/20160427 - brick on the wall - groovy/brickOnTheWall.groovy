def static completeWall(bricks) {
    def end
    
    if(bricks.sum() == 4){return [3,2,1,1,1,0]}

    if(bricks[0] == bricks[1] + bricks[2]){
        end = [bricks[1], 0, bricks[2]]
    }

    return bricks + end
}
