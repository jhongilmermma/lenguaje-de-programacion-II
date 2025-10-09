class Love:
{
    public string Color { get; set; } = "#ffaa15";   // Color corregido
    public double LineWidth { get; set; } = 1.5;     // Grosor de línea
    public int Bottom { get; set; } = 0;             // Posición bottom
    public int Left { get; set; } = 7;               // Posición left
    public string FlexDirection { get; set; } = "column";

    public void Show()
    {
        Console.WriteLine($"Color: {Color}");
        Console.WriteLine($"Line width: {LineWidth}");
        Console.WriteLine($"Bottom: {Bottom}");
        Console.WriteLine($"Left: {Left}");
        Console.WriteLine($"Flex direction: {FlexDirection}");
    }
}

class Program
{
    static void Main()
    {
        Love love = new Love();
        love.Show();
    }
}
