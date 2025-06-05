$(document).ready(function () {
  $('.nav-link').on('click', function (e) 
  {

    e.preventDefault();


    const page = $(this).data('page');


    $('#content').load(`/pages/${page}/${page}.html`);
  }
);
});

jQuery(document).ready(function () {
  jQuery('.navbar-brand').on('click', function (e){
    
    e.preventDefault();

    $('#content').load(`/pages/home.html`);
  });
})
