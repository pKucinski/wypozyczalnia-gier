
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