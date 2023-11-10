const recetas = JSON.parse(window.localStorage.getItem("recetas")) || [];
for(const receta of recetas) {
  console.log(receta.nombre);
  console.log(receta.imagen);
  
  const alimento = document.createElement("div");
  alimento.classList.add("alimento");
  alimento.append("...");

  const alimentoImagen = document.createElement("div");
  alimentoImagen.classList.add("imagen-alimento");
  alimento.appendChild(alimentoImagen);

  const linkAlimento = document.createElement("a");
  linkAlimento.setAttribute("href","./receta.html");
  const imagen = document.createElement("img");
  imagen.setAttribute("src","./static/img/"+receta.imagen);
  linkAlimento.appendChild(imagen);
  alimentoImagen.appendChild(linkAlimento);
  
  const texto = document.createElement("div");
  texto.classList.add("texto");
  const titulo = document.createElement("h1");
  const link = document.createElement("a");
  link.setAttribute("href","./receta.html");
  link.append(receta.nombre);
  titulo.appendChild(link);
  texto.append(titulo);
  alimentoImagen.appendChild(texto);

  const listaAlimentos = document.getElementById("li2");
  listaAlimentos.appendChild(alimento);
}