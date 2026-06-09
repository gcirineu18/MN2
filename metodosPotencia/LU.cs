

public class LU
{
    public static double[] Solver(double[,] matrix,  double[] v)
    {
        var(Lmatrix, Umatrix) = Decomposition(matrix);
        var y = ForwardReduction(Lmatrix, v);
        var x = BackSubstitution(Umatrix, y);
        return x;
    }

    private static double[] ForwardReduction(double[,] Lmatrix, double[] b)
{
    int length = b.Length;
    double[] y = new double[length];

    for (int i = 0; i < length; i++)
    {
        double sum = 0.0;
        for (int j = 0; j < i; j++)
        {
            sum += Lmatrix[i, j] * y[j];
        }
        y[i] = (b[i] - sum) / Lmatrix[i, i];
    }

    return y;
}

private static double[] BackSubstitution(double[,] Umatrix, double[] y)
{
    int length = y.Length;
    double[] x = new double[length];

    for (int i = length - 1; i >= 0; i--)
    {
        double sum = 0.0;
        for (int j = i + 1; j < length; j++)
        {
            sum += Umatrix[i, j] * x[j];
        }
        x[i] = (y[i] - sum) / Umatrix[i, i];
    }

    return x;
}    public static (double[,], double[,]) Decomposition(double[,] matrix )
    {
        int length = matrix.GetLength(0);
        double[,] Lmatrix = new double[length, length];
        double[,] Umatrix = (double[,])matrix.Clone();

        int counter = 0;
        double multiplicador = 0.0;

        while (counter < length)
        {

            if (Math.Abs(Umatrix[counter,counter]) == 0.0)
            {
                throw new Exception("Pivô nulo.");
            }
            for(int k = counter + 1 ; k < length; k++)
            {
                for(int j = counter; j < length; j++)
                {                   
                    if(j == counter)
                    {
                        multiplicador = Umatrix[k,j] / Umatrix[counter, counter];
                        Lmatrix[k,j] = multiplicador;
                    } 
                    Umatrix[k,j] -= multiplicador * Umatrix[counter,j];
                }
            }
            counter++;
        }

        for(int k = 0; k < length; k++)
        {
            Lmatrix[k,k] = 1.0;
        }

        return (Lmatrix, Umatrix);
    }
}