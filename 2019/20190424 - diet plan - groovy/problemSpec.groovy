import spock.lang.*
import problem

class ProblemSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        problem.problem(input) == output

        where:
        input        | output
        ["", "", ""] | ""
        ["A", "", ""] | "A"
        ["B", "", ""] | "B"
        ["C", "", ""] | "C"
        ["CA", "", ""] | "AC"
        ["A", "A", ""] | ""
        ["B", "B", ""] | ""
        ["A", "", "A"] | ""
        ["B", "", "B"] | ""
        ["AB", "A", ""] | "B"
    }  
}
