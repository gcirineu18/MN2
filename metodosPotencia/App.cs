using System;
using System.Text;

class App{

    static (double, double[], int) ExecuteMethod(string method, double[] vOld, double[,] matrix, double epsilon, double lambdaOld, double palpite = 0.0){    
        
        if(method == "regular"){
            return PotenciaRegular.Execute(vOld, matrix, epsilon, lambdaOld);
        } else if(method == "inversa")
        {
            return PotenciaInversa.Execute(vOld, matrix, epsilon, lambdaOld);  
        } else if( method == "deslocamento")
        {
            return PotenciaDeslocamento.Execute(vOld, matrix, epsilon, lambdaOld, palpite);
        } else {
           Console.WriteLine("No existent method with that name.");
            Environment.Exit(1);
        }
        return (0.0, [], 0);
    }
    static void Main(string[] args){

        double[,] matrix = {{2.0/3.0, 1.0/3.0, 1.0/3.0},{1.0/3.0, 4.0/3.0, 1.0/3.0},{1.0/3.0, 1.0/3.0, 2.0/3.0}};  
        //double[,] matrix = {{1.0, 1.0, 1.0},{4.0, 3.0, -1.0},{3.0, 5.0, 3.0}};          
        double epsilon = 0.0000000001;
        double[] vOld = {1,1,1};
        double lambdaOld = 0.0; 
        int steps;
        double palpite = 0.0;

        if (args.Length > 1 && !string.IsNullOrWhiteSpace(args[1])){
            try {
                palpite = double.Parse(args[1]);
            }
            catch(Exception e){
                throw new ArgumentException("Argumento inválido.", e);
            }
        }

        (lambdaOld, vOld, steps) = ExecuteMethod(args[0], vOld, matrix, epsilon, lambdaOld, palpite);
        Utils.PrintResults(lambdaOld, vOld, steps);

    }
}