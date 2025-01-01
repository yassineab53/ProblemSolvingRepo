//package 2024-12-31.yassine;

public class Solution {
    public static int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int [] res = new int[2*n];
        for(int i = 0; i < n; i++){
            res[i] = nums[i];
            res[i+n] = nums[i];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] t = {1,2,1};
        int[] r = Solution.getConcatenation(t);
        for(int i = 0 ; i < r.length ; i++){
            System.out.println(r[i]);
        }
    }
}
