import java.util.*

data class Position(
    val x: Int,
    val y: Int,
    val directionIndex: Int
)

class `0503_경주로건설` {

    private lateinit var board: Array<IntArray>

    private val dp by lazy { Array(board.size) { Array(board.size) { Array(4) { Int.MAX_VALUE } } } }

    private val directions = listOf( Pair(1, 0), Pair(-1, 0), Pair(0, 1), Pair(0, -1) )

    fun solution(board: Array<IntArray>): Int {
        this.board = board

        bfs()
        return dp.last().last().minOrNull()!!
    }

    private fun bfs() {
        (0..3).forEach { i -> dp[0][0][i] = 0 }

        val queue: Queue<Position> = LinkedList()
        queue.add(Position(0, 0, 0))

        while (queue.isNotEmpty()) {
            val pos = queue.poll()

            directions.forEachIndexed { index, direction ->
                val nx = pos.x + direction.first
                val ny = pos.y + direction.second
                val cost = dp[pos.x][pos.y][pos.directionIndex] + COST_DIRECT + if (isCorner(pos, index)) COST_CORNER else 0

                if (canGo(nx, ny) && cost < dp[nx][ny][index]) {
                    dp[nx][ny][index] = cost
                    queue.add(pos.copy( x = nx, y = ny, directionIndex = index ))
                }
            }
        }
    }

    private fun canGo(nx: Int, ny: Int) = 0 <= nx && nx < board.size && 0 <= ny && ny < board.size && board[nx][ny] == 0

    private fun isCorner(position: Position, index: Int) = with(position) {
        position.directionIndex != index && (x != 0 || y != 0)
    }

    companion object {

        const val COST_CORNER = 500

        const val COST_DIRECT = 100
    }
}