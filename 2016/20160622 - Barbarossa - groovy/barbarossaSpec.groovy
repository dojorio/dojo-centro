// https://www.urionlinejudge.com.br/judge/en/problems/view/1997
import spock.lang.*
import static barbarossa.armedSoldiers

class BarbarossaSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        armedSoldiers(s,a,n) == output

        where:
        s   | a   | n   | output
        0   | 0   | 0   | 0
        1   | 1   | 11  | 1
        1   | 0   | 11  | 0
        0   | 1   | 11  | 0
        1   | 1   | 9   | 0
        1   | 3   | 9   | 1
        1   | 4   | 9   | 1
        2   | 4   | 9   | 0
        2   | 5   | 9   | 1

    }
}
