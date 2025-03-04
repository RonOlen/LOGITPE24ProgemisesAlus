using System;
using System.Collections.Specialized;
using System.ComponentModel.Design;

namespace IFsAndOddsnumber
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            // konsool kysib numbrit ja siis muudetakse
            // see int andmetüübiks

            //teha if ja else-ga kontroll
            // kus saame teada et kas nr on paris voi paaritu
            // kasuta operaatoreid

          

            Console.WriteLine("Sisesta number");
            int num = int.Parse(Console.ReadLine());

            if (num % 2 == 0)
            Console.WriteLine("Paaris");
            
            else

                Console.WriteLine("paaritu");




            



        }
    }
}
