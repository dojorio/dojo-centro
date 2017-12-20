import spock.lang.*
import problem

class ProblemSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        problem.efeitoMagnetico(magnetos, cursor) == output

        where:
        magnetos | cursor  | output
        [[]]     | [0, 0]  | [0, 0]
    }
}
