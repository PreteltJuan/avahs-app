window.addEventListener('resize', resize_menu_lateral);
window.addEventListener('resize', resize_menu_favoritos);

var estado_find = false
var estado_menu_lateral = false
var estado_menu_favoritos = false
var pageWidth = 0;
var menuLateral = document.getElementById("menu-lateral")
var menuFavoritos = document.getElementById("menu-favoritos")
var fav_btn = document.getElementById("favorite-btn")
var find = document.getElementById("find")

//lines que abren y cierran menu
var linea1 = document.getElementById("line-menu-icon")
var linea2 = document.getElementById("line-menu-icon-2")


function ocultarFind() {
    if (estado_find) {
        find.classList.remove("find-show");
        find.classList.add("find-hidden");
    } else {
        find.classList.remove("find-hidden");
        find.classList.add("find-show");
        if (estado_menu_lateral) {
            majenarMenuOpciones()
        }
    }
    estado_find = !estado_find
}



function manejarMenuOpciones() {
    if (estado_menu_lateral) {
        linea1.classList.remove("rotate");
        linea1.classList.add("a-rotate");

        linea2.classList.remove("rotate-2");
        linea2.classList.add("a-rotate-2");

    } else {
        if (estado_find) {
            ocultarFind();
        }
        linea1.classList.remove("a-rotate");
        linea1.classList.add("rotate");

        linea2.classList.remove("a-rotate-2");
        linea2.classList.add("rotate-2");

        menuLateral.style.left = "0";
    }
    estado_menu_lateral = !estado_menu_lateral
    resize_menu_lateral()
}


function manejarMenuFavoritos(){
    if (estado_find) {
        ocultarFind();
    }
    if(estado_menu_favoritos){
        fav_btn.classList.remove("material-symbols-rounded");
        fav_btn.classList.add("material-symbols-outlined");
    }else{
        fav_btn.classList.remove("material-symbols-outlined");
        fav_btn.classList.add("material-symbols-rounded");
    }
    estado_menu_favoritos = !estado_menu_favoritos
    resize_menu_favoritos()
}


function resize_menu_lateral() {
    pageWidth = document.documentElement.scrollWidth;
    if (!estado_menu_lateral) {
        if (pageWidth < 600) {
            menuLateral.style.left = "-41vw";
        } else if (pageWidth < 900) {
            menuLateral.style.left = "-51vw";
        } else {
            menuLateral.style.left = "-31vw";
        }
    } else {
        menuLateral.style.left = "0";
        if (pageWidth < 600) {
            menuLateral.style.width = "41vw";
        } else if (pageWidth < 900) {
            menuLateral.style.width = "51vw";
        } else {
            menuLateral.style.width = "31vw";
        }
    }
}

function resize_menu_favoritos() {
    pageWidth = document.documentElement.scrollWidth;
    if (!estado_menu_favoritos) {
        if (pageWidth < 600) {
            menuFavoritos.style.right = "-41vw";
        } else if (pageWidth < 900) {
            menuFavoritos.style.right = "-51vw";
        } else {
            menuFavoritos.style.right = "-31vw";
        }
    } else {
        menuFavoritos.style.right = "0";
        if (pageWidth < 600) {
            menuFavoritos.style.width = "31vw";
        } else if (pageWidth < 900) {
            menuFavoritos.style.width = "41vw";
        } else {
            menuFavoritos.style.width = "21vw";
        }
    }
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
