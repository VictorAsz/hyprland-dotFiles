jQuery(document).ready(function () {
  // Clique em links do menu
  jQuery('.nav-link').on('click', function (e) {
    e.preventDefault();
    const page = jQuery(this).data('page');
    jQuery('#content').load(`/pages/${page}/${page}.html`);
  });

  // Clique na logo (navbar-brand)
  jQuery('.navbar-brand').on('click', function (e) {
    e.preventDefault();
    jQuery('#content').load(`/pages/home/home.html`);
  });

  // Carregar a home automaticamente ao abrir o site
  jQuery('#content').load(`/pages/home/home.html`);
});
