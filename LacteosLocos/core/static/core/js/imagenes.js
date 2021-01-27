jQuery(function() {

    // llamada al plugin
    jQuery('.gridder').gridderExpander({
        scroll: true,  // activar/desactivar auto-scroll
        scrollOffset: 30,  // distancia en píxeles de margen al hacer scroll
        scrollTo: "panel", // hacia donde se hace el auto-scroll
        animationSpeed: 400, // duración de la animación al hacer clic en elemento
        animationEasing: "easeInOutExpo", // tipo de animación
        showNav: true,  // activar/desactivar navegación
        nextText: "Next", // texto para pasar a la siguiente imagen
        prevText: "Previous", // texto para pasar a la imagen anterior
        closeText: "Close", // texto del botón para cerrar imagen expandida
        onStart: function(){
            //código que se ejecuta cuando Gridder se inicializa
        },
        onContent: function(){
            //código que se ejecuta cuando Gridder ha cargado el contenido
        },
        onClosed: function(){
            //código que se ejecuta al cerrar Gridder
        }
    });

});