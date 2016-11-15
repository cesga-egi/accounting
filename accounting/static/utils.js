function CommaFormatted(amount) {
    var isInt = parseInt(amount);
    if (isNaN(isInt)) return amount; 
    if (isInt == 0) return 0;
    isInt=isInt.toString().replace(/^0+/, ''); 
    isInt += '';
    var x = isInt.split('.');
    var x1 = x[0];
    var x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

//To remove the comma for the variables
function RemoveCommaFormatted(amount) {
  var amount = amount.toString().replace(/,/g,"");
  return amount;
}

function myInt(amount) {
  var isInt = parseInt(amount);
  if (isNaN(isInt)) return 0; 
  return isInt;
}