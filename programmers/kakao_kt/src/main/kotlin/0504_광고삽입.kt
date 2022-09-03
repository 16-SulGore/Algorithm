class Time(
    val hour: Int,
    val minute: Int,
    val second: Int,
) {

    override fun toString(): String {
        val newHour = if (hour < 10) "0${hour}" else hour
        val newMinute = if (minute < 10) "0${minute}" else minute
        val newSecond = if (second < 10) "0${second}" else second

        return "${newHour}:${newMinute}:${newSecond}"
    }

    override fun hashCode() = hour * 60 * 60 + minute * 60 + second

    override fun equals(other: Any?) = hashCode() == other.hashCode()
}

class Solution {

    private lateinit var playTime: Time

    private lateinit var advTime: Time

    private lateinit var logTimes: List<Pair<Time, Time>>

    private val pointer = IntArray(MAX_SEC)

    fun solution(play_time: String, adv_time: String, logs: Array<String>): String {
        playTime = play_time.toTime()
        advTime = adv_time.toTime()
        logTimes = logs.map { log -> log.toTimePair() }
            .onEach { pair -> setTwoPointer(pair) }

        return getMaxTime().toString()
    }

    private fun setTwoPointer(timePair: Pair<Time, Time>) {
        pointer[timePair.first.hashCode()] += 1
        pointer[timePair.second.hashCode()] -= 1
    }

    private fun getMaxTime(): Time {
        var time = 0L
        var maxTime = 0L
        var timeDp = 0L

        var head = 0
        var tail = 0

        var result = 0

        (0 until MAX_SEC).forEach { _ ->
            timeDp += pointer[tail++]

            if (tail - head > advTime.hashCode()) timeDp -= pointer[head++]

            time += timeDp

            if (maxTime < time) {
                result = head
                maxTime = time
            }
        }

        return result.toTime()
    }

    companion object {

        const val MAX_SEC = 100 * 60 * 60
    }
}

// parsing extension methods
fun String.toTime() = Time(
    hour = substring(0, 2).toInt(),
    minute = substring(3, 5).toInt(),
    second = substring(6, 8).toInt()
)

fun String.toTimePair() = Time(
    hour = substring(0, 2).toInt(),
    minute = substring(3, 5).toInt(),
    second = substring(6, 8).toInt()
) to Time(
    hour = substring(9, 11).toInt(),
    minute = substring(12, 14).toInt(),
    second = substring(15, 17).toInt()
)

fun Int.toTime(): Time {
    val hour: Int = this / 60 / 60
    val minute: Int = (this - hour * 60 * 60) / 60
    val second: Int = (this - hour * 60 * 60 - minute * 60)

    return Time(hour, minute, second)
}