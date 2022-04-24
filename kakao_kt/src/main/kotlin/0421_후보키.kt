class Solution {

    private val candidateKeys: MutableList<List<Int>> = mutableListOf()

    private lateinit var relation: Array<Array<String>>

    fun solution(relation: Array<Array<String>>): Int {
        this.relation = relation
        getKeys().forEach { key -> if (isUniqueness(key)) removeUnminimalityKey(key) }

        return candidateKeys.size
    }

    private fun getKeys() = Util.getCombinationList(relation[0].size)

    private fun isUniqueness(key: List<Int>) = relation.map { tuple -> key.map { index -> tuple[index] } }
        .let { keyList -> keyList.size == keyList.toSet().size }


    private fun removeUnminimalityKey(key: List<Int>) = candidateKeys.forEachIndexed { i, candidateKey ->
        when {
            candidateKey.containsAll(key) -> candidateKeys.removeAt(i)
            key.containsAll(candidateKey) -> Unit
            else -> candidateKeys.add(key)
        }
    }
}

object Util {

    fun getCombinationList(targetSize: Int): List<List<Int>> {
        val answer: MutableList<List<Int>> = mutableListOf()
        val elements = mutableListOf<Int>()
        val visited = Array(targetSize) { false }

        (0 until targetSize).forEach { i ->
            elements.add(i)
        }

        (0 until targetSize).forEach { i ->
            combination(answer, elements , visited, 0, i + 1)
        }

        return answer
    }

    // backtracking
    // reference: https://notepad96.tistory.com/entry/kot-5
    private fun combination(
        answer: MutableList<List<Int>>,
        elements: List<Int>,
        visited: Array<Boolean>,
        start: Int,
        target: Int) {
        if(target == 0) {
            answer.addAll( listOf(elements.filterIndexed { index, t -> visited[index] }) )
        } else {
            for(i in start until elements.size) {
                visited[i] = true
                combination(answer, elements, visited, i + 1, target - 1)
                visited[i] = false
            }
        }
    }
}