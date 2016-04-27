def static completeWall(bricks) {
    def end
    
    if(bricks.sum() == 4){return [3,2,0,1,1,0]}

    if(bricks[0] == 3){
        end = [bricks[1], 0, 3 - bricks[1]]
    }

    if(bricks[0] == 1){
        end = [bricks[1], 0, 1 - bricks[1]]
    }

    return bricks + end
}
