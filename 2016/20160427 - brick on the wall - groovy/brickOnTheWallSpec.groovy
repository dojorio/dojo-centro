// https://www.urionlinejudge.com.br/judge/en/problems/view/1426
import spock.lang.*
import static brickOnTheWall.completeWall 

class brickOnTheWallSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        completeWall(filled) == result

        where:
        filled                 | result
        [4,1,1]                | [4,2,2,1,1,1]
        [3,2,1]                | [3,2,1,2,0,1]
        [1,1,0]                | [1,1,0,1,0,0]
        [1,0,1]                | [1,0,1,0,0,1]
        [3,1,2]                | [3,1,2,1,0,2]
        [3,0,3]                | [3,0,3,0,0,3]
        [3,3,0]                | [3,3,0,3,0,0]
        [3,1,0]                | [3,2,1,1,1,0]
        [3,0,1]                | [3,1,2,0,1,1]
        [2,0,0]                | [2,1,1,0,1,0]
        [16,4,4,1,1,1]         | [16,8,8,4,4,4,2,2,2,2,1,1,1,1,1]
        [255,54,67,10,18,13]   | [255,121,134,54,67,67,23,31,36,31,10,13,18,18,13]
    }
}
