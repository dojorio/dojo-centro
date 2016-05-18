import spock.lang.*
import brainfuck

class BrainfuckSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        brainfuck.execute(input, code) == output

        where:
        input  | code | output
        ''     | ''   | ''
        'a'    | ',.' | 'a'
        'ab'   | ',.' | 'a'
        'ba'   | ',.' | 'b'
        'a'    | ''   | ''
        'a'    | ',+.'| 'b'
        'a'    | '+'    | ''
        ''     | '+'*96 + '.' | 'a'
        'ab'   | ',,.' | 'b'


    }
}
