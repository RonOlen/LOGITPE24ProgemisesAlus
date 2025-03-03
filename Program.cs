// See https://aka.ms/new-cons,ole-template for more information
Console.WriteLine("Hello World!");
//peab saama sisestada nime
//if ja else kontrollib, kas on nimi vi on tühi
//kui leiate kuskilt teksti värviliseks teha, siis kasutage
Console.WriteLine("Mis teie nimi on!");
string name = Console.ReadLine();

if (name != "")

    Console.WriteLine("Õige nimi: " + name);

else

    Console.WriteLine("Vale nimi");
Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("ERROR");
