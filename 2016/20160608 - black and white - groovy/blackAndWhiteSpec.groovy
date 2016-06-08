// https://www.urionlinejudge.com.br/judge/en/problems/view/1997
import spock.lang.*
import static blackAndWhite.numberOfMoves

class BlackAndWhiteSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        numberOfMoves(source,target) == output

        where:
        source | target | output
        'n'    | 'n'    | 0
        'n'    | 'b'    | 1
        'b'    | 'n'    | 1
    }
}
