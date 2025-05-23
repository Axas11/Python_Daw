const input = document.getElementById("nombre");
const parrafoSaludo = document.getElementById("saludo")
const parrafoNavegador = document.getElementById("nombreNavegador")

let nombreNavegador = localStorage.getItem("nombre");

if (nombreNavegador === null) {
    nombreNavegador = "ninguno";
}

parrafoNavegador.textContent = `Nombre por defecto: ${nombreNavegador}`;


function mostrarNombre() {
    let nombre = input.value 
    parrafoSaludo.innerText = "hola, " + nombre;

    localStorage.setItem("nombre", nombre);
    nombreNavegador = localStorage.getItem("nombre");
    parrafoNavegador.textContent = `Nombre por defecto: ${nombreNavegador}`; 

}