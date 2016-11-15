$.fn.dataTableExt.oApi.fnReloadAjax = function (oSettings, sNewSource, fnCallback) {
    if ( typeof sNewSource != 'undefined' ) {
        oSettings.sAjaxSource = sNewSource;
     }
    this.fnClearTable( this );
    this.oApi._fnProcessingDisplay( oSettings, true );
    var that = this;

    $.getJSON( oSettings.sAjaxSource, null, function(json) {
        /* Got the data - add it to the table */
        for ( var i=0 ; i<json.aaData.length ; i++ ) {
            that.oApi._fnAddData( oSettings, json.aaData[i] );
        }
        oSettings.aiDisplay = oSettings.aiDisplayMaster.slice();
        that.fnDraw( that );
        that.oApi._fnProcessingDisplay( oSettings, false );
        /* Callback user function - for event handlers etc */
        if ( typeof fnCallback == 'function' ) {
            fnCallback( oSettings );
        }
    } );
}

jQuery.fn.dataTableExt.oSort['percent-asc']  = function(a,b) {
	var x = a.toString().replace( /<.*?>/g, "" );
	var y = b.toString().replace( /<.*?>/g, "" );
	x = (x == "-") ? 0 : x.replace( /%/, "" );
	y = (y == "-") ? 0 : y.replace( /%/, "" );
	if (x == "") x = 0;
	if (y == "") y = 0;
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ? -1 : ((x > y) ?  1 : 0));
};

jQuery.fn.dataTableExt.oSort['percent-desc'] = function(a,b) {
	var x = a.toString().replace( /<.*?>/g, "" );
	var y = b.toString().replace( /<.*?>/g, "" );
	x = (x == "-") ? 0 : x.replace( /%/, "" );
	y = (y == "-") ? 0 : y.replace( /%/, "" );
	if (x == "") x = 0;
	if (y == "") y = 0;
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ?  1 : ((x > y) ? -1 : 0));
};

jQuery.fn.dataTableExt.oSort['numeric-comma-asc']  = function(a,b) {
    var x = a.toString().replace( /<.*?>/g, "" );
	var y = b.toString().replace( /<.*?>/g, "" );
	x = (x == "") ? 0 : x.replace( /,/g, "" );
	y = (y == "") ? 0 : y.replace( /,/g, "" );
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ? -1 : ((x > y) ?  1 : 0));
};

jQuery.fn.dataTableExt.oSort['numeric-comma-desc'] = function(a,b) {
    var x = a.toString().replace( /<.*?>/g, "" );
	var y = b.toString().replace( /<.*?>/g, "" );
	x = (x == "") ? 0 : x.replace( /,/g, "" );
	y = (y == "") ? 0 : y.replace( /,/g, "" );
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ?  1 : ((x > y) ? -1 : 0));
};