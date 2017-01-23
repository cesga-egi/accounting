
// Return an array of the selected opion values
// // select is an HTML select element
function getSelectValues(select) {
  var result = [];
  var options = select && select.options;
  var opt;

  for (var i=0, iLen=options.length; i<iLen; i++) {
    opt = options[i];

    if (opt.selected) {
      result.push(opt.value || opt.text);
    }
  }
  return result;
}
//
function setDefaultValues(){
	if (document.getElementById('monthsSelect').value=="")
		document.getElementById('monthsSelect').value=11;
	if (document.getElementById('fromSelect').value=="") {
		var monthNames = ["January", "February", "March", "April", "May", "June",
		                  "July", "August", "September", "October", "November", "December"
		                ];
		var d = new Date();
		//Set the default date to one year ago
		document.getElementById('fromSelect').value="January" + " " + (d.getYear()+1900).toString();
		$('.selectMultiple option').each(function (index2){
			this.selected='selected';
		});
		$('.saveButton').each(function (index2){
			this.style.visibility='hidden';//selected='selected';
		});

    }
}
//
function getUrlParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) 
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) 
        {
            return sParameterName[1];
        }
    }
} 

function addMonths(dateObj, num) {

    var currentMonth = dateObj.getMonth() + dateObj.getFullYear() * 12;
    dateObj.setMonth(dateObj.getMonth() + num);
    var diff = dateObj.getMonth() + dateObj.getFullYear() * 12 - currentMonth;

    // If don't get the right number, set date to 
    //     // last day of previous month
             if (diff != num) {
                dateObj.setDate(0);
             } 
            return dateObj;
    }


function checkData(){    
    var from = $('#fromSelect').val();
    var months = parseInt(document.getElementById('monthsSelect').value);
    var fromDate = new Date(from)
    var toDate = addMonths(fromDate, months)
    var lastMonth = new Date()
    lastMonth.setMonth(lastMonth.getMonth());
    if (toDate > lastMonth) {
    	alert("End Date of the report is invalid");
    	return false;
    }
    if (isNaN(months)){
    	alert("The number of months is not a number!");
    	return false;
    }
    var url= '/wlcg/report/tier1/?from=' + from + '&months=' + months;
    
    var a=['tables', 'graphs', 'federations', 'experiments'];
    for (index = 0; index < a.length; ++index) {
    	var data = getSelectValues(document.getElementById(a[index] +'Select'));
		if (data && data.length>0)
			url  +=  "&" + a[index] + "=" + data;
    }
    if (document.getElementById('accCheck').checked)
    	url +='&accsum=1';
    if (document.getElementById('expCheck').checked)
    	url +='&expsum=1';
    if (document.getElementById('daysCheck').checked)
    	url +='&metricdays=1';
    
    window.location.href = url;
  }; 

//create canvas function from highcharts example http://jsfiddle.net/highcharts/PDnmQ/
function myCreateCanvas(myHighChart)  {
    var svg = myHighChart.getSVG(),
    width = parseInt(svg.match(/width="([0-9]+)"/)[1]),
    height = parseInt(svg.match(/height="([0-9]+)"/)[1]),
    canvas = document.createElement('canvas');

    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);

    if (canvas.getContext && canvas.getContext('2d')) {
       canvg(canvas, svg);
       return canvas.toDataURL("image/jpeg");
    } 

    alert("Your browser doesn't support this feature, please use a modern browser");
   return false;
}

