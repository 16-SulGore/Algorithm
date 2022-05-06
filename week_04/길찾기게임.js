class Node {
    constructor(value, x) {
        this.value = value;
        this.x = x;
        this.left = null;
        this.right = null;
    }
}

class Tree {
    constructor() {
        this.root = null;
    }

    insert = (node) => {
        if (!this.root) {
            this.root = node;
            return;
        }

        let currentNode = this.root;
        while (true) {
            if (node.x < currentNode.x) {
                if (!currentNode.left) {
                    currentNode.left = node;
                } else {
                    currentNode = currentNode.left;
                    continue;
                }
            }
            if (node.x > currentNode.x) {
                if (!currentNode.right) {
                    currentNode.right = node;
                } else {
                    currentNode = currentNode.right;
                    continue;
                }
            }
            break;
        }
    };

    order = (answer, node) => {
        answer.preOrder.push(node.value);
        if (node.left) this.order(answer, node.left);
        if (node.right) this.order(answer, node.right);
        answer.postOrder.push(node.value);
    };
}

const compare = (a, b) => {
    if (a[2] == b[2]) {
        return a[1] - b[1];
    }
    return b[2] - a[2];
};

const solution = (nodeinfo) => {
    tree = new Tree();
    nodeinfo
        .map(([x, y], level) => [level + 1, x, y])
        .sort((a, b) => compare(a, b))
        .forEach(([level, x, _]) => {
            node = new Node(level, x);
            tree.insert(node);
        });

    answer = {
        preOrder: [],
        postOrder: [],
    };
    tree.order(answer, tree.root);
    return [answer.preOrder, answer.postOrder];
};
