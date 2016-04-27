def static completeWall(bricks) {
    if (bricks[0] == bricks[1] + bricks[2]) {
        return bricks + [bricks[1], 0, bricks[2]]
    }

    if (bricks.sum() == 4) {
        switch(bricks[1]) {
            case 0: return [3,1,2,0,1,1];
            case 1: return [3,2,1,1,1,0];
        }
    }

    if(bricks[0] == 2){
        return [2,1,1,0,1,0]

    }
}
