
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

     public static double[,] InitializeIdentityMatrix(int length)
    {
        double[,] identityMatrix = new double[length,length];
        for(int i = 0; i < length; i++)
        {
            identityMatrix[i,i] = 1;
        }
        return identityMatrix;
    }

    public static double[,] VectorToTransposeMultiplication(double[] v)
    {
        int length = v.Length;
        double[,] result = new double[length, length];
         for (int i = 0; i < length; i++)
        {
            for(int j = 0; j < length; j++)
            {
                result[i,j] = v[i] * v[j];
            }
        } 
        return result;
    }    
    public static double[,] MatrixTranspose(double[,] matrix)
    {
        int length = matrix.GetLength(0);
        double[,] transposeMatrix = new double[length,length] ;
        for (int i = 0; i < length; i++)
        {
            for(int j = 0; j < length; j++)
            {
                transposeMatrix[j,i] = matrix[i,j];
            }
        } 
        return transposeMatrix;
    }

    public static double[,] MultiplyMatrixesSameDimension(double[,] m1, double[,] m2)
    {
        int k;
        int length = m1.GetLength(0);
        double[,] result_matrix = new double[length,length];
        for(int i = 0; i < length; i++)
        {
             for(int j = 0; j < length; j++)
            {
                k = 0;
                while(k < length)
                {
                result_matrix[i,j] += m1[i,k] * m2[k,j];  
                 k++;
                }
         
            }
        }
        return result_matrix;
    }


    public static double VectorLength(double[] v)
    {
        double value = 0;
        int length = v.GetLength(0);
        
        for(int i = 0; i < length; i++)
        {
            value += Math.Pow(v[i], 2);
        }

        return Math.Sqrt(value);
    }

    public static double[] VectorSubtraction(double[] v1, double[] v2)
    {       
        int length = v1.GetLength(0);
        double[] resultVector = new double[length];
        
        for(int i = 0; i < length; i++)
        {
            resultVector[i] = v1[i] - v2[i];
        }

        return resultVector;
    }

    public static double[] SimplerNormalize(double[] v0, double comprimento)
    {
        int length = v0.Length;
        double[] normalized_v = new double[length];

        if(comprimento == 0)
        {
            throw new ArgumentException(
                "Not possible to normalize null vector."
            );
        }
        for(int i = 0; i < length; i++)
        {
            normalized_v[i] = v0[i] / comprimento;
        }

        return normalized_v;
    }

}