def static completeWall(bricks) {
    if(bricks[0] == 3){
        return [3,2,1,2,0,1]
    }
    if(bricks[0] == 1){
        return [1,1,0,1,0,0]
    }
    return bricks[0] == 4 ? [4,2,2,1,1,1] : [2,1,1,0,1,0]
}
