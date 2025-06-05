jQuery(document).ready(function () {
  jQuery('.nav-link').on('click', function (e) 
  {

    e.preventDefault();


    const page = jQuery(this).data('page');


    jQuery('#content').load(`/pages/${page}/${page}.html`);
  }
);
});

jQuery(document).ready(function () {
  jQuery('.nav-link').on('click', function (e) {
    e.preventDefault();
    const page = jQuery(this).data('page');
    jQuery('#content').load(`/pages/${page}/${page}.html`);
  });

  // Carrega a página de home automaticamente ao iniciar
  jQuery('#content').load(`/pages/home/home.html`);
});



jQuery(document).ready(function () {
  jQuery('.navbar-brand').on('click', function (e){
    
    e.preventDefault();

    $('#content').load(`/pages/home/home.html`);
  });
})

