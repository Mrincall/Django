function Mudarestado(minhaDiv) {
  var display = document.getElementById(minhaDiv).style.display;
  if (display == "none")
    document.getElementById(minhaDiv).style.display = 'block';
  else
    document.getElementById(minhaDiv).style.display = 'none';
}

function Botoes(b1) {
  document.getElementById('b2').click();
}