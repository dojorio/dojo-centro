import spock.lang.*
import patternName

class PatternNameSpec extends spock.lang.Specification {
	def "uma letra só"() {
        expect:
        patternName.camel(snake) == camelCase

        where:
        snake | camelCase
        'a'   | 'A'
        'b'   | 'B'
    }
}
