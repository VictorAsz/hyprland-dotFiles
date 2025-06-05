$(document).ready(function () {
  $('.page-link').on('click', function (e) {
    e.preventDefault();
    const page = $(this).data('page');
    $('#content').load(`${page}/${page}.html`);
  });
});
