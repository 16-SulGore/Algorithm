data class Build(
    val x: Int,
    val y: Int,
    val buildType: BuildType,
    val isCreate: Boolean
)

enum class BuildType(val value: Int) {
    TOWER(0),
    DIVER(1),
}

class Solution {

    private lateinit var board: Array<Array<Array<Boolean>>>

    fun solution(n: Int, build_frame: Array<IntArray>): Array<IntArray> {
        board = Array(n + 1) { Array(n + 1) { arrayOf(false, false) } }

        setBuild(build_frame)

        return getTotalBuilt()
    }

    private fun setBuild(buildFrame: Array<IntArray>) = buildFrame.forEach { element ->
        with (element.toBuild()) {
            when (isCreate) {
                true -> {
                    board[x][y][buildType.value] = canBuild(this)
                }

                false -> {
                    board[x][y][buildType.value] = false

                    if (!checkAllBuilt()) board[x][y][buildType.value] = true
                }
            }
        }
    }

    private fun canBuild(build: Build): Boolean = when (build.buildType) {
        BuildType.TOWER -> canBuildTower(build.x, build.y)
        BuildType.DIVER -> canBuildDiver(build.x, build.y)
    }

    private fun canBuildTower(x: Int, y: Int) = hasBaseTower(x, y) || hasLeftDiver(x, y) || hasBaseDiver(x, y)

    private fun hasBaseTower(x: Int, y: Int) = y == 0 || (y > 0 && board[x][y - 1][BuildType.TOWER.value])

    private fun hasLeftDiver(x: Int, y: Int) = x > 0 && board[x - 1][y][BuildType.DIVER.value]

    private fun hasBaseDiver(x: Int, y: Int) = board[x][y][BuildType.DIVER.value]

    private fun canBuildDiver(x: Int, y: Int) = hasBaseTower(x, y) || hasRightBaseTower(x, y) || (hasRightDiver(x, y) && hasLeftDiver(x, y))

    private fun hasRightBaseTower(x: Int, y: Int) = y > 0 && x + 1 < board.size && board[x + 1][y - 1][BuildType.TOWER.value]

    private fun hasRightDiver(x: Int, y: Int) = x + 1 < board.size && board[x + 1][y][BuildType.DIVER.value]

    private fun checkAllBuilt(): Boolean {
        var result = true

        boardForEach { x, y, builtType, built ->
            if (built) result = result && canBuild(intArrayOf(x, y, builtType, 1).toBuild())
        }

        return result
    }

    private fun getTotalBuilt(): Array<IntArray> {
        var answer = arrayOf<IntArray>()

        boardForEach { x, y, builtType, built ->
            if (built) answer += intArrayOf(x, y, builtType)
        }

        return answer
    }

    private fun boardForEach(block: (x: Int, y: Int, builtType: Int, built: Boolean) -> Unit) {
        board.forEachIndexed { x, line ->
            line.forEachIndexed { y, cell ->
                cell.forEachIndexed { builtType, built ->
                    block(x, y, builtType, built)
                }
            }
        }
    }
}

fun IntArray.toBuild() = Build(
    x = get(0),
    y = get(1),
    buildType = if (BuildType.DIVER.value == get(2)) BuildType.DIVER else BuildType.TOWER,
    isCreate = get(3) == 1
)