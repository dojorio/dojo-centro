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
        1     | 4     | 3
        //4     | 1     | 3
        //5     | 1     | 3
        //1     | 2     | 3

    }
}  