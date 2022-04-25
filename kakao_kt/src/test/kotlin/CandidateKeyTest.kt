import org.junit.Test

import org.junit.Assert.*

class CandidateKeyTest {

    private val solution = Solution()

    @Test
    fun `입출력 예제 1번`() {
        val input: Array<Array<String>> = arrayOf(
            arrayOf("100","ryan","music","2"),
            arrayOf("200","apeach","math","2"),
            arrayOf("300","tube","computer","3"),
            arrayOf("400","con","computer","4"),
            arrayOf("500","muzi","music","3"),
            arrayOf("600","apeach","music","2")
        )

        assertEquals(2, solution.solution(input))
    }
}