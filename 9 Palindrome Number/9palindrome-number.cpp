class Solution {
public:
    bool isPalindrome(int x) {
        int arr[100];
        int rem=x;
        int count=0;
        if(x<0){
            return false;
        }
        while(rem>0){
            arr[count]=rem%10;
            rem=rem/10;
            count++;
        }
              for (int l = 0, r = count - 1; l < r; l++, r--) {
            if (arr[l] != arr[r]) {
                return false;
            }
        }
        
        return true;
    }
};