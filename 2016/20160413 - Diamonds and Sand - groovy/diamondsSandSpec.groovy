//https://www.urionlinejudge.com.br/judge/en/problems/view/1069
import spock.lang.*
import static diamondsSand.pan

class diamondsSandSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        pan(mine) == result

        where:
        mine | result
        ''   | 0
    }
}