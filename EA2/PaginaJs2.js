function sumar()
{    
    document.getElementById("resultado").value = "";
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt("0" + n1) + parseInt("0" + n2);
    //alert("La suma de los números es: " + total);
    document.getElementById("resultado").value = total;
}

// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero
// y que no esten vacios (NaN) not a number).

function dividir()
{
    document.getElementById("resultado").value = "";
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    n1 = parseInt("0" + n1);
    n2 = parseInt("0" + n2);
    if(n2 == 0)
    {
        alert("No se puede dividir por cero");
        return;
    }

    var total = parseInt(n1) / parseInt(n2);
    document.getElementById("resultado").value = total;
}
function multiplicar()
{
    document.getElementById("resultado").value = "";
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt("0" + n1) * parseInt("0" + n2);
    //alert("La suma de los números es: " + total);
    document.getElementById("resultado").value = total;
}
function restar()
{
    document.getElementById("resultado").value = "";
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt("0" + n1) - parseInt("0" + n2);
    //alert("La suma de los números es: " + total);
    document.getElementById("resultado").value = total;
}

// agregar botón limpiar para dejar en blanco todos los input
// también asignar el foco al número 1
function limpiar()
{    
    document.getElementById("numero1").value = "";
    document.getElementById("numero2").value = "";
    document.getElementById("resultado").value = "";
    document.getElementById("numero1").focus();
}