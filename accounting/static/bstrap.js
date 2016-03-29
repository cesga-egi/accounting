$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
$('#collapseOne').collapse("hide");
$("#inputMetric").on('mouseleave', function(e) {
    $('#inputMetric').popover('destroy');
});

$("#inputMetric").on('mouseover', function(e) {
    var $e = $(e.target); 
    if ($e.is('option')) {
        $('#inputMetric').popover('destroy');
        $("#inputMetric").popover({
            trigger: 'manual',
            placement: 'down',
            title: $e.attr("data-title"),
            content: $e.attr("data-content")
        }).popover('show');
    }
});

$.getScript("http://eternicode.github.io/bootstrap-datepicker/bootstrap-datepicker/js/bootstrap-datepicker.js", function(){

var startDate = new Date('01/01/2004');
var FromEndDate = new Date();
var ToEndDate = new Date();

ToEndDate.setDate(ToEndDate.getDate()+365);

$('#from_date').datepicker({
    
    startView: "years",
  minViewMode: "months",
    format: 'mm/yyyy',
    startDate: startDate,
    endDate: FromEndDate, 
    autoclose: true
})
    .on('changeDate', function(selected){
        startDate = new Date(selected.date.valueOf());
        startDate.setDate(startDate.getDate(new Date(selected.date.valueOf())));
        $('.to_date').datepicker('setStartDate', startDate);
    }); 
$('#to_date')
    .datepicker({
        viewMode: 'years',
        minViewMode: "months",
        format: 'mm/yyyy',
        startDate: startDate,
        endDate: FromEndDate,
        autoclose: true
    })
    .on('changeDate', function(selected){
        FromEndDate = new Date(selected.date.valueOf());
        FromEndDate.setDate(FromEndDate.getDate(new Date(selected.date.valueOf())));
        $('.from_date').datepicker('setEndDate', FromEndDate);
    });

  
  
});



