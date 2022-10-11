const clave1 = document.querySelector("#clave1")
const clave2 = document.querySelector("#clave2")
const formulario = document.querySelector("#formulario")
const error = document.querySelector("#error")

formulario.addEventListener("submit",function(event){
    error.innerText = ""

    if(clave1.value !== clave2.value){
        event.preventDefault()
        error.innerText = "Las contraseñas no coinciden"
    }
})