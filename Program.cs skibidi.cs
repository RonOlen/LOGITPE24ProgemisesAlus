namespace IFsAndElses
{
    internal class Program
    {
        static void Main(string[] args)

            // if ja else rakendus tuleb yeha
            //kontrollib sinu vaunust
            //1. Kui oled alla 18. siis konsool annab vastuse, et olen alaealine
            

            //2 Kui oled 19 kuni 65 aastat vana siis
            // konsool vastab, et oled täisealine

            //3Kui oled üle 65.a vana siis oled pensionäär
        {
            Console.WriteLine("Vana sa oled");
                int age = int.Parse(Console.ReadLine());

            if (age < 18)
                Console.WriteLine("Oled alaealine");

            else if (age >= 18 && age <= 64)

                Console.WriteLine("Oled täiskasvanud");
            else if (age >= 65)

                Console.WriteLine("Oled pensionäär");
        }
    }
}
