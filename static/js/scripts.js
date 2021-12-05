

function whenDelivery()
{
    var objDate = new Date();
    var hours = objDate.getHours();
    if (hours >= 14 && hours <= 24)
    {
      document.getElementById('deliveryInfo').innerHTML = "Kup teraz, dostawa jutro";
    }
    else{
      document.getElementById('deliveryInfo').innerHTML = "Kup teraz, dostawa pojutrze";
    }

}


function updateSubTotal() {

  var myTab = document.getElementById('basketTable');
    var sum=0;
        for (i = 1; i < myTab.rows.length-1; i++) {
            var objCells = myTab.rows.item(i).cells;
            sum+=parseFloat(objCells[4].innerHTML)
        }
  document.getElementsById("sumOfProducts").innerHTML = sum.toFixed(2)+"zł";


}
