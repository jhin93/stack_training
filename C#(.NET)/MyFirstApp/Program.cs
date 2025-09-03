namespace MyFirstApp;

using System;

class Program
{
    static void Main(string[] args)
    {
        Person person = new Person("John", 32);
        person.DisplayInfo();

        person.Name = "Wick";
        person.Age = 40;
        person.DisplayInfo();

        person.Age = -10;
        person.DisplayInfo();
    }
}
