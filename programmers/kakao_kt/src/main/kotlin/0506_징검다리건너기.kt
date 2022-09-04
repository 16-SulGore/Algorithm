class `0506_징검다리건너기`{

    private lateinit var stones: IntArray

    private var k = 0

    fun solution(stones: IntArray, k: Int): Int {
        this.stones = stones
        this.k = k

        var answer = 0

        var start = 0
        var end = stones.maxOrNull()!!

        while (start <= end) {
            val mid = (start + end) / 2

            when (canGoCount(mid)) {
                true -> {
                    start = mid + 1
                }
                false -> {
                    end = mid - 1
                    answer = mid
                }
            }
        }

        return answer
    }

    private fun canGoCount(peopleCount: Int): Boolean {
        var count = 0

        stones.forEach { stone ->
            if (count >= k) return false

            count = if (stone <= peopleCount) count + 1 else 0
        }

        return count < k
    }
}
