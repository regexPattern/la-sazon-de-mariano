/**
 * @typedef Receta
 * @prop {string} nombre
 * @prop {Object} publicacion
 * @prop {Autor} publicacion.autor
 */

/**
 * @typedef Autor
 * @prop {string} nombre
 * @prop {Date} fecha
 */

/**
 * @typedef Calificacion
 * @prop {number} promedio;
 * @prop {number} cantidad;
 */

async function obtenerDatosReceta() {
  await new Promise((resolve) => setTimeout(resolve, 1000));

  // ... busco en la base de datos ...

  return {
    nombre: "Tacos al pastor",
    publicacion: {
      autor: { nombre: "Carlos Castillo" },
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
  };
}

/**
 * @param {Awaited<ReturnType<typeof obtenerDatosReceta>>} receta
 */
function actualizarPaginaReceta(receta) {
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

  const listaIngredientes = document.getElementById("lista-ingredientes");
  for (const ingrediente of receta.ingredientes) {
    const listItemIngrediente = document.createElement("li");
    listItemIngrediente.textContent = ingrediente;
    listaIngredientes.appendChild(listItemIngrediente);
  }

  const parrafosInstrucciones = document.getElementById("instrucciones-receta");
  for (const paso of receta.pasos) {
    const parrafoInstruccion = document.createElement("p");
    parrafoInstruccion.textContent = paso;
    parrafosInstrucciones.appendChild(parrafoInstruccion);
  }
}

