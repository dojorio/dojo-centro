import spock.lang.*
import cattaro

class CatTaroSpec extends spock.lang.Specification {
	def "cat"() {
        expect:
        cattaro.verifica(texto) == resultado

        where:
        texto | resultado
        'cat' | 'POSSIBLE'
        ''    | 'IMPOSSIBLE'
        'catq'| 'POSSIBLE'
        'catw'| 'POSSIBLE'
        'ccat'| 'IMPOSSIBLE'
        'catcat'| 'IMPOSSIBLE'
        'caat'| 'IMPOSSIBLE'
        'cyat'| 'POSSIBLE'


    }



}



