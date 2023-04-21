function sumar()
{
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt(n1) + parseInt(n2);
    //alert("La suma de los números es: " + total);
    document.getElementById("resultado").value = total;
}

// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero
// y que no esten vacios (NaN)).