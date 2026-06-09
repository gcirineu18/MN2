using System;
using System.Text;

class App{

    static void ExecuteMethod(string method, double[] vOld, double[,] matrix, double epsilon, double lambdaOld){    
        
        if(method == "regular"){
            PotenciaRegular.Execute(vOld, matrix, epsilon, lambdaOld);
        } else if(method == "inversa")
        {
            PotenciaInversa.Execute(vOld, matrix, epsilon, lambdaOld);  
        } else {
           Console.WriteLine("No existent method with that name.");
            Environment.Exit(1);
        }
    }
    static void Main(string[] args){

        double[,] matrix = {{2.0/3.0, 1.0/3.0, 1.0/3.0},{1.0/3.0, 4.0/3.0, 1.0/3.0},{9.0/3.0, 1.0/3.0, 2.0/3.0}};  
        //double[,] matrix = {{1.0, 1.0, 1.0},{4.0, 3.0, -1.0},{3.0, 5.0, 3.0}};          
        double epsilon = 0.0000000001;
        double[] vOld = {1,1,1};
        double lambdaOld = 0.0; 

        ExecuteMethod(args[0], vOld, matrix, epsilon, lambdaOld);
    }
}