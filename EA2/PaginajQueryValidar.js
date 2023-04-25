$(function()
{
    $('.btnAceptar').click(function()
    {
        if(!$.trim($('.txtRut').val()))
        {
            alert("Debe especificar rut");
            $('.txtRut').focus();
        }
        else  if(!$.trim($('.txDv').val()))
        {
            alert("Debe especificar dv");
            $('.txDv').focus();
        }
        else  if(!$.trim($('.txtNombre').val()))
        {
            alert("Debe especificar nombre");
            $('.txtNombre').focus();
        }
        else  if(!$.trim($('.txtEmail').val()))
        {
            alert("Debe especificar email");
            $('.txtEmail').focus();
        }
    })
});