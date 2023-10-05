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

/**
 * @typedef {Object} Receta
 *
 * @property {string} Receta.nombre
 *
 * @property {Object} Receta.publicacion
 * @property {Object} Receta.publicacion.autor
 * @property {string} Receta.publicacion.autor.nombre
 * @property {string} Receta.publicacion.autor.perfil
 * @property {Date} Receta.publicacion.fecha
 *
 * @property {Object} Receta.calificaciones
 * @property {number} Receta.calificaciones.promedio
 * @property {number} Receta.calificaciones.cantidad
 *
 * @property {string} Receta.imagen
 * @property {string[]} Receta.ingredientes
 * @property {string[]} Receta.pasos
 * @property {string[]} Receta.comentarios
 */

/* carga de datos */

const contenedorReceta = document.getElementById("contenedor-receta");

(async () => {
  const receta = await obtenerDatosReceta();
  actualizarPagina(receta);

  pantallaCarga.remove();
  clearInterval(ellipsisCargaInterval);
  contenedorReceta.style.display = "block";
})();

/* handlers formulario comentarios */

const formularioComentario = document.querySelector("form");

formularioComentario.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(formularioComentario);
  const comentario = formData.get("contenido");

  if (comentario) {
    formularioComentario.reset();
    agregarElementoComentario(comentario);
  }
});

/* handlers boton guardar */

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

/**
 * @param {Receta} receta
 */
function actualizarPagina(receta) {
  /* resumen */

  document.getElementById("nombre-receta").textContent = receta.nombre;
  document.getElementById("nombre-autor-receta").textContent =
    receta.publicacion.autor.nombre;
  document.getElementById("fecha-registro-receta").textContent =
    receta.publicacion.fecha.toDateString();
  document.getElementById("cantidad-calificaciones").textContent =
    receta.calificaciones.cantidad + " calificaciones";
  document.getElementById("calificacion-numerica").textContent =
    receta.calificaciones.promedio;
  document.getElementById("imagen-receta").setAttribute("src", receta.imagen);

  /* ingredientes */

  const listaIngredientes = document.getElementById("lista-ingredientes");
  for (const ingrediente of receta.ingredientes) {
    const listItemIngrediente = document.createElement("li");
    listItemIngrediente.textContent = ingrediente;
    listaIngredientes.appendChild(listItemIngrediente);
  }

  /* pasos */

  const parrafosInstrucciones = document.getElementById("instrucciones-receta");
  for (const paso of receta.pasos) {
    const parrafoInstruccion = document.createElement("p");
    parrafoInstruccion.textContent = paso;
    parrafosInstrucciones.appendChild(parrafoInstruccion);
  }

  /* comentarios */

  for (const comentario of receta.comentarios) {
    agregarElementoComentario(comentario);
  }
}

// TODO: Eventualmente podemos tener una funcion que se encargue exclusivamente
// de traer los comentarios de la receta, para hacer si poder hacer refresh
// cuando agregamos uno.
//
const listaComentarios = document.getElementById("lista-comentarios");

/**
 * @param {string} comentario
 */
function agregarElementoComentario(comentario) {
  const contenedorComentario = document.createElement("div");
  contenedorComentario.classList.add("contenedor-comentario");

  const contenidoComentario = document.createElement("p");
  contenidoComentario.textContent = comentario;

  contenedorComentario.appendChild(contenidoComentario);
  listaComentarios.appendChild(contenedorComentario);
}

/**
 * @returns Receta
 */
async function obtenerDatosReceta() {
  const parametrosUrl = new URLSearchParams(window.location.search);
  const codigoReceta = Number(parametrosUrl.get("codigo-receta"));

  await new Promise((resolve) => setTimeout(resolve, 0));

  return {
    nombre: "Tacos al pastor",
    publicacion: {
      autor: {
        nombre: "Carlos Castillo",
        perfil: "./index.html",
      },
      fecha: new Date(Date.now()),
    },
    calificaciones: {
      promedio: 4.5,
      cantidad: 10,
    },
    imagen: "./static/img/tacos.jpeg",
    ingredientes: [
      "Carne de cerdo 1/2 k",
      "Cebolla 1/4 Unidad",
      "Cilantro",
      "Cebolla picada",
      "Chiles Guajillo 2 Unidades",
      "Chiles pasilla 2 Unidades",
      "Tomates 4 Unidades",
      "Ajo 1 Diente",
      "Piña",
      "Achiote 50 g",
    ],
    pasos: [
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet corporis harum asperiores ex earum eligendi cupiditate saepe ea debitis nemo ab dignissimos, aliquam id. Rem veniam provident sed blanditiis suscipit? Amet ipsa voluptates molestias rem laboriosam commodi accusamus sed sapiente, iste ab animi alias blanditiis ipsum corrupti aliquam labore perferendis ad nesciunt perspiciatis quaerat quis a. Similique ullam distinctio maxime. Expedita ad fugiat similique veniam maiores maxime cum, repellat nulla.",
      "Aut quos laudantium ex minima repellendus, ullam provident, officiis natus perspiciatis pariatur temporibus, blanditiis aliquid consequatur odit deleniti a esse. Incidunt vero distinctio placeat dicta, tempore laudantium numquam sit quia libero harum architecto error ullam quae? Nemo repudiandae eos adipisci minus, perferendis aspernatur ullam voluptas illo officia ut, ducimus nostrum. Ullam necessitatibus dignissimos, assumenda, possimus sed et similique tenetur unde sint esse ducimus voluptates, quae est odit dolorem laudantium atque. Iste ratione minima impedit provident, eius quidem pariatur soluta distinctio. Corporis debitis nam eveniet consequatur sequi culpa pariatur maiores, illum dolorem iusto laudantium, repudiandae tenetur.",
      "Error porro veniam sapiente magni. Asperiores ea deserunt commodi, sapiente ducimus vero sed placeat perspiciatis? Id ea reprehenderit dolores incidunt sint praesentium nesciunt enim unde, officiis totam earum omnis quibusdam, numquam qui atque, ad corrupti necessitatibus amet. Nobis non asperiores laboriosam sunt reiciendis. Officia, corrupti. Necessitatibus similique iure magni saepe voluptatem aliquam iusto illo ad minima eveniet obcaecati delectus assumenda nihil praesentium, consectetur nobis! Architecto ad voluptatibus sunt aperiam maiores eum sint id facilis in. Voluptatibus nam ad alias repudiandae voluptatem distinctio ea vero dolore sed dolor magnam, expedita ut ratione odit, eveniet illum eius officia laudantium nemo, illo aspernatur nisi iste incidunt? Blanditiis, nobis! Quos maiores asperiores beatae, placeat eius odit cumque commodi aliquid non odio perferendis assumenda doloremque praesentium repellat neque facere! Et ad quibusdam repellat sequi necessitatibus vitae vel aut tenetur? Esse? Nobis odit ratione nam recusandae ab ducimus repellat dolores! Molestiae quasi illum ad aliquid illo incidunt nulla magni.",
    ],
    comentarios: [
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
      "Aut quos laudantium ex minima repellendus, ullam provident, officiis natus perspiciatis pariatur temporibus, blanditiis aliquid consequatur odit deleniti a esse.",
      "Error porro veniam sapiente magni. Asperiores ea deserunt commodi, sapiente ducimus vero sed placeat perspiciatis? Id ea reprehenderit dolores incidunt sint praesentium nesciunt enim unde, officiis totam earum omnis quibusdam, numquam qui atque, ad corrupti necessitatibus amet.",
    ],
  };
}
