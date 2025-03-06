using System.Collections;

namespace RandomNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            int number = new Random().Next(1, 7);

            Console.WriteLine(number);

            switch (number)
            {
                case 1:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                    case 2:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                    case 3:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                    case 4:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                    case 5:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                    case 6:
                    Console.WriteLine("Veeretaisd nr" + number);
                    break;

                  





                default:
                    Console.WriteLine("Error");
                    break;

                    //nüüd tuleb kasutada switchi, et näidata numbrit 1-st kuni 6-ni
            }


        }
    }
}
