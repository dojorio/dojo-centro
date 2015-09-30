import spock.lang.*
import ratinho

class RatinhoSpec extends spock.lang.Specification {
	def "retorna o pai da criança"() {
        expect:
        ratinho.testeDeDna(pai1, pai2, filho) == papai

        where:
        pai1        | pai2        | filho | papai
        ['ZE', 'A'] | ['JO', 'C'] | 'A'   | 'ZE'
        ['JO', 'A'] | ['ZE', 'T'] | 'A'	  | 'JO'
        ['ZE', 'G'] | ['JO', 'A'] | 'A'	  | 'JO'
    }
}