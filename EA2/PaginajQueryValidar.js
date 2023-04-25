$(function()
{
    let numeros = '1234567890';
    let letras  = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM ';
    
    $('.txtRut').keypress(function(e)
    {
        // obtener el caracter presionado por el usuario
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })

    $('.txtDv').keypress(function(e)
    {
        let patron = numeros + 'kK';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    })

    $('.btnLimpiar').click(function()
    {
/*        $('.txtRut').val('');
        $('.txDv').val('');
        $('.txtNombre').val('');5
        $('.txtEmail').val('');
 */       
        
        $('.txtRut, .txtDv, .txtNombre, .txtEmail').val('');
        $('.txtRut').focus();
    });
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