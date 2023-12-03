/*document.getElementsByTagName("form")[0].addEventListener("submit", (event) => {
  event.preventDefault();
})*/
document.getElementById("btn").addEventListener("click", myFunction);
document.getElementById("ayudabtn").addEventListener("click", myFunctionAyuda);

function myFunction() {
  validform = form();
  if (validform) {
    const jsConfetti = new JSConfetti();
    jsConfetti.addConfetti();
    setTimeout(() => { }, 2000);
  }
}

function myFunctionAyuda() {
  alert("Si quieres ayuda, perdon pero no hay :(");
}

/*document.getElementsByTagName("form")[0].addEventListener("submit", (event) => {
  event.preventDefault();
})*/

/*
function containsNumbers(str) {
  numberYesOrNo = /\d/.test(str);
  return numberYesOrNo;
}

let recetas = [];

function form() {
  let nombre = document.getElementById("nom02").value;
  let descripcion = document.getElementById("descrip").value;
  let imagen = document.getElementById("arch02").value;
  let pais =
    document.getElementById("selLoc").options[
      document.getElementById("selLoc").value
    ].text;
  let cond = document.getElementById("chk00");

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
  if (descripcion === "") {
    alert("El campo descripcion es obligatorio.");
    isValid = false;
  }

  // Validación para el país.
  if (pais === "Seleccionar..") {
    alert("Debes seleccionar un país.");
    isValid = false;
  }

  //Validar si los condiciones son aceptadas.
  if (!cond.checked) {
    alert("Tienes que aceptar los condiciones para crear una receta!");
    isValid = false;
  }

  if (isValid) {
    let nuevaReceta = {
      nombre: nombre,
      descripcion: descripcion,
      pais: pais,
    };

    recetas.push(nuevaReceta);
    return true;
  }
}

let contadorIngredientes = 1; // Contador para identificadores únicos de ingredientes
*/
var arrayIngredientes = [];

function agregarIngrediente() {
  // Obtén los valores de los campos de ingrediente, cantidad y medida
  const ingrediente = document.getElementById(`ingrediente`).value;
  const cantidad = document.getElementById(`cantidad`).value;
  const selectElement = document.getElementById("selQuan");
  const selectedIndex = selectElement.selectedIndex;
  const selectedText = selectElement.options[selectedIndex].text;

  const medida = selectedText;

  // Verifica si todos los campos tienen valores antes de agregar a la lista
  if (ingrediente && cantidad && medida) {
    const listaIngredientes = document.getElementById("listaIngredientes");

    // Crea un nuevo elemento de lista para mostrar el ingrediente
    const nuevoElementoLista = document.createElement("li");
    nuevoElementoLista.textContent = `${ingrediente} ${cantidad} ${medida}`;

    // Añade el nuevo elemento a la lista
    listaIngredientes.appendChild(nuevoElementoLista);
    arrayIngredientes.push({
      ingrediente: ingrediente,
      cantidad: cantidad,
      medidad: selectedText,
    });

    // Incrementa el contador para el próximo ingrediente
    contadorIngredientes++;

    // Limpia los campos de ingrediente, cantidad y medida
    document.getElementById(`ingrediente`).value = "";
    document.getElementById(`cantidad`).value = "";
    document.getElementById("selQuan").value = 0;
  } else {
    alert("Por favor, completa todos los campos antes de agregar.");
  }
} 

const form = document.getElementsByTagName("form")[0];

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const categorias = [];

  for (const inputName of formData.keys()) {
    if (inputName.startsWith("categoria")) {
      categorias.push(formData.get(inputName));
    }
  }

  const infoReceta = {
    nombre: formData.get("nombreplato"),
    pasos: formData.get("recetadescrip"),
    imagen: formData.get("archivoplato").name,
    localidad: formData.get("localidad"),
    categorias: categorias,
    ingredientes: arrayIngredientes
  };

  console.log(infoReceta);

  const request = new XMLHttpRequest(); 
    request.open("POST", "/receta/crear"); 
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(infoReceta)); 

});
