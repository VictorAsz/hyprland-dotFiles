$(document).ready(function () {
  $('.nav-link').on('click', function (e) 
  {

    e.preventDefault();


    const page = $(this).data('page');

    console.log("passei por aqui")
    $('#content').load(`/pages/${page}/${page}.html`);
  }
);
});

jQuery(document).ready(function () {
  jQuery
})