function tableToJson(table) {
    var data = [];

    // first row needs to be headers
    var headers = [];
    for (var i=0; i<table.rows[0].cells.length; i++) {
        headers[i] = table.rows[0].cells[i].innerHTML.toLowerCase().replace(/ /gi,'');
    }


    // go through cells
    for (var i=0; i<table.rows.length; i++) {

        var tableRow = table.rows[i];
        var rowData = {};

        for (var j=0; j<tableRow.cells.length; j++) {

            rowData[ headers[j] ] = tableRow.cells[j].innerHTML;

        }

        data.push(rowData);
    }
   return data;
}
function  prepareTable(res){
	var title=res.columns[0];
	var key=title;
	var newcolumns=[{title:title, key:key /*, width:60 */}];		
	for (var i=1; i<res.columns.length; i++){
		newcolumns.push({title:res.columns[i], key:res.columns[i]} )			
	} 
	res.columns=newcolumns;
	for  (var j=0; j<res.data.length; j++) {
		var new_cell={};
		for (var k=0; k<res.data[j].length; k++)
			new_cell[ res.columns[k].key]=res.data[j][k];			
		res.data[j]=new_cell;
		
	}
	//}
	return res;
}
function getReportDates(){
	var monthNames = [
	                  "January", "February", "March",
	                  "April", "May", "June", "July",
	                  "August", "September", "October",
	                  "November", "December"
	              ];
	var startDate=new Date(Date.parse('1 '+ document.getElementById('fromSelect').value));
	var number=parseInt(document.getElementById('monthsSelect').value);

	var endDate = new Date(Date.parse('1 '+ document.getElementById('fromSelect').value));
	endDate.setMonth(endDate.getMonth() + number -1);
	var my_string= monthNames[startDate.getMonth()];

	if (startDate.getFullYear()!= endDate.getFullYear())
		my_string +=' ' + startDate.getFullYear().toString();

	return my_string +' to ' + monthNames[endDate.getMonth()]+' ' + endDate.getFullYear().toString();
}


