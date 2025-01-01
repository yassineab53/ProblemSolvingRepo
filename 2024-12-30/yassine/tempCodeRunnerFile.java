    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 1 ; i <= n; i++){
            String str = "";
            int tmp = i;
            while(tmp != 0){
                if(tmp%2 !=0){
                    str = "1" + str;
                }else{
                    str = "0" + str;
                }
                tmp = tmp / 2;
            }
            System.out.print(str + ", ");
        }
        scanner.close();
