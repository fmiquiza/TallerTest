using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace practica_17_11_22
{
    public class Persona
    {
        protected string nombre { get; }
        protected string apellido { get; }
        protected int ci;
        public Genero genero;
        public Persona(string nombre, string apellido, int ci, Genero genero)
        {
            this.nombre = nombre;
            this.apellido = apellido;
            this.ci = ci;
            this.genero = genero;
        }
        public void Hablar()
        {
            Console.WriteLine($"{this.nombre} hablando...");
        }
        public void Caminar()
        {
            Console.WriteLine($"{this.nombre} caminando...");
        }
        public string Nombre{
            get { return this.nombre;}
        }
        public string Apellido
        {
            get { return this.apellido; }
        }
    }
   public enum Genero
    {
        Hombre,
        Mujer
    }
}
