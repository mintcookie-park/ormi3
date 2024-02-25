class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        if(num_list.length >= 11) {
            for(int plus : num_list) {
                answer += plus;
            }
        } else {
            answer = 1;
            for(int multi : num_list) {
                answer *= multi;
            }
        }
        
        return answer;
    }
}