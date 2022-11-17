using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Create
{
    public class Persona : IAplicacion
    {
        string Apellido { get; set; }
        string Nombre { get; set; } 
        public ICrear ProcesarCuenta { get; set; } = new Persona();
    }
    public enum Rol
    {
        Doctor,
        Enfermera,
    }
}
}
