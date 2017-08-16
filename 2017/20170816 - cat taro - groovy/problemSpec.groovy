import spock.lang.*
import ocr

// https://community.topcoder.com/stat?c=problem_statement&pm=13006

class ProblemSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        ocr.catTaro(input) == output

        where:
        input  |  output
        ''     |  'Impossible'
        'CAT'  |  'Possible'
    }
}
