import spock.lang.*
import problem

class ProblemSpec extends spock.lang.Specification {
    def "Account Book"() {
        expect:
        problem.lava_jato(total, values) == proof

        where:
        total | values | proof
        1     | [1]    | '+'
        -1    | [1]    | '-'
        1     | [2]    | '*'
        -1    | [2]    | '*'    
    }
}
