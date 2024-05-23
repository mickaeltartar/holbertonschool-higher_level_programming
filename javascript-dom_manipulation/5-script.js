const updateButtonOfHeader = document.getElementById('update_header');

updateButtonOfHeader.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});