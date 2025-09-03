namespace MyFirstApp;

public class Person
{
    public string Name {get; set;}
    public int Age {get; set;}
	public string Job {get; set;}

    public Person(string name, int age, string job)
	{ 
        Name = name;
        Age = age;
        Job = job;
    }

    public void Introduce() 
	{
		Console.WriteLine($"name : {Name}, age : {Age}, job : {Job}");
	}

}