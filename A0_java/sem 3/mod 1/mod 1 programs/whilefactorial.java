import java.util.Scanner;
class whilefactorial 
{
public static void main(String[] args) 
{
    Scanner sc=new Scanner(System.in);
    System.out.println("enter the number for which u want the factorial");
    int n=sc.nextInt();
    int fact=1;
    while(n>0)
    {
        fact=fact*n;
        n--;
    }
    System.out.println(fact);
}  
}
