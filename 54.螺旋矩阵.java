import java.util.ArrayList;
import java.util.List;

import javax.sound.midi.Soundbank;

/*
 * @lc app=leetcode.cn id=54 lang=java
 *
 * [54] 螺旋矩阵
 */

// @lc code=start
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        String direction="R";
        int m=matrix.length;
        int n=matrix[0].length;
        int r_barrier=n-1;
        int d_barrier=m-1;
        int u_barrier=1;
        int l_barrier=0;
        int total_count=m*n;
        int curr_count=0;
        int x=0,y=0;
        if(y==r_barrier){
            direction="D";
        }
        List<Integer> res=new ArrayList<>(total_count);
        while(curr_count<total_count){
            System.out.println(String.format("x:%d,y:%d,direction:%s,count:%d,total:%d",x,y,direction,curr_count,total_count));
            res.add(matrix[x][y]);
            curr_count+=1;
            if(direction=="R"){
                    y+=1;
                if(y==r_barrier){
                    direction="D";
                    r_barrier=r_barrier-1;
                }
                
            }else if(direction=="D"){
                    x+=1;
                if(x==d_barrier){
                    direction="L";
                    d_barrier=d_barrier-1;
                }
            }else if (direction=="L"){
                y-=1;
                if(y==l_barrier){
                    direction="U";
                    l_barrier=l_barrier+1;
                }

            }else if(direction=="U"){
                x-=1;
                if(x==u_barrier){
                    direction="R";
                    u_barrier=u_barrier+1;
                }
            }

        }

        

        return res;
    }
public static void main(String[] args) {
    int input[][]={{3},{2}};
    Solution sln=new Solution();
    List<Integer> res= sln.spiralOrder(input);
    System.out.println(res);

    
}
}
// @lc code=end

