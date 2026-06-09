

using System.Numerics;

public class PotenciaInversa: IPotencia{
    
    public static void Execute(double[] vOld, double[,] matrix, double epsilon, double lambdaOld = 0.0){
        int length = matrix.GetLength(0);
        vOld = Utils.normalize(vOld);
        double[] vNew = new double[length];
        double lambdaNew;
        double erroRelativo = 1.0;

        int steps = 0;
        while(erroRelativo > epsilon)
        {      
            ++steps;
            vNew = LU.Solver(matrix, vOld);

            lambdaNew = Utils.dotProduct(vOld, vNew);

            erroRelativo = Math.Abs((lambdaNew - lambdaOld) / lambdaNew);
            vOld = Utils.normalize(vNew);
            lambdaOld = lambdaNew;
            
        }
        lambdaOld = 1.0 /lambdaOld;
        Console.WriteLine($"Lambda Old: {lambdaOld}\nVector elements:");
        foreach(double value in vOld){
            Console.Write($"{value}, " );
        }
        Console.WriteLine($"\nNº de passos: {steps}");
    }

}