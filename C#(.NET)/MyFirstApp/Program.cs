using System;

namespace MyFirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What's your name?");
            string name = Console.ReadLine() ?? "";

            Console.WriteLine($"Hi, {name}!");
        }
    }
}