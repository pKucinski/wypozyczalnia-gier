function updateSubTotal()
{
  var myTab = document.getElementById('basketTable');
    var sum=0;
        for (i = 1; i < myTab.rows.length-1; i++) {
            var objCells = myTab.rows.item(i).cells;
            sum+=parseFloat(objCells[2].innerHTML);
        }
  document.getElementById("sumOfProducts").innerHTML = sum.toFixed(2)+"zł";
  document.getElementById("sumOfProducts2").innerHTML = sum.toFixed(2)+"zł";

}

function countVat()
{
  var myTab = document.getElementById('basketTable');
    var sum=0;
        for (i = 1; i < myTab.rows.length-1; i++) {
            var objCells = myTab.rows.item(i).cells;
            sum+=parseFloat(objCells[2].innerHTML);
        }
    document.getElementById("toPay").innerHTML = sum.toFixed(2)+"zł";
       sum=(sum-parseInt(sum)*0.77);
    document.getElementById("vat").innerHTML = sum.toFixed(2)+"zł";
}

function whenDelivery()
{
    var objDate = new Date();
    var hours = objDate.getHours();
    if (hours >= 14 && hours <= 24)
    {
      document.getElementById("deliveryInfo").innerHTML = "Kup teraz, dostawa jutro";
    }
    else{
      document.getElementById("deliveryInfo").innerHTML = "Kup teraz, dostawa pojutrze";
    }

}

var myModal = new bootstrap.Modal(document.getElementById("basicExampleModal"), {});
document.onreadystatechange = function () {
  myModal.show();
};
