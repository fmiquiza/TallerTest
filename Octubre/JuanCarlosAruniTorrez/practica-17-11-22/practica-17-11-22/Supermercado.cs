using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace practica_17_11_22
{
    public class Supermercado
    {
        public string nombre;
        public List<Empleado> empleados { get; set; }
        public Supermercado(string nombre)
        {
            this.empleados = new List<Empleado>();
            this.nombre = nombre;   
        }
        public void AddEmpleado(Empleado emple)
        {
            this.empleados.Add(emple);
        }
        public void DeleteEmpleado(Empleado emple)
        {
            if (this.empleados.Contains(emple))
            {
                this.empleados.Remove(emple);
                Console.WriteLine("Eliminado");
            }
            else
            {
                Console.WriteLine("Empleado no encontrado");
            }
        }
        public void BuscarEmpleado(string emple)
        {
            empleados.ForEach(x =>
            {
                if (x.Nombre.Equals(emple))
                {
                    Console.WriteLine($"Nombre: {x.Nombre}\n{x.Apellido}\n{x.rol}\n{x.genero}");
                }
            });
        }
        public void hacerTrabajarEmpleados()
        {
            empleados.ForEach(x =>
            {
                x.Trabajar();
            });
        }
        public void MostrarTrabajadores()
        {
            empleados.ForEach(x =>
            {
                Console.WriteLine($"nombre: {x.Nombre}  {x.Apellido} Rol: {x.rol}");
            });
        }
    }
}
