package patterns;

public class pattern20 {
    public static void main(String[] args) {
        int n=4;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(i==1 || i==n)
                {
                    System.out.print("*"+" ");
                }
                else if(i!=1 && i!=n)
                {
                    if(j==1 || j==n)
                    {
                        System.out.print("*"+" ");
                    }
                    else
                    {
                        System.out.print("  ");
                    }
                }
            }
            System.out.println();
        }
    }
    }

