def static completeWall(bricks) {
    def end

    if(bricks[0] == 3){
        if(bricks[1]){
            return end = bricks[1] == 1 ? [1,0,2] : [2,0,1]   
        }

        return [3,0,3,0,0,3]

        
    }

    if(bricks[0] == 1){
        end = bricks[1] == 1 ? [1,0,0] : [0,0,1]   
    }

    return bricks + end
}
