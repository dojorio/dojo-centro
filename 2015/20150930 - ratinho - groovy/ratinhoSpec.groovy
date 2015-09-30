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
        ['ZE', 'A'] | ['JO', 'A'] | 'A'	  | 'CADIM'
        ['ZE', 'C'] | ['JO', 'T'] | 'A'	  | 'CADIM'

        ['ZE', 'AA'] | ['JO', 'AC'] | 'AT' | 'CADIM'
        ['ZE', 'AA'] | ['JO', 'CA'] | 'AT' | 'CADIM'
        ['ZE', 'AT'] | ['JO', 'CT'] | 'AT' | 'ZE'

        ['ZE', 'CG'] | ['JO', 'AG'] | 'AT' | 'JO'
        ['ZE', 'AG'] | ['JO', 'CG'] | 'AT' | 'ZE'
        ['ZE', 'AG'] | ['JO', 'CG'] | 'TA' | 'ZE'
    }
}