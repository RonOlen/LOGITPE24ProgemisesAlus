using System.Threading.Channels;

namespace RectangleCalculator
{
        internal class Program
        {
                static void Main(string[] args)
                {
                 Console.WriteLine("Ristküliku kalkulaator!");

                Console.WriteLine("Enter First Value");
                 string firstNumber = Console.ReadLine();
                float floatFirst = float.Parse(firstNumber);

    
                  Console.WriteLine("Enter Second Value");
                string secondNumber = Console.ReadLine();
                float floatSecond = float.Parse(secondNumber);

                 float floatPindala = floatFirst * floatSecond;
                 Console.WriteLine("Pindala on" + floatPindala);

                 float floatPindala = floatFirst * floatSecond;
                 Console.WriteLine("Pindala on" + floatPindala);

                 float ruutKülg = 4;
                 Console.WriteLine("Ruutu pindala on" + (ruutKülg * ruutKülg));
                 Console.WriteLine("Ruutu ümbermõõt on:" + (4 * ruutKülg));

                 float kolmPikkus = 5, kolmKõrgus = 3;
                 Console.WriteLine("Kolmnurka pindala on:" + (0.5 * kolmPikkus * kolmKõrgus));
                 Console.WriteLine("Kolmnurka ümbermõõt on" + (3 * kolmPikkus));

                 float raadius = 8;
                 Console.WriteLine("Ringi pindala on" + (Math.PI * raadius * raadius));
                 Console.WriteLine("Ringi ümbermõõt on" + (2 * Math.PI * raadius));


                }

        }

}


