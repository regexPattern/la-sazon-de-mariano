function buscar() {
  var input = document.getElementById("search-input").value;
  var resultados = document.getElementById("resultados");
  resultados.innerHTML =
    "<h3>Resultados de la búsqueda:</h3><p>Resultado 1</p><p>Resultado 2</p><p>Resultado 3</p>";
}

const lista1 = document.querySelector(".cont-c");
const categorias = [
  {
    nom: "cat",
    img: "./static/img/argentina.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/japon.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/suecia.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/india.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/mexico.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/nicaragua.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/espana.jpeg",
  },
  { nom: "cat", img: "./static/img/francia.jpeg" },
  {
    nom: "cat",
    img: "./static/img/italia.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/ukas.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/usa.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/uzbe.jpeg",
  },
  {
    nom: "cat",
    img: "./static/img/china.jpeg",
  },
];

for (const cat of categorias) {
  const elementoimg = document.createElement("div");
  const imagenCat = document.createElement("img");
  imagenCat.src = cat.img;
  const elementoCat = document.createElement("a");

  elementoimg.classList.add("fotos");
  elementoimg.appendChild(imagenCat);
  elementoCat.classList.add("flex-box");
  elementoCat.appendChild(elementoimg);
  elementoCat.href = "https://es.wikipedia.org/wiki/Argentina";

  lista1.appendChild(elementoCat);
}

const lista = document.querySelector(".cont-r");

for (const receta of db.recetas) {
  const iRec = document.createElement("img");
  iRec.src = receta.img;
  const eRec = document.createElement("a");
  const nomRec = document.createElement("h1");
  nomRec.textContent = receta.nombre;
  const pRec = document.createElement("p");
  pRec.textContent =
    "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus rem blanditiis culpa fuga voluptatum error voluptates dolor, tempore voluptas dolorum doloremque id unde iure esse aliquam eius cupiditate dignissimos ut?";

  eRec.appendChild(iRec);
  iRec.classList.add("fotos2");
  eRec.appendChild(nomRec);
  eRec.classList.add("texto");
  eRec.appendChild(pRec);
  eRec.classList.add("flex-box2");
  eRec.href = `receta.html?codigo-receta=${receta.codigo}`;

  console.log(eRec);
  lista.appendChild(eRec);
}