function createTemplatePage(doc, siteName,  headerFunction, tabName, notes, pageNumber, summary){
	
	       var totalRows=[];

	    var cellFunction = function (my_cell, my_info) {
	    	if (my_cell.raw.indexOf('Total')>-1 || my_cell.raw.indexOf('TOTAL')>-1){
	    		//alert("DOING A TOTAL ROW" + value);
    		     totalRows.push(my_info.row.index);
	    	}
	    	var totaloffset=0;
	    	
	    	if (totalRows.indexOf(my_info.row.index)>-1){
	    	  //alert("PUTTING A SPECIAL COLOR");
	    	   totaloffset=30;
	    	} 
	    	if (my_info.column.dataKey.indexOf('MoU')>-1 || my_info.column.dataKey.indexOf('Total')>-1)
	    		totaloffset+=30;

	    	doc.setFillColor(my_info.row.index % 2 === 0 ? 245-totaloffset : 255-totaloffset);
	    };	    
    doc.addPage();
    doc.addImage('wlcg_logo', 5, 5, 30, 30); // use the cached image

    doc.setFontSize(22);
    doc.setFontType("bold");
    if (summary) {
	doc.text(45,12, 'WLCG Accounting Summary');
    } else {
       doc.text(45,12, 'WLCG Accounting');
       doc.setFontSize(15);
       doc.text(45,27, 'Centre:  ');
    }
    doc.setFontSize(15);
    doc.setTextColor(0,0,255);

    if (summary) {
        doc.text(45,27, siteName);
    } else {
        doc.text(75,27, siteName);
    }
	doc.text(45, 19, getReportDates());

	//if (notes)
	//	doc.text(44,34,  notes);
	doc.setFontType("normal");
	doc.setFontSize(10);
	doc.setTextColor(100);
	//doc.text(45, 30, 'Please report accounting data in the shaded cells and return the report to lcg.office@cern.ch');
	var notesText={'cpu':[
	                      {'Notes':'* Local Wallclock Work', ' ':'Sum of wallclock time used by jobs submitted locally as reported by the batch system during the referenced month multiplied by benchmarked HEPSPEC06 of the CPU resource and by number of processors.'},
	                      {'Notes':'** Global Wallclock Work', ' ':'Sum of wallclock time used by jobs submitted to the distributed infrastructure as reported by the batch system during the referenced month multiplied by benchmarked HEPSPEC06 of the CPU resource and by number of processors.'},
	                      {'Notes':'*** MoU pledge', ' ':'MoU CPU Pledge for a given month in HEPSEPC06 hours or days depending on the selected unit'},
                              {'Notes':'**** MoU%', ' ':'Total Wallclock work during referenced period as % of MoU CPU pledge for the same period'},
	                      ],
			   'disk':[   {'Notes':' ', ' ':'Space used/allocated at end of the calendar month'},
	                      {'Notes':'* MoU pledge', ' ':'pledge in MoU for data storage'},
                              {'Notes':'** installed capacity', ' ':'capacity installed (TB)'},
                              {'Notes':'*** Total', ' ':'in TB per month'},
			           ],
                           'graph': [ {'Notes':'* Wallclock Work', ' ':'Sum of wallclock time used by jobs as reported by the batch system during the referenced month multiplied by benchmarked HEPSPEC06 of the CPU resource and by number of processors.'},],
                        'summary':[ {'Notes':'* Wallclock Work', ' ':'Sum of wallclock time used by jobs as reported by the batch system during the referenced month multiplied by benchmarked HEPSPEC06 of the CPU resource and by number of processors.'},
{'Notes':'** disk/tape used in year to date', ' ':'Sum of TBytes occupied by the end of every month of the referenced period.'}
]  
			}
	if (tabName){
	    createStandardTables(tabName, doc, headerFunction);
        }
        if (notes) {
	      var tableType='graph';
	      if ((notes.indexOf('Disk')>-1) || (notes.indexOf('Tape')>-1))
	          tableType='disk';
	      if (notes.indexOf('Wall')>-1)
	    	  tableType='cpu';
              if (notes.indexOf('summary')>-1)
                  tableType='summary';
	      doc.autoTable([{'title':'Notes', 'key':'Notes'}, {'title':' ', 'key':' ' }], 
	    		  notesText[tableType],
	    		  { margin: {right: 170, left: 5, top: 180, bottom: 0},
	        	 styles: { startY: false, cellPadding:1 ,fontSize: 6, rowHeight: 3,  //renderHeaderCell: headerFunction, 
	        	overflow: 'linebreak', columnWidth: 'wrap'},
                                        drawCell: cellFunction,
});
	}
	var dt1 = new Date();
	var utcDate = dt1.toUTCString();
	doc.setFontSize(6);

	doc.text(120,205, 'Page ' + pageNumber.toString() + '                                        ' + siteName + '                                             ' + utcDate );

	doc.setFontSize(10);


}
function 	createExperimentSummaryPage(doc,  headerFunction, pageNumber){
	       var totalRows=[];

	    var cellFunction = function (my_cell, my_info) {
	    	if (my_cell.raw.indexOf('Total')>-1 || my_cell.raw.indexOf('TOTAL')>-1){
	    		//alert("DOING A TOTAL ROW" + value);
    		     totalRows.push(my_info.row.index);
	    	}
	    	var totaloffset=0;
	    	
	    	if (totalRows.indexOf(my_info.row.index)>-1){
	    	  //alert("PUTTING A SPECIAL COLOR");
	    	   totaloffset=30;
	    	} 
	    	if (my_info.column.dataKey.indexOf('MoU')>-1 || my_info.column.dataKey.indexOf('Total')>-1)
	    		totaloffset+=30;

	    	doc.setFillColor(my_info.row.index % 2 === 0 ? 245-totaloffset : 255-totaloffset);
	    };	    
	createTemplatePage(doc, 'All Tier-1s + CERN', headerFunction, false, false, pageNumber, true);

	
	var margin={'0': {right: 180, left: 5, top: 35, bottom: 0},
			'1': {right: 5, left: 150, top: 35, bottom: 0},
			'2': {right: 180, left: 5, top: 110, bottom: 0},
			'3': {right: 5, left: 150, top: 110, bottom: 0},
			}
	$('#tabs__Experiment_Summary_Page .datatableH').each(function (index2) {
        var res = doc.autoTableHtmlToJson(this, true);
        res=prepareTable(res);
        doc.autoTable(res.columns, res.data, { margin: margin[index2],
        	styles: {startY: false, cellPadding:1 ,fontSize: 5, rowHeight: 3, columnWidth:'auto', renderHeaderCell: headerFunction, 
        	overflow: 'linebreak'}, drawCell: cellFunction
        });    	
    });
}
function 	createAccountingSummaryPage(doc,  headerFunction, pageNumber){
	createTemplatePage(doc, 'All Tier-1s + CERN', headerFunction, false, 'summary', pageNumber, true);

	       var totalRows=[];

	    var cellFunction = function (my_cell, my_info) {
	    	if (my_cell.raw.indexOf('Total')>-1 || my_cell.raw.indexOf('TOTAL')>-1){
	    		//alert("DOING A TOTAL ROW" + value);
    		     totalRows.push(my_info.row.index);
	    	}
	    	var totaloffset=0;
	    	
	    	if (totalRows.indexOf(my_info.row.index)>-1){
	    	  //alert("PUTTING A SPECIAL COLOR");
	    	   totaloffset=30;
	    	} 
	    	if (my_info.column.dataKey.indexOf('MoU')>-1 || my_info.column.dataKey.indexOf('Total')>-1)
	    		totaloffset+=30;

	    	doc.setFillColor(my_info.row.index % 2 === 0 ? 245-totaloffset : 255-totaloffset);
	    };	    
	
    doc.setFillColor(41, 128, 185);
    doc.rect(02, 40, 77, 10, 'F');
    doc.rect(77, 40, 17, 10, 'F');
    doc.rect(94, 40, 40, 10, 'F');
    doc.rect(134, 40, 60, 10, 'F');
    doc.rect(194, 40, 41, 10, 'F');
    doc.rect(235, 40, 60, 10, 'F');

    doc.setFontSize(6);
    doc.setFontStyle('bold');
    doc.setTextColor(255,255,255);

    doc.text(18,43, 'Wallclock Work in HEPSPEC06');
    doc.text(18,46, 'hours/days during the referenced period*');
    doc.text(65,44, ' disk used in year to date **');
    doc.text(124,44,' disk at end of period');
    doc.text(185,44,' tape used in year to date **');
    doc.text(245, 44, ' tape at end of period' );	

    doc.setFontSize(10);
    doc.setTextColor(100);
    
	var margin={'0': {right: 2, left: 2, top: 47, bottom: 0},
			'1': {right: 80, left: 5, top: 120, bottom: 0},
			};
    var columnStyle={'0': {'Site Summary':{columnWidth:20}, 
'% installed':{columnWidth:13}, 
'% pledge':{columnWidth:12},            
'cpu installed **':{columnWidth:17}, 
'TByte-months':{columnWidth:16}, 
'% installed ':{columnWidth:13}, 
'% pledge ':{columnWidth:12}, 
'TBytes occup.':{columnWidth:19}, 
'occupied *':{columnWidth:12}, 
'occupied **':{columnWidth:14}, 
'installed **':{columnWidth:14}, 
'TByte-months ':{columnWidth:16}, 
'% installed  ':{columnWidth:13}, 
'% pledge  ':{columnWidth:12}, 
'TBytes occup. ':{columnWidth:19}, 
'occupied * ':{columnWidth:13}, 
'occupied ** ':{columnWidth:14},    
'installed ** ':{columnWidth:14},    

}, '1':{}};
			
	$('#tabs__Accounting_Summary_Page .datatableH').each(function (index2) {
        var res = doc.autoTableHtmlToJson(this, true);
        if (index2==0) {
	        var data = [],
	            headers = [],
	            header = this.rows[1],
	            tableRow,
	            rowData,
	            i,
	            j;
	
	        for (i = 0; i < header.cells.length; i++) {
	            headers.push(typeof header.cells[i] !== 'undefined' ? header.cells[i].textContent : '');
	        }
	
	        for (i = 2; i < this.rows.length; i++) {
	            tableRow = this.rows[i];
	            rowData = [];
	            for (j = 0; j < header.cells.length; j++) {
	                rowData.push(typeof tableRow.cells[j] !== 'undefined' ? tableRow.cells[j].textContent : '');
	            }
	            data.push(rowData);
	        }
	        res =  { columns: headers, data: data, rows: data };
	    }
        
        res=prepareTable(res);
        doc.autoTable(res.columns, res.data, { margin: margin[index2], 
        	 styles:  { startY: false, cellPadding:0.1 ,fontSize: 6, rowHeight: 3, columnWidth: 'auto' ,//renderHeaderCell: headerFunction, 
        	overflow: 'linebreak'}, drawCell: cellFunction,        
        });    	
    });
}

