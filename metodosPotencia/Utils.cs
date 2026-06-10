
class Utils
{
    public static double dotProduct(double[] v0, double[] v1)
    {
        int length = v0.Length;
        if(length != v1.Length)
        {
            throw new ArgumentException(
                "Vectors should have the same size"
                ) ;
        }

        double sum = 0;
        for(int i = 0; i < length; i++)
        {
            sum += v0[i] * v1[i];
        }
        return sum;
    }

    public static double[] normalize(double[] v0)
    {
        int length = v0.Length;
        double[] normalized_v = new double[length];
        double l2Norm = 0.0;
        for(int i = 0; i < length; i++)
        {
            l2Norm += Math.Pow(v0[i],2);
        }
        l2Norm = Math.Sqrt(l2Norm);
        if(l2Norm == 0)
        {
            throw new ArgumentException(
                "Not possible to normalize null vector."
            );
        }
        for(int i = 0; i < length; i++)
        {
            normalized_v[i] = v0[i] / l2Norm;
        }

        return normalized_v;
    }

    public static void PrintMatrix(double[,] m)
    {
        int rows = m.GetLength(0), cols = m.GetLength(1);
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
                Console.Write($"{m[i, j],8:F2} ");
            Console.WriteLine();
        }
    }

    public static double[,] MatrixScalarProduct(double[,] m1, double scalar)
    {
        int rows = m1.GetLength(0), cols = m1.GetLength(1);
        double[,] result = new double[rows,cols];
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                result[i,j] = m1[i,j] * scalar;
            }              
        }
        return result;
    }

    public static double[,] MatrixSubtraction(double[,] m1, double[,] m2)
    
    {
        int rows = m1.GetLength(0), cols = m1.GetLength(1);
        double[,] result = new double[rows,cols];
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                result[i,j] = m1[i,j] - m2[i,j];
            }              
        }
        return result;
    }

    public static void PrintResults(double lambdaOld, double[] vOld, int steps)
    {
        Console.WriteLine($"Lambda Old: {lambdaOld}\nVector elements:");
        foreach(double value in vOld){
            Console.Write($"{value}, " );
        }
        Console.WriteLine($"\nNº de passos: {steps}");
    }

}