/* PANTALLA DE CARGA */

const pantallaCarga = document.getElementById("pantalla-carga");
const ellipsisCarga = document.getElementById("ellipsis-carga");

const ellipsisCargaInterval = setInterval(() => {
  const cantidadActualEllipsis =
    ellipsisCarga.textContent.match(/./g)?.length || 0;

  if (cantidadActualEllipsis === 3) {
    ellipsisCarga.textContent = "";
  } else {
    ellipsisCarga.textContent += ".";
  }
}, 500);

/* RENDER RECETA */

const contenedorReceta = document.getElementById("contenedor-receta");

(async () => {
  const receta = await obtenerDatosReceta();

  actualizarPagina(receta);

  pantallaCarga.remove();
  clearInterval(ellipsisCargaInterval);
  contenedorReceta.style.display = "block";
})();

async function obtenerDatosReceta() {
  const parametrosUrl = new URLSearchParams(window.location.search);
  const codigoReceta = Number(parametrosUrl.get("codigo-receta"));

  await new Promise((resolve) => setTimeout(resolve, 0));

  return db.recetas.find((receta) => receta.codigo === codigoReceta);
}

function actualizarPagina(receta) {
  /* RESUMEN */

  document.getElementById("nombre-receta").textContent = receta.nombre;
  document.getElementById("nombre-autor-receta").textContent =
    receta.autor;
  document.getElementById("imagen-receta").setAttribute("src", receta.img);

  /* INGREDIENTES */

  const listaIngredientes = document.getElementById("lista-ingredientes");
  for (const ingrediente of receta.ingredientes) {
    const listItemIngrediente = document.createElement("li");
    listItemIngrediente.textContent = ingrediente;
    listaIngredientes.appendChild(listItemIngrediente);
  }

  /* PASOS */

  const parrafosInstrucciones = document.getElementById("instrucciones-receta");
  for (const paso of receta.pasos) {
    const parrafoInstruccion = document.createElement("p");
    parrafoInstruccion.textContent = paso;
    parrafosInstrucciones.appendChild(parrafoInstruccion);
  }

  /* COMENTARIOS */

  const comentarios =
    JSON.parse(window.localStorage.getItem("comentarios")) || [];
  for (const comentario of comentarios) {
    insertarElementoComentario(comentario);
  }
}

/* COMENTARIOS */

const formularioComentario = document.querySelector("form");

formularioComentario.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(formularioComentario);
  const comentario = formData.get("contenido");

  if (comentario) {
    formularioComentario.reset();
    insertarElementoComentario(comentario);

    const comentarios =
      JSON.parse(window.localStorage.getItem("comentarios")) || [];
    comentarios.push(comentario);
    window.localStorage.setItem("comentarios", JSON.stringify(comentarios));
  }
});

const listaComentarios = document.getElementById("lista-comentarios");

function insertarElementoComentario(comentario) {
  const contenedorComentario = document.createElement("li");
  contenedorComentario.classList.add("contenedor-comentario");

  const contenidoComentario = document.createElement("p");
  contenidoComentario.textContent = comentario;

  contenedorComentario.appendChild(contenidoComentario);
  listaComentarios.appendChild(contenedorComentario);

  const elementosComentarios = listaComentarios.getElementsByTagName("li");
  const contenidosComentarios = [];

  for (const li of elementosComentarios) {
    contenidosComentarios.push(li.textContent);
  }
}

/* GUARDAR RECETA */

const svgGuardada = document.querySelector("#guardar-receta > svg");

function actualizarSvgGuardada() {
  if (window.localStorage.getItem("guardada") === "true") {
    svgGuardada.style.fill = "currentColor";
  } else {
    svgGuardada.style.fill = "transparent";
  }
}

actualizarSvgGuardada();

const botonGuardar = document.getElementById("guardar-receta");

botonGuardar.addEventListener("click", () => {
  window.localStorage.setItem(
    "guardada",
    window.localStorage.getItem("guardada") === "true" ? "false" : "true",
  );

  actualizarSvgGuardada();
});
