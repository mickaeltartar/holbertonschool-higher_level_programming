const Button = document.querySelector('#red_header');

Button.addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});