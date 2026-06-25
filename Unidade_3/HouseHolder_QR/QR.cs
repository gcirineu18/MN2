

class QR
{
    private static double[,] MatrizJacobiBaseadaNoElemento_ij_DeRvelha(
        double[,] matrix,
        int i, 
        int j, 
        int n
    )
    {
        int length = matrix.GetLength(0);
        var Jmatrix = Utils.InitializeIdentityMatrix(length);
        double theta;
        double epsilon = 0.000001;

        if(Math.Abs(matrix[i,j]) <= epsilon) return Jmatrix;
        
        if(Math.Abs(matrix[j,j]) <= epsilon)
        {
            if(matrix[i,j] < 0)
            {
                theta = Math.PI / 2.0;
            }
            else
            {
                 theta = -(Math.PI / 2.0);
            }
        }
        else
        {
            theta = Math.Atan(-matrix[i,j]/matrix[j,j]);
        }

        Jmatrix[i,i] = Math.Cos(theta);
        Jmatrix[j,j] = Math.Cos(theta);
        Jmatrix[i,j] = Math.Sin(theta);
        Jmatrix[j,i] = -Math.Sin(theta);

        return Jmatrix;
    }


    private static (double[,], double[,]) CalculateQR(double[,] matrix, int n)
    {
        double[,] Jij, Rnova = new double[n,n];
        var QT = Utils.InitializeIdentityMatrix(n);
        var Rvelha = matrix;

        for(int j = 0; j < n - 1; j++)
        {
            for(int i = j + 1; i < n; i++)
            {
               Jij = MatrizJacobiBaseadaNoElemento_ij_DeRvelha(Rvelha, i, j, n);
               Rnova = Utils.MultiplyMatrixesSameDimension(Jij, Rvelha);
               Rvelha = Rnova;
               QT = Utils.MultiplyMatrixesSameDimension(Jij, QT);               
            }        
        }

        var Q = Utils.MatrixTranspose(QT);
        var R = Rnova;
        return(Q,R);
    }

    public static double SomaDosQuadradosDoTermosAbaixoDiagonal(double[,] newMatrix, int n)
    {
        double sum = 0.0;
        for(int i = 1; i < n; i++)
        {
            for(int j = 0; j < i; j++)
            {
                sum += Math.Pow(newMatrix[i,j], 2);
            }
        }
        return sum;
    }

    public static (double[,], double[]) MetodoQR(double[,] matrix, int n, double epsilon)
    {
        double[] lambda = new double[n];
        double val = 100;
        var P = Utils.InitializeIdentityMatrix(n);
        var oldMatrix = matrix;
        double[,] Q, R, newMatrix = new double[n,n]; 
        while(val > epsilon)
        {
          (Q,R) = CalculateQR(oldMatrix, n);
          newMatrix = Utils.MultiplyMatrixesSameDimension(R,Q);
          oldMatrix = newMatrix;
          P = Utils.MultiplyMatrixesSameDimension(P, Q);
          val = SomaDosQuadradosDoTermosAbaixoDiagonal(newMatrix, n);  
        }

        for(int i = 0; i < n; i++)
        {
            lambda[i] = newMatrix[i,i];
        }

        return (P, lambda);
    }
}