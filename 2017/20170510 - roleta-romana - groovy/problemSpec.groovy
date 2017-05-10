import spock.lang.*
import ocr

class ProblemSpec extends spock.lang.Specification {
    def "2pessoas"() {
        expect:
        orc.problem(input) == output

        where:
        input  |  output
        1 | 1
    }
}
