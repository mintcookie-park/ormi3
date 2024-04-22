import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
        public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {


            // Data 저장할 list 생성
            List<Data> dataList = new ArrayList<>();

            for( int i = 0 ; i < data.length; i++ ){
                // 생성자를 통해 data 배열에 있는 데이터 dataList 에 삽입
                // 조건에 따라서 저장되는 것들만 선별
                if("code".equals(ext) && data[i][0] < val_ext ){
                    dataList.add(new Data( data[i][0] , data[i][1]  , data[i][2]  , data[i][3] ));
                }
                if("date".equals(ext) && data[i][1] < val_ext){
                    dataList.add(new Data( data[i][0] , data[i][1]  , data[i][2]  , data[i][3] ));
                }
                if("maximum".equals(ext) && data[i][2] < val_ext){
                    dataList.add(new Data( data[i][0] , data[i][1]  , data[i][2]  , data[i][3] ));
                }
                if("remain".equals(ext) && data[i][3] < val_ext){
                    dataList.add(new Data( data[i][0] , data[i][1]  , data[i][2]  , data[i][3] ));
                }
            }
						// 오름차순 정렬 해야되는 요소에 따라서 다르게 오름차순 정렬
            if("code".equals(sort_by)){
                dataList = dataList.stream().sorted(Comparator.comparing(Data::getCode)).collect(Collectors.toList());
            }
            if("date".equals(sort_by)){
                dataList = dataList.stream().sorted(Comparator.comparing(Data::getDate)).collect(Collectors.toList());
            }
            if("maximum".equals(sort_by)){
                dataList = dataList.stream().sorted(Comparator.comparing(Data::getMaximum)).collect(Collectors.toList());
            }
            if("remain".equals(sort_by)){
                dataList = dataList.stream().sorted(Comparator.comparing(Data::getRemain)).collect(Collectors.toList());
            }

            int[][] answer = new int[dataList.size()][4];
						// 이중 배열로 다시 parsing 작업 
            for( int i = 0; i < dataList.size() ; i++ ){
                answer[i][0] = dataList.get(i).getCode();
                answer[i][1] = dataList.get(i).getDate();
                answer[i][2] = dataList.get(i).getMaximum();
                answer[i][3] = dataList.get(i).getRemain();
            }


            return answer;
        }


        class Data{
            int code;
            int date;
            int maximum;
            int remain;

            public Data( int code , int loc , int maximum , int remain ) {
                this.code = code;
                this.date = loc;
                this.maximum = maximum;
                this.remain = remain;
            }

            public int getCode() {
                return code;
            }

            public void setCode (int code) {
                this.code = code;
            }

            public int getDate() {
                return date;
            }

            public void setDate (int date) {
                this.date = date;
            }
            public int getMaximum() {
                return maximum;
            }

            public void setMaximum (int maximum) {
                this.maximum = maximum;
            }
            public int getRemain() {
                return remain;
            }

            public void setRemain (int remain) {
                this.remain = remain;
            }

        }

}