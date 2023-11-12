class Solution {
    public int findNumbers(int[] nums) {
        int temp = 0;
        for(int num : nums){
            int temp2 = getEvenNums(num);
            if (temp2 % 2 == 0){
                temp++;
            }
        }
        return temp;
        
    }
    int getEvenNums(int num){
        int temp = 0;
        while (num > 0){
            num = num / 10;
            temp++;
        }
        return temp;
    }
}