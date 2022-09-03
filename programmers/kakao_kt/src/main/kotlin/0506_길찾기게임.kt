data class Node(
    val id: Int,
    val x: Int,
    val y: Int,
    var left: Node? = null,
    var right: Node? = null,
) {
    fun setChild(node: Node): Unit = when {
        x <= node.x -> {
            when (right) {
                null -> right = node
                else -> right!!.setChild(node)
            }
        }
        else -> {
            when (left) {
                null -> left = node
                else -> left!!.setChild(node)
            }
        }
    }
}

object Tree {

    private var root: Node? = null

    private var preorder = intArrayOf()

    private var postorder = intArrayOf()

    fun setNode(node: Node) = when(root) {
        null -> root = node
        else -> root!!.setChild(node)
    }

    fun getPreorder(): IntArray {
        preorder = intArrayOf()
        root?.let { preorder(root!!) }
        return preorder
    }

    private fun preorder(cur: Node) {
        preorder += cur.id
        cur.left?.let { preorder(cur.left!!) }
        cur.right?.let { preorder(cur.right!!) }
    }

    fun getPostorder(): IntArray {
        postorder = intArrayOf()
        root?.let { postorder(root!!) }
        return postorder
    }

    private fun postorder(cur: Node) {
        cur.left?.let { postorder(cur.left!!) }
        cur.right?.let { postorder(cur.right!!) }
        postorder += cur.id
    }
}

class Solution {

    fun solution(nodeinfo: Array<IntArray>): Array<IntArray> {
        nodeinfo.mapIndexed { index, node -> node + index }
            .sortedBy { -it[1] }
            .forEach { node -> Tree.setNode(Node(node[2] + 1, node[0], node[1])) }

        return arrayOf(Tree.getPreorder(), Tree.getPostorder())
    }
}