/*
 * @lc app=leetcode.cn id=8 lang=java
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution {
    public int myAtoi(final String str) {

        int index=0;
        int res=0;
        int symbol=1;

        if(str.length()==0) return 0;


        while(index<str.length()-1&&str.charAt(index)==' ' )
            index++;

        // System.out.println(index);
        char first_char = str.charAt(index);
        System.out.println(first_char>0);
        if( index==str.length()-1 && (first_char<'0'||first_char>'9')){
            System.out.println("only have -");
            return 0;
        }
        if (str.charAt(index) == '-'){
            symbol=-1;
            index+=1;
        }else if(str.charAt(index)=='+'){
            index+=1;

        }
        else if (str.charAt(index)<'0' || str.charAt(index)>'9'){
            System.out.println("not a number");
            return 0;
        }
        for(;index<str.length();index++){
            char curr_val = str.charAt(index);

            if(curr_val<'0'||curr_val>'9')break;

            if(res > Integer.MAX_VALUE/10)
                return Integer.MAX_VALUE;

            if(res<Integer.MIN_VALUE/10){
                return Integer.MIN_VALUE;
            }
            if(res== Integer.MAX_VALUE/10 && curr_val-'0'>7)
                return Integer.MAX_VALUE;
            if (res==Integer.MIN_VALUE/10 && curr_val-'0'>8)
                return Integer.MIN_VALUE;

            res =res*10+symbol*(curr_val-'0');

        }



        return res;

    }
}
// @lc code=end

