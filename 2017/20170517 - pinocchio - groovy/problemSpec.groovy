import spock.lang.*
import ocr


class ProblemSpec extends Specification {
    @Unroll
    def "corrida de pinocchio"() {
        expect:
        ocr.problem(pinocchio1, pinocchio2, pista) == ganhador

        where:
        pinocchio1  |  pinocchio2  |  pista  |  ganhador
        [1, 0.1]    |  [1, 0.1]    |  5      |  "empate"
        [1, 0.2]    |  [1, 0.1]    |  5      |  "pinocchio1"
        [1, 0.1]    |  [1, 0.2]    |  5      |  "pinocchio2"
        [1, 0.1]    |  [1, 0.3]    |  5      |  "pinocchio2"
        [2, 0.1]    |  [1, 0.1]    |  5      |  "pinocchio2"
        [2, 2]      |  [1, 0.1]    |  2      |  "pinocchio1"
        [1, 0.1]    |  [2, 2]      |  2      |  "pinocchio2"
        [1, 0.1]    |  [2, 1.9]      |  2      |  "pinocchio2"
    }
}
