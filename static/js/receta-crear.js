document.getElementById("ayudabtn").addEventListener("click", myFunctionAyuda);

function myFunctionAyuda() {
  alert("Si quieres ayuda, perdon pero no hay :(");
}

function containsNumbers(str) {
  numberYesOrNo = /\d/.test(str);
  return numberYesOrNo;
}

var arrayIngredientes = [];

function agregarIngrediente() {
  // Obtén los valores de los campos de ingrediente, cantidad y medida
  const nombre = document.getElementById("nombre-ingrediente").value;
  const cantidad = document.getElementById("cantidad-ingrediente").value;
  const selectElement = document.getElementById("medida-ingrediente");
  const selectedIndex = selectElement.selectedIndex;
  const selectedOption = selectElement.options[selectedIndex];

  const nombreMedida = selectedOption.text;

  // Verifica si todos los campos tienen valores antes de agregar a la lista
  if (nombre && cantidad && nombreMedida) {
    const listaIngredientes = document.getElementById("listaIngredientes");

    // Crea un nuevo elemento de lista para mostrar el ingrediente
    const nuevoElementoLista = document.createElement("li");
    nuevoElementoLista.textContent = `${nombre} - ${cantidad} ${nombreMedida}${ Number(cantidad) > 0 ? 's' : '' }`;

    // Añade el nuevo elemento a la lista
    listaIngredientes.appendChild(nuevoElementoLista);
    arrayIngredientes.push({
      ingrediente: nombre,
      cantidad: cantidad,
      id_medida: selectedOption.value,
      nombre_medida: selectedOption.text
    });

    // Limpia los campos de ingrediente, cantidad y medida
    document.getElementById("nombre-ingrediente").value = "";
    document.getElementById("cantidad-ingrediente").value = "";
    selectElement.value = 0;
  } else {
    alert("Por favor, completa todos los campos antes de agregar.");
  }
} 

const form = document.getElementById("formulario-receta");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const nombre = document.getElementById("nombre").value;
  let pasos = document.getElementById("pasos").value;
  let pais = document.getElementById("id_pais").selectedIndex;
  let condiciones = document.getElementById("condiciones");

  let isValid = true; // Usamos esta variable para verificar si todo está válido.

  // Validación para el nombre.
  if (nombre === "") {
    alert("El campo nombre es obligatorio.");
    isValid = false;
  }
  if (containsNumbers(nombre)) {
    alert("Esta prohibido usar numeros en el nombre!");
    isValid = false;
  }

  // Validación para la descripcion.
  if (pasos === "") {
    alert("El campo descripcion es obligatorio.");
    isValid = false;
  }

  // Validación para el país.
  if (pais === 0) {
    alert("Debes seleccionar un país.");
    isValid = false;
  }

  //Validar si los condiciones son aceptadas.
  if (!condiciones.checked) {
    alert("Tienes que aceptar los condiciones para crear una receta!");
    isValid = false;
  }

  if (!isValid) {
    return;
  }

  const formData = new FormData(form);
  const categorias = [];

  for (const inputName of formData.keys()) {
    if (inputName.startsWith("categoria")) {
      categorias.push(formData.get(inputName));
    }
  }

  formData.append("ingredientes", JSON.stringify(arrayIngredientes));

  const request = new XMLHttpRequest(); 
  request.open("POST", "/receta/crear"); 
  request.send(formData); 
});
