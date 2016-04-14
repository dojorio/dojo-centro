//https://www.urionlinejudge.com.br/judge/en/problems/view/1063
import spock.lang.*
import static railsAgain.sort 

class railsAgainSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        sort(trainIn, trainOut) == result

    	where:
        trainIn  | trainOut | result
        'a'      | 'a'      | 'IR'    
        'ab'     | 'ab'     | 'IRIR'
        'ab'     | 'ba'     | 'IIRR'
        'abc'    | 'abc'    | 'IRIRIR'
    }
}  