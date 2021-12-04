updateSubTotal();

function updateSubTotal() {

  var myTab = document.getElementById('basketTable');
    var sum=0;
        for (i = 1; i < myTab.rows.length-1; i++) {
            var objCells = myTab.rows.item(i).cells;
            sum+=parseFloat(objCells[4].innerHTML)
        }
  document.getElementById("sumOfProducts").innerHTML = sum.toFixed(2)+"zł";
}