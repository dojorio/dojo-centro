import spock.lang.*
import erdos

class ErdosSpec extends spock.lang.Specification {
	def "only Erdos"() {
        expect:
		erdos.numbers(["X": ["Erdos"]]) == ["Erdos": 0]
	}

	def "Erdos with Ze"() {
        expect:
		erdos.numbers([
			"X": ["Erdos", "Ze"]]) == ["Erdos": 0, "Ze": 1]
	}
		
	def "Erdos with many authors"(){
        expect:
		erdos.numbers([
			"X": ["Erdos", "Ze", "Maria"]]) == ["Erdos": 0, "Ze": 1, "Maria": 1]
	}

	def "Erdos with Maria"(){
        expect:
		erdos.numbers([
			"X": ["Erdos", "Maria"]]) == ["Erdos": 0, "Maria": 1]
	}

	def "Erdos with Ze e Jo"(){
        expect:
		erdos.numbers([
			"X": ["Erdos", "Ze", "Jo"]]) == ["Erdos": 0, "Ze": 1, "Jo": 1]
	}

	def "Erdos with Maria"(){
        expect:
		erdos.numbers([
			"X": ["Maria", "Erdos"]]) == ["Erdos": 0, "Maria": 1]
	}


}