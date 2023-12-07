const formularioEliminar = document.getElementById("formulario-eliminar")

if (formularioEliminar) {
  formularioEliminar.addEventListener("submit", (event) => {
    if (!confirm("¿Deseas eliminar este perfil? Este paso no puede deshacerse.")) {
      event.preventDefault()
    }
  })
}
