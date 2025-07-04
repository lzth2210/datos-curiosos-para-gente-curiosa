const botonSol = document.querySelector('.bx-sun');
const botonLuna = document.querySelector('.bx-moon');
const cuerpo = document.querySelector('.claro');

botonSol.addEventListener('click', () =>{
    cuerpo.classList.add('oscuro');
});

botonLuna.addEventListener('click', () =>{
    cuerpo.classList.remove('oscuro');
});