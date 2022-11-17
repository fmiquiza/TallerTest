using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Create
{
    public interface ICrear
    {
        PersonalTrabajo Crear(IAplicacion persona);
    }
}
