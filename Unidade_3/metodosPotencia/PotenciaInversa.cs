

using System.Numerics;

public class PotenciaInversa: IPotencia{
    
    public static (double, double[], int) Execute(double[] vOld, double[,] matrix, double epsilon, double lambdaOld = 0.0, double palpite = 0.0){
        int length = matrix.GetLength(0);
        vOld = Utils.normalize(vOld);
        double[] vNew = new double[length];
        double lambdaNew;
        double erroRelativo = 1.0;

        int steps = 0;
        var(Lmatrix, Umatrix) = LU.Decomposition(matrix);
        while(erroRelativo > epsilon)
        {      
            ++steps;
            vNew = LU.Solver(Lmatrix, Umatrix, vOld);

            lambdaNew = Utils.dotProduct(vOld, vNew);

            erroRelativo = Math.Abs((lambdaNew - lambdaOld) / lambdaNew);
            vOld = Utils.normalize(vNew);
            lambdaOld = lambdaNew;
            
        }
        lambdaOld = 1.0 /lambdaOld;

        return(lambdaOld, vOld, steps);
    }

}