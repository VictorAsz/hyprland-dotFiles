jQuery(document).ready(function () {
  // Cliques no Menu
  jQuery('.nav-link').on('click', function (e) {
    e.preventDefault();
    const page = jQuery(this).data('page');
    jQuery('#content').load(`/pages/${page}/${page}.html`);
  });

  // Clique na logo 
  jQuery('.navbar-brand').on('click', function (e) {
    e.preventDefault();
    jQuery('#content').load(`/pages/home/home.html`);
  });
  
  jQuery('#content').load(`/pages/home/home.html`);
});