function createStandardTables(tabName, doc, headerFunction){
	
	       var totalRows=[];

	    var cellFunction = function (my_cell, my_info) {
	    	if (my_cell.raw.indexOf('Total')>-1 || my_cell.raw.indexOf('TOTAL')>-1){
	    		//alert("DOING A TOTAL ROW" + value);
    		     totalRows.push(my_info.row.index);
	    	}
	    	var totaloffset=0;
	    	
	    	if (totalRows.indexOf(my_info.row.index)>-1){
	    	  //alert("PUTTING A SPECIAL COLOR");
	    	   totaloffset=30;
	    	} 
	    	if (my_info.column.dataKey.indexOf('MoU')>-1 || my_info.column.dataKey.indexOf('Total')>-1)
	    		totaloffset+=30;

	    	doc.setFillColor(my_info.row.index % 2 === 0 ? 245-totaloffset : 255-totaloffset);
	    };	    
	$(tabName +' .pledge_table').each(function (index2) {
        var res = doc.autoTableHtmlToJson(this, true);
        res=prepareTable(res);
        doc.autoTable(res.columns, res.data, { margin: {right: 65, left: 185, top: 7, bottom: 0} ,
        	styles: {startY: false, cellPadding:1 ,fontSize: 6, rowHeight: 3, //renderHeaderCell: headerFunction, 
        	overflow: 'linebreak'}, drawCell: cellFunction, columnStyles:{' MoU pledges ':{columnWidth:20}} 
        });    	
    });
}
function saveToJson() {

	var query = window.location;

	window.open(query +'&type=json');
}

