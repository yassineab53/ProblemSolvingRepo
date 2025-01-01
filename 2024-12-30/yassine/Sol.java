import java.util.Scanner;

public class Sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        String str = "";
        int tmp = N;
        while(tmp != 0){
            if(tmp % 2 != 0){
                str = "1" + str;
            }else{
                str = "0" + str;
            }
            tmp /=2;
        }

        System.out.println(str);
        sc.close(); 
    }
}
