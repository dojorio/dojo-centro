import spock.lang.*
import miojo

class miojoSpec extends spock.lang.Specification {
    def "teste"() {
        expect:
        miojo.calcula(amp1, amp2) == result

    	where:
        amp1  | amp2  | result
        0     | 0     | null
        0     | 3     | 3
        3     | 0     | 3
        4     | 0     | null
        0     | 4     | null
        1     | 4     | 4
        4     | 1     | 4
        5     | 1     | 5

    }
}  