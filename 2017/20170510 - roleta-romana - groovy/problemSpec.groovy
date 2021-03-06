import spock.lang.*
import ocr

class ProblemSpec extends spock.lang.Specification {

   	@Unroll
    def "para #pessoas pessoas e passo #salto o sobrevivente eh #saida"() {
        expect:
        ocr.roleta(pessoas, salto, inicio) == saida

        where:
        pessoas | salto | inicio | saida
        1       | 1     | 1      | 1
        2       | 1     | 1      | 1
        3       | 1     | 1      | 3
        4       | 1     | 1      | 1
        5       | 1     | 1      | 3
        6       | 1     | 1      | 5
        7       | 1     | 1      | 7
        8       | 1     | 1      | 1
        9       | 1     | 1      | 3
        16      | 1     | 1      | 1

		1       | 2     | 1      | 1 
        2       | 2     | 1      | 2
        3       | 2     | 1      | 2
        4       | 2     | 1      | 1
        5       | 2     | 1      | 4

        3       | 2     | 2      | 3
    }
}
