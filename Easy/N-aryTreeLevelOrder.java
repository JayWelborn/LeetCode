/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) {
            return new ArrayList<List<Integer>>();
        }
        
        List<List<Integer>> levelOrder = new ArrayList<List<Integer>>();
        Queue<Node> currentLevelQueue = new LinkedList<Node>();
        Queue<Node> nextLevelQueue = new LinkedList<Node>();
        currentLevelQueue.add(root);
        int level = 0;
        
        while(currentLevelQueue.size() > 0) {
            if (levelOrder.size() == level) {
                levelOrder.add(level, new ArrayList<Integer>());
            }
            Node currentNode = currentLevelQueue.remove();
            levelOrder.get(level).add(currentNode.val);
            for (Node node : currentNode.children) {
                nextLevelQueue.add(node);
            }
            
            if (currentLevelQueue.size() == 0 && nextLevelQueue.size() > 0) {
                currentLevelQueue = nextLevelQueue;
                nextLevelQueue = new LinkedList<Node>();
                level++;
            }
        }
        
        return levelOrder;
    }
}
