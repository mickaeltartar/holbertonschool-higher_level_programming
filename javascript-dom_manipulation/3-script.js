const header = document.querySelector('header');
const toggleHead = document.getElementById('toggle_header');

toggleHead.addEventListener('click', function () {
  header.classList.toggle('red');
  header.classList.toggle('green');
});