using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace practica_17_11_22
{
    public class Empleado : Persona
    {
        private int codigoCliente { get; }
        public Rol rol { get; set; }
        public Empleado(string nombre, string apellido, int ci, Genero genero, int codigo, Rol rol):base(nombre,apellido,ci,genero)
        {
            this.codigoCliente = codigo;
            this.rol = rol;
        }
        public void Trabajar()
        {
            Console.WriteLine($"{this.nombre} con el rol {this.rol} esta trabajando");
        }
    }
    public enum Rol
    {
        Cajero,
        Administrador,
        Reoposicionador,
        Limpieza
    }
}
