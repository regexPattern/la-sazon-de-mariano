/*document.getElementsByTagName("form")[0].addEventListener("submit", (event) => {
	event.preventDefault();
})*/
document.getElementById("btn").addEventListener("click", myFunction);
document.getElementById("ayudabtn").addEventListener("click", myFunctionAyuda);

function myFunction() {
    validform = form();
    if (validform){
        const jsConfetti = new JSConfetti();
        jsConfetti.addConfetti();
        setTimeout(() => {}, 2000); 
    }
}

function myFunctionAyuda(){
    alert("Si quieres ayuda, perdon pero no hay :(")
}

/*document.getElementsByTagName("form")[0].addEventListener("submit", (event) => {
	event.preventDefault();
})*/
function containsNumbers(str) {
    numberYesOrNo = /\d/.test(str)
    return numberYesOrNo;
  }

let recetas = [];

function form(){
  let nombre = document.getElementById('nom02').value;
  let descripcion = document.getElementById('descrip').value;
  let imagen = document.getElementById('arch02').value;
  let pais = document.getElementById("selLoc").options[document.getElementById("selLoc").value].text;
  let cond = document.getElementById('chk00');

  let isValid = true;  // Usamos esta variable para verificar si todo está válido.

  // Validación para el nombre.
  if (nombre === "") {
    alert("El campo nombre es obligatorio.");
    isValid = false;
  }
  if(containsNumbers(nombre)){
    alert("Esta prohibido usar numeros en el nombre!");
    isValid = false;
  }  

  // Validación para la descripcion.
  if (descripcion === "") {
    alert("El campo descripcion es obligatorio.");
    isValid = false;
  }

  // Validación para el país.
  if (pais === "Seleccionar.." ) {
    alert("Debes seleccionar un país.");
    isValid = false;
  }

  //Validar si los condiciones son aceptadas. 
  if (!cond.checked){
    alert("Tienes que aceptar los condiciones para crear una receta!")
    isValid = false;
  }
  

  if (isValid) {
    let nuevaReceta = {
      nombre: nombre,
      descripcion: descripcion,
      pais: pais
    };

    recetas.push(nuevaReceta);
    return true;
  }
}
