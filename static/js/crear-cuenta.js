document.getElementById("btn").addEventListener("click", myFunction);
document.getElementById("ayudabtn").addEventListener("click", myFunctionAyuda);
//document.getElementById("cancelbtn").addEventListener("click", myFunctionCancel);

function myFunction() {
    validform = form();
    if (validform){
        const jsConfetti = new JSConfetti();
        jsConfetti.addConfetti();
        setTimeout(() => {
            window.location = "/cuenta-creada";
          }, 2000); 
    }
}

function myFunctionAyuda(){
    alert("Si quieres ayuda, perdon pero no hay :(")
}

/*
function myFunctionCancel(){       
    window.location ="file"
}
*/

function containsNumbers(str) {             //checks if there are any numbers in a string
    numberYesOrNo = /\d/.test(str)
    return numberYesOrNo;
  }

let usuarios = [];

function form(){
  let nombre = document.getElementById('nom01').value;
  let usuario = document.getElementById('usu01').value;
  let contrasena = document.getElementById('con01').value;
  let email = document.getElementById('email01').value;
  let imagen = document.getElementById('arch01').value;
  let pais = document.getElementById("selLoc").options[document.getElementById("selLoc").value].text;
  let cond = document.getElementById('chk01');

  let isValid = true;  // Usamos esta variable para verificar si todo está válido.

  // Validación para el nombre.
  if (nombre === "") {
    alert("El campo nombre es obligatorio.");
    isValid = false;
  }
  if(containsNumbers(nombre)){
    alert("Es prohibido usar numeros en el nombre!");
    isValid = false;
  }  

  // Validación para el usuario.
  if (usuario === "") {
    alert("El campo usuario es obligatorio.");
    isValid = false;
  }
  usuario2 = usuarios.find(u => u.usuario === usuario);
  if (usuario2){
    alert("El usuario existe, tienes que elegir otro!");
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
  if (pais === "Seleccionar.." ) {
    alert("Debes seleccionar un país.");
    isValid = false;
  }

  //Validar si los condiiones son aceptados. 
  if (!cond.checked){
    alert("Tienes que aceptar los condiciones para crear una cuenta!")
    isValid = false;
  }
  

  if (isValid) {
    let nuevoUsuario = {
      nombre: nombre,
      usuario: usuario,
      contrasena: contrasena,  // De nuevo, recuerda no guardar contraseñas en texto claro.
      email: email,
      pais: pais
    };

    usuarios.push(nuevoUsuario);
    return true;
  }

}
