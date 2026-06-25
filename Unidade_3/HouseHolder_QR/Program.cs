

public class HouseHolder{
    
   public static (double[,], double[,]) CalculateHouseHoulder(
        double[,] matrix, int n
   )
    {
        var hMatrix = Utils.InitializeIdentityMatrix(n);
        var oldMatrix = matrix;
        int length = matrix.GetLength(0);
        double[,] newHmatrix, newMatrix = new double[length,length];

        for (int i = 0; i < n-2; i++)
        {
            newHmatrix = ConstructHouseHolder(oldMatrix, i);

            newMatrix = Utils.MultiplyMatrixesSameDimension(newHmatrix, oldMatrix);
            newMatrix = Utils.MultiplyMatrixesSameDimension(newMatrix, newHmatrix);

            oldMatrix = newMatrix;

            hMatrix = Utils.MultiplyMatrixesSameDimension(hMatrix, newHmatrix);
        }

        return (newMatrix, hMatrix);

    }

    private static double[,] ConstructHouseHolder(double[,] matrix, int i)
    {
        int length = matrix.GetLength(0);
        var identityMatrix = Utils.InitializeIdentityMatrix(length);   
        double[] w = new double[length], 
                wLine = new double[length], 
                e = new double[length];

        for(int j = i + 1; j< length; j++)
        {
            w[j] = matrix[j, i];
        }

        var comprimentoVector = Utils.VectorLength(w);
        wLine[i+1] = comprimentoVector;
        var N = Utils.VectorSubtraction(w, wLine);
        var n = Utils.SimplerNormalize(N, Utils.VectorLength(N));
        var normMatrix = Utils.VectorToTransposeMultiplication(n);
        normMatrix = Utils.MatrixScalarProduct(normMatrix, 2);
        var Hmatrix = Utils.MatrixSubtraction(identityMatrix , normMatrix);

        return Hmatrix;
    }

   

    static void Main(string[] args)
    {
        double[,] matrix1 = {{7.0, 8.0, 9.0},{4.0, 5.0, 1.0},{2.0, 2.0, 0.0}};  
        double[,] matrix2 = {{1.0, 3.0, 8.0},{4.0, 0.0, 2.0},{7.0, 1.0, 9.0}};  
        double epsilon = 0.0000000001;
        double[] vector = [2, 3, 1];

        var mult = Utils.MultiplyMatrixesSameDimension(matrix1, matrix2);

        var result = Utils.VectorToTransposeMultiplication(vector);


        // double[,] matrix3 = {{40.0, 8.0, 4.0, 2.0 , 1.0},
        //                      {8.0, 30.0, 12.0, 6.0, 2.0},
        //                      {4.0, 12.0, 20.0, 1.0, 2.0}, 
        //                      {2.0, 6.0, 1.0, 25.0, 4.0},
        //                      {1.0, 2.0, 2.0, 4.0, 5.0, }};  
        //double[,] matrix3 = {{2.0/3.0, 1.0/3.0, 1.0/3.0},{1.0/3.0, 4.0/3.0, 1.0/3.0},{1.0/3.0, 1.0/3.0, 2.0/3.0}}; 
        double[,] matrix3 =
        {
            {15,3,1,5,1,5,1,2,3,4},
            {3,14,5,1,5,6,2,3,4,5},
            {1,5,14,5,6,3,3,4,5,6},
            {5,1,5,20,3,1,4,5,6,7},
            {1,5,6,3,18,5,5,6,7,8},
            {5,6,3,1,5,24,6,7,8,9},
            {1,2,3,4,5,6,27,3,1,5},
            {2,3,4,5,6,7,3,26,1,5},
            {3,4,5,6,7,8,1,1,26,6},
            {4,5,6,7,8,9,5,5,6,32}
        };

        int n  = matrix3.GetLength(0);
        var(T, HH) = CalculateHouseHoulder(matrix3, n);
        Console.WriteLine("\n Matriz A:");
        Utils.PrintMatrix(matrix3);
        Console.WriteLine("\n Matriz Tridiagonal:");
        Utils.PrintMatrix(T);
        Console.WriteLine("\n Matriz HH:");
        Utils.PrintMatrix(HH);
       
       var(P, lambda) = QR.MetodoQR(T, n, epsilon);

       var autovetores = Utils.MultiplyMatrixesSameDimension(HH, P);

       Console.WriteLine($"Autovalores:");
       foreach( double lamb in lambda)
        {
            Console.WriteLine(lamb);
        }

       Console.WriteLine($"Autovetores:");
       Utils.PrintMatrix(autovetores);
    }
}