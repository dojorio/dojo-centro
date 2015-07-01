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

    def "duas letras"() {
        expect:
        patternName.camel(snake) == camelCase

        where:
        snake | camelCase
        'aa'  | 'Aa'
        'bb'  | 'Bb'
        'ba'  | 'Ba'
        'ab'  | 'Ab'
    }

    def "três letras"() {
        expect:
        patternName.camel(snake) == camelCase

        where:
        snake | camelCase
        'aaa'  | 'Aaa'
    }

    def "duas palavras"() {
        expect:
        patternName.camel(snake) == camelCase

        where:
        snake   | camelCase
        'a_a'   | 'AA'
        'b_b'   | 'BB'
        'ab_a'  | 'AbA'
        'ab_ab' | 'AbAb'
    }

}



