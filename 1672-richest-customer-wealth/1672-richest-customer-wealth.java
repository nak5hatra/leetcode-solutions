class Solution {
    public int maximumWealth(int[][] accounts) {
        
        int answer = Integer.MIN_VALUE;

        for(int i = 0; i < accounts.length; i++){
            int sum = 0;
            for (int j = 0; j < accounts[i].length; j++){

                sum += accounts[i][j];
            }
            if (answer < sum){
                answer = sum;
            }
        }
        return answer;
    }
}