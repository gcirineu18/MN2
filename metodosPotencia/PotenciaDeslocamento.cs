

public class PotenciaDeslocamento: IPotencia{
    
    public static (double, double[], int) Execute(double[] vOld, double[,] matrix, double epsilon, double lambdaOld = 0.0, double palpite = 0.0){
        int length = matrix.GetLength(0);
        
        vOld = Utils.normalize(vOld);

        double[,] Imatrix = InitializeIdentityMatrix(length);

        double[] vNew;
        double lambdaNew;
        int steps;
        
        Imatrix = Utils.MatrixScalarProduct(Imatrix, palpite);
        double[,] newMatrix = Utils.MatrixSubtraction(matrix, Imatrix);
        
        (lambdaNew, vNew, steps) = PotenciaInversa.Execute(vOld, newMatrix, epsilon);
        lambdaNew = lambdaNew + palpite;
        
        return(lambdaNew, vNew, steps);
    }

    private static double[,] InitializeIdentityMatrix(int length)
    {
        double[,] identityMatrix = new double[length,length];
        for(int i = 0; i < length; i++)
        {
            identityMatrix[i,i] = 1;
        }

        return identityMatrix;
    }

}