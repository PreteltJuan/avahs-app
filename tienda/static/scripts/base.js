

window.addEventListener('resize', resize_menu_lateral);

var estado_find = false
function ocultarFind() {

    if (estado_find) {
        document.getElementById("find").classList.remove("find-show");
        document.getElementById("find").classList.add("find-hidden");
    } else {
        document.getElementById("find").classList.remove("find-hidden");
        document.getElementById("find").classList.add("find-show");

        if (estado_menu_lateral) {
            mostrar()
        }
    }

    estado_find = !estado_find
}
var estado_menu_lateral = false
var pageWidth = 0;

function resize_menu_lateral() {
    pageWidth = document.documentElement.scrollWidth;
    if (!estado_menu_lateral) {
        if (pageWidth < 600) {
            document.getElementById("menu-lateral").style.left = "-41vw";
        } else if (pageWidth < 900) {
            document.getElementById("menu-lateral").style.left = "-51vw";
        } else {
            document.getElementById("menu-lateral").style.left = "-31vw";
        }
    } else {
        document.getElementById("menu-lateral").style.left = "0";
        if (pageWidth < 600) {
            document.getElementById("menu-lateral").style.width = "41vw";
        } else if (pageWidth < 900) {
            document.getElementById("menu-lateral").style.width = "51vw";
        } else {
            document.getElementById("menu-lateral").style.width = "31vw";
        }
    }
}
function mostrar() {
    pageWidth = document.documentElement.scrollWidth;
    if (estado_menu_lateral) {
        document.getElementById("line-menu-icon").classList.remove("rotate");
        document.getElementById("line-menu-icon").classList.add("a-rotate");

        document.getElementById("line-menu-icon-2").classList.remove("rotate-2");
        document.getElementById("line-menu-icon-2").classList.add("a-rotate-2");

    } else {
        if (estado_find) {
            ocultarFind();
        }
        document.getElementById("line-menu-icon").classList.remove("a-rotate");
        document.getElementById("line-menu-icon").classList.add("rotate");

        document.getElementById("line-menu-icon-2").classList.remove("a-rotate-2");
        document.getElementById("line-menu-icon-2").classList.add("rotate-2");

        document.getElementById("menu-lateral").style.left = "0";
    }
    estado_menu_lateral = !estado_menu_lateral
    resize_menu_lateral()
}

var top_header_seleccionado = 1

setInterval(actualizar_top_header, 6000);
const div1 = document.getElementById("top-header-content-1");
const div2 = document.getElementById("top-header-content-2");
const div3 = document.getElementById("top-header-content-3");

function actualizar_top_header() {
    switch (top_header_seleccionado) {
        case 1:
            div1.style.top = "-50px";
            div2.style.top = "1vh";
            top_header_seleccionado++;
            break;
        case 2:
            div2.style.top = "-50px";
            div3.style.top = "1vh";        
            top_header_seleccionado++;
            break;
        case 3:
            div3.style.top = "-50px";
            div1.style.top = "1vh";
            top_header_seleccionado=1;
            break;
    }

}