document.querySelector('.sticks').addEventListener('click', (e) =>
{
  e.stopPropagation();
  e.preventDefault();
  //document.querySelector('.input').value = '';
  document.querySelector('.input-container').blur();
});