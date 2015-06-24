import spock.lang.*
import patternName

class PatternNameSpec extends spock.lang.Specification {
	def "uma letra só"() {
        expect:
        patternName.camel('a') == 'A'
    }
}
