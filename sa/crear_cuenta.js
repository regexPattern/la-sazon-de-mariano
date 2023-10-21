
document.getElementById("btn").addEventListener("click", myFunction);

function myFunction() {

    const jsConfetti = new JSConfetti();
    jsConfetti.addConfetti();

    setTimeout(() => {
        window.location = "file:///C:/Users/Samantha/Desktop/Programaci%C3%B3n%20Web/cuenta_creada.html";
      }, 2000);
}

function getValueForID(id){                 //gets the value that the user wrote of the specific id 
    el = document.getElementById(id).value;
    return el;
}

function containsNumbers(str) {             //checks if there are any numbers in a string
    numberYesOrNo = /\d/.test(str)
    return numberYesOrNo;
  }

function username(){
    //check if the username in usu01 already exsists 
    el0 = getValueForID("usu01");
    const usuario = usuarios.find(u => u.usuario === el0);

    if(usuario){
        alert("El usuario existe, tienes que elegir otro!")
    }
    else{
        nuevousuario = {
            usuario : el0
        };
        usuarios.push(nuevousuario);
    }
}

function name(){                           //validates the name input 
    el1 = getValueForID("nom01");
    numberYesOrNo = containsNumbers(el1);
    if(numberYesOrNo){                     //if the string doesnt have any numbers it will be saved and added to the list 
        const usuario = usuarios.find(u => u.usuario === el0);

        usuarios.push(el1);
    }
    else{                                  //if not there will be an alert and 
        alert("Tienes que escribir el nombre con solo letras!")
    }
}

function password(){
    //first check con1 if there is a number and a special sign - puede ser con regex
    //then check if both con01 and con02 are the same 
    el2 = getValueForID("con01");
    el3 = getValueForID("con02");
    numberYesOrNo = containsNumbers(el2);
2
    if(numberYesOrNo){
        if(el2=el3){
            text[i,2].push(el2);
        }
        else{
            alert("Tu repeticion de contrasena tiene que estar lo mismo!")
        }
    }
    else{
        alert("Tu contrasena necesita incluir un numero!")
    }
}

function username(){
    //check if the username in usu01 already exsists 
}

function email(){
    //check if the content in email01 tiene un @ - puede ser con regex
}

function condiciones(){
    //check if the box is checked 
}

function ayuda(){
    //do a listener that will pop up a text when button ayuda is pressed
}

function cancel(){
    //it will take you to the first site
}

function crearCuenta(){
    //add all to an array 
}


