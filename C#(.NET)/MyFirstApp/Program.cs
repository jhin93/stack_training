namespace MyFirstApp;

using System;

class Program
{
    static void Main(string[] args)
    {
        List<Person> people = new List<Person>
        {
            new Person("John", 25, "designer"),
            new Person("Jane", 30, "capenter"),
            new Person("Bob", 35, "lawyer"),
            new Person("Dave", 35, "designer"),
            new Person("Cane", 35, "designer")
        };

        Console.WriteLine("=== everyone === ");
        foreach (var person in people)
        {
            person.Introduce();
        }

        Console.WriteLine("=== under age 30 ===");
        var youngPeople = people.Where(p => p.Age < 30);
        foreach (var person in youngPeople)
        {
            person.Introduce();
        }
        
        Console.WriteLine("=== someone who is designer and over 25 ===");
        var designers = people.Where(p => p.Job == "designer" && p.Age > 25).OrderBy(p => p.Name);
        foreach (var person in designers)
        {
            person.Introduce();
        }
    }
}
