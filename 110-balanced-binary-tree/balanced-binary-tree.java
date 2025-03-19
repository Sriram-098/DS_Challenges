/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public static boolean isBalanced(TreeNode root) {

        return f(root)!=-1;
    }
    public static int f(TreeNode root){
        if(root==null){
            return 0;
        }

        int  left=f(root.left);
        int  right=f(root.right);
        if(left==-1 || right==-1 ||Math.abs(left-right)>1){
            return -1;
        }

        
        return Math.max(right,left)+1;

    }
}