function createFirstPage(doc){
    var wlcg_logo='data:image/jpeg;base64,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';			
	doc.addImage(wlcg_logo, 'JPEG', 120, 20, 50, 50, 'wlcg_logo');	
	doc.setFontSize(50);

	//doc.text(120,80, 'WLCG');
    doc.centeredText("WLCG",{align: "center"},0,80);

	doc.setFontSize(12);
//	doc.text(115,90, 'Worldwide LHC Computing Grid');
    doc.centeredText("Worldwide LHC Computing Grid",{align: "center"},0,90);

	doc.setFontSize(20);

	
    doc.centeredText("WLCG Accounting Report",{align: "center"},0,130);

    doc.centeredText(getReportDates(),{align: "center"},0,140);
    doc.centeredText('Tier-1 Centres + CERN',{align: "center"},0,150);

	
}
function saveToPdf() {

	(function(API){
	    API.centeredText = function(txt, options, x, y) {
	        options = options ||{};
	        /* Use the options align property to specify desired text alignment
	         * Param x will be ignored if desired text alignment is 'center'.
	         * Usage of options can easily extend the function to apply different text 
	         * styles and sizes 
	        */
	        if( options.align == "center" ){
	            // Get current font size
	            var fontSize = this.internal.getFontSize();

	            // Get page width
	            var pageWidth = this.internal.pageSize.width;

	            // Get the actual text's width
	            /* You multiply the unit width of your string by your font size and divide
	             * by the internal scale factor. The division is necessary
	             * for the case where you use units other than 'pt' in the constructor
	             * of jsPDF.
	            */
	            txtWidth = this.getStringUnitWidth(txt)*fontSize/this.internal.scaleFactor;

	            // Calculate text's x coordinate
	            x = ( pageWidth - txtWidth ) / 2;
	        }

	        // Draw text at x,y
	        this.text(txt,x,y);
	    }
	})(jsPDF.API);
	  var doc = new jsPDF('landscape');

	       var totalRows=[];

	    var cellFunction = function (my_cell, my_info) {
	    	if (my_cell.raw.indexOf('Total')>-1 || my_cell.raw.indexOf('TOTAL')>-1){
	    		//alert("DOING A TOTAL ROW" + value);
    		     totalRows.push(my_info.row.index);
	    	}
	    	var totaloffset=0;
	    	
	    	if (totalRows.indexOf(my_info.row.index)>-1){
	    	  //alert("PUTTING A SPECIAL COLOR");
	    	   totaloffset=30;
	    	} 
	    	if (my_info.column.dataKey.indexOf('MoU')>-1 || my_info.column.dataKey.indexOf('Total')>-1)
	    		totaloffset+=30;

	    	doc.setFillColor(my_info.row.index % 2 === 0 ? 245-totaloffset : 255-totaloffset);
	    };	    
	  
		doc.setFont("helvetica");	  
	  
	  // All units are in the set measurement for the document
	    // This can be changed to "pt" (points), "mm" (Default), "cm", "in"
	    var pageNumber=2;
	    
	    createFirstPage(doc);
	    doc.setFontSize(6);

	    var headerFunction = function (x, y, width, height, key, value, settings) {
	        doc.setFillColor(79, 129, 189); // Turquoise
	        doc.setTextColor(255, 255, 255);
	        //doc.setFontStyle('bold');
	        doc.rect(x, y, width, height, 'F');
	        y += settings.lineHeight / 2 + doc.internal.getLineHeight() / 2;
//	        if (x<10)
//	        	y -=3;
	        doc.text('' + key, x + settings.padding, y);
	    };
	    $('.mySites').each(function (index){
	    	var siteName=this.text;
	    	if (siteName== ' Experiment Summary Page'){
	    	    createExperimentSummaryPage(doc, headerFunction, pageNumber);
		    	pageNumber +=1;
	    	}else if (siteName == ' Accounting Summary Page'){
	    		createAccountingSummaryPage(doc,  headerFunction, pageNumber);
		    	pageNumber +=1;
	    	} else 	{
	    		var tabName='#tabs_'+this.text;
	    		if (this.text == 'All Tier-1s  ')
	    			tabName='#tabs_All_Tier-1s__';
	    		if (this.text == 'All Tier-1s + CERN')
	    			tabName='#tabs_All_Tier-1s_and_CERN';
			$(tabName+' .datatableH').each(function (index2) {

		    	      createTemplatePage(doc, siteName,  headerFunction, tabName, this.rows[0].children[0].textContent, pageNumber, false );
			    	pageNumber +=1;
			
			        var res = doc.autoTableHtmlToJson(this, true);
			        res=prepareTable(res);
                                var first_column=res.columns[0]['title'];
			        doc.autoTable(res.columns, res.data, { margin: {right: 5, left: 5, top: 35, bottom: 0},
			        	styles:{ startY: false, cellPadding:1 ,fontSize: 6, rowHeight: 4, columnWidth: 'auto',
			        	overflow: 'linebreak', },
                                        columnStyles:{0:{columnWidth:'auto'}, 1:{columnWidth:'auto'}},
                                        drawCell: cellFunction,

			        });    	
                              if (index2==2) {
                                 doc.rect(20,125,240,30, 'D');
                                 doc.text(20,120, 'Comments:');
                              }
			    });

	    	    createTemplatePage(doc, siteName, headerFunction, false, 'graph', pageNumber, false );
	    	    pageNumber +=1;
			    //loop through each chart
			    $(tabName + ' .myChart').each(function (index) {
			        var imageData = myCreateCanvas($(this).highcharts());
			        /**
			        * addImage(imagedata, type, x, y, width, height)
			        */
			        var y=40;
			        if (index>2)
			        	y=110;
			        var x=10 + (index % 3)*90;
			        doc.addImage(imageData, 'JPEG', x,  y, 90, 60);
			    });
	    	}
	    });

	  //save with name  
	  doc.save('Accounting.pdf');

	};
  
  
