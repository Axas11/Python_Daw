const parrafo = document.querySelector("#contador")

let numero = parseInt(parrafo.textContent);

parrafo.innerHTML



console.log(numero)

function disminuir(){
    numero--;
    parrafo.textContent = numero;

}

function aumentar(){
    numero++;
    parrafo.textContent = numero;

}