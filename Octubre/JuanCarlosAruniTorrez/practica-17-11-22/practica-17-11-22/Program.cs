using System;

namespace practica_17_11_22
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Supermercado Carrefur = new Supermercado("Carrefur");
            Empleado emple1 = new Empleado("Miguel","Mamani",4325212,Genero.Hombre,123,Rol.Reoposicionador);
            Empleado emple2 = new Empleado("Maria", "Quispe", 532234, Genero.Mujer, 124, Rol.Administrador);
            Empleado emple3 = new Empleado("Facundo", "Miranda", 4325232, Genero.Hombre, 125, Rol.Limpieza);
            Empleado emple4 = new Empleado("Ana", "Gutierrez", 4323412, Genero.Mujer, 126, Rol.Cajero);
            Empleado emple5 = new Empleado("Juan", "Aruni", 5325212, Genero.Hombre, 127, Rol.Limpieza);

            Carrefur.AddEmpleado(emple1);
            Carrefur.AddEmpleado(emple2);
            Carrefur.AddEmpleado(emple3);
            Carrefur.AddEmpleado(emple4);
            Carrefur.AddEmpleado(emple5);

            Carrefur.hacerTrabajarEmpleados();
            Console.WriteLine("-----------------------------");
            Carrefur.MostrarTrabajadores();
            Console.WriteLine("-----------------------------");
            Carrefur.BuscarEmpleado("Maria");
            Console.WriteLine("-----------------------------");
            Carrefur.DeleteEmpleado(emple2);
            Console.WriteLine("-----------------------------");
            Carrefur.MostrarTrabajadores();
        }
    }
}
