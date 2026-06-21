
public interface IPotencia
{
    static abstract (double, double[], int) Execute(
        double[] vOld, 
        double[,] matrix, 
        double epsilon, 
        double lambdaOld = 0.0,
        double palpite = 0.0
    );
}