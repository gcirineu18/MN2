
public class PotenciaRegular: IPotencia{
    
    public static void Execute(double[] vOld, double[,] matrix, double epsilon, double lambdaOld = 0.0){
        int length = matrix.GetLength(0);
        vOld = Utils.normalize(vOld);
        double[] vNew = new double[length];
        double lambdaNew;
        double erro = 1.0;

        int steps = 0;
        while(erro > epsilon)
        {      
            ++steps;
            for(int i = 0; i < length; i++)
            {
                double sum = 0;
                for(int j = 0; j < length; j++)
                {
                    sum +=  matrix[i,j] * vOld[j  ]; 
                }
                vNew[i] = sum;
            }
            lambdaNew = Utils.dotProduct(vOld, vNew);

            erro = Math.Abs(lambdaNew - lambdaOld) / lambdaNew;
            vOld = Utils.normalize(vNew);
            lambdaOld = lambdaNew;
            
        }
        Console.WriteLine($"Lambda Old: {lambdaOld}\nVector elements:");
        foreach(double value in vOld){
            Console.Write($"{value}, " );
        }
        Console.WriteLine($"\nNº de passos: {steps}");
    }
}