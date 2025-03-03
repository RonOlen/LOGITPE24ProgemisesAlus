// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
// vaja arvutada, mitu kahe eurost läheb ümber maa
// maa ümbermõõt tuleb vaja arvutada raadiuse abil
Console.WriteLine("Euro münti ruumala on 5cm")

 double coinDiameter =  25.75; // mm
double earthRadius = 6378000000; // mm
double aroundEarth = 2 * Math.PI * earthRadius

   
    Console.WriteLine("Maailmas Ümbermõõt:" + aroundEarth);
//nyyd alles muntide arv välja arvutada
double howManyCoins = aroundEarth / coinDiameter

Console.WriteLine("Maailmase mahub" + howManyCoins);