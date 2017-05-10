import spock.lang.*
import ocr

class ProblemSpec extends spock.lang.Specification {
   	@Unroll
    def "2 pessoas"() {
        expect:
        ocr.roleta(pessoas, salto, inicio) == saida

        where:
        pessoas | salto | inicio | saida
        1       | 1     | 1      | 1
        2       | 1     | 1      | 1
        3       | 1     | 1      | 3
        4       | 1     | 1      | 1
        


    }
}
