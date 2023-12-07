const form = document.getElementById("formulario-signup")

document.getElementById("ayuda-btn").addEventListener("click", () => {
    alert("Si quieres ayuda, perdon pero no hay :(")
})

document.getElementById("cancel-btn", () => {
  form.reset()
})

function containsNumbers(str) {
    numberYesOrNo = /\d/.test(str)
    return numberYesOrNo;
  }

form.addEventListener("submit", (event) => {
  event.preventDefault()

  const formData = new FormData(form);

  let nombre = formData.get('nombre');
  let usuario = formData.get('nombre_usuario');
  let contrasena = formData.get('contrasenia');
  let email = formData.get('email');
  let pais = formData.get("id_pais");
  let condiciones = formData.get('terminos');

  let isValid = true;  // Usamos esta variable para verificar si todo está válido.

  if (nombre === "") {
    alert("El campo nombre es obligatorio.");
    isValid = false;
  }
  if(containsNumbers(nombre)){
    alert("Esta prohibido usar numeros en el nombre!");
    isValid = false;
  }  

  // Validación para el usuario.
  if (usuario === "") {
    alert("El campo usuario es obligatorio.");
    isValid = false;
  }

  // Validación para la contraseña.
  if (contrasena === "" || contrasena.length < 6) {
    alert("La contraseña debe tener al menos 6 caracteres.");
    isValid = false;
  }

  // Validación para el email.
  if (email === "" || !email.includes('@')) {
    alert("Ingresa un email válido.");
    isValid = false;
  }

  // Validación para el país.
  if (pais === 0) {
    alert("Debes seleccionar un país.");
    isValid = false;
  }

  //Validar si los condiciones son aceptadas.
  if (!condiciones){
    alert("Tienes que aceptar los condiciones para crear una cuenta!")
    isValid = false;
  }

  if (isValid) {
    const request = new XMLHttpRequest(); 
    request.open("POST", "/signup"); 
    request.send(formData); 
  }
})
