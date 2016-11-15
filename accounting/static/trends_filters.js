
// ==========
// = TRENDS =
// ==========

var PLOT_NUMBER_OF_JOBS = 1;
var PLOT_CPU_TIME_USED = 3;
var PLOT_CPU_WALL_TIME_USED = 5;
var PLOT_CPU_EFFICENCY = 7;
var PLOT_PERC_HOURS_USED = 9;


function add_tier0_option(){
	if (!$("#site option[value='CH-CERN']").length){
		ch_cern = $('<option value="CH-CERN">CH-CERN</option>');
		ch_cern.prependTo('#tier1_group');
	}
}


function plot_filters(auto){
	/*
		shows and hides filters depending on plot type and sites.
		auto is false when the user triggered the change.
	*/

	plot = $('#view').val();
	group = $('#groups').val();

	// show sites or countries depending on selected group
	if (group == 'tier0') {
		add_tier0_option();
		$("#site option[value='CH-CERN']").attr('selected', true);
		$("#site").attr('disabled', true);
		$("#countries").hide();
		$("#bestnm").hide();

	}else if (group == 'tier1' || group == 'tier01'){
		$("#site").attr('disabled', false);
		if (!auto){
			$("#site option[value='all']").attr('selected', true);
		}
		$("#sites").show();
		$("#countries").hide();
		$("#bestnm").show();

		if (group == 'tier1'){
			$("#site option[value='CH-CERN']").remove();
		}else{
			add_tier0_option();
		}

	}else if (group == 'tier2'){
		$("#sites").hide();
		$("#countries").show();
		$("#bestnm").show();
	}

	//#$("#vos").show();
	$("#vo").removeAttr("multiple");
	// plot specific filters
	if (plot == PLOT_PERC_HOURS_USED){
		//$("#vos").hide();
		$("#vo").attr("multiple","multiple");
		if (group == 'tier2'){
			$("#countries").show();
			$("#sites").hide();
		}else{
			$("#sites").show();
			$("#countries").hide();
		}
	}
	if (plot == PLOT_CPU_EFFICENCY && !auto){
		$('#plottypel').attr('checked', true);
	}else if (!auto){
		$('#plottypeb').attr('checked', true);
	}
}


function dehighlight_months(monthpicker){
	monthpicker.find('td.mtz-monthpicker-month').removeClass('ui-state-active');
	monthpicker.find('td.mtz-monthpicker-month').addClass('ui-state-default');
}

function highlight_month(monthpicker, month){
	dehighlight_months(monthpicker);
	month = monthpicker.find('td.mtz-monthpicker-month[data-month="' + month + '"]');
	month.removeClass('ui-state-default');
	month.addClass('ui-state-active');
}

$(document).ready(function(){
	// start with the proper filters
	
	$('#plottype input[value="{{ plottype }}"]').attr('checked', true);
	$("#view option[value='{{ view }}']").attr('selected', true);
	$("#groups option[value='{{ group }}']").attr('selected', true);
	plot_filters(true);
	//alert ( "{{ selected_vo }}");
	$("#vo option[selected]").attr('selected', true);
	
	$('#view').bind('change', function(){
		plot_filters(false);
	});

	$('#groups').bind('change', function(){
		plot_filters(false);
	})

	$('#period-fixed-options input').bind('click', function(){
		$('#period-fixed').attr('checked', true);
	});

	$('#period-custom-options input').bind('click', function(){
		$('#period-custom').attr('checked', true);
	});

	date = new Date();
	year = date.getFullYear();
	month = date.getMonth();

	// start month pickers
    $("#startdate").monthpicker({
		id: 'monthpicker_startdate',
		pattern: 'mm-yyyy',
		startYear: 2006,
		finalYear: year
	});
    $("#enddate").monthpicker({
		id: 'monthpicker_enddate',
		pattern: 'mm-yyyy',
		startYear: 2006,
		finalYear: year
	});

	// highlight current selected months
	start_month = parseInt($("#startdate").val().split('-')[0], 10);
	highlight_month($('#monthpicker_startdate'), start_month);
	end_month = parseInt($("#enddate").val().split('-')[0], 10);
	highlight_month($('#monthpicker_enddate'), end_month);

	// bind month highlighting actions
	$("#startdate").monthpicker().bind('monthpicker-click-month', function(e, month){
		highlight_month($('#monthpicker_startdate'), month);
	});
	$("#enddate").monthpicker().bind('monthpicker-click-month', function(e, month){
		highlight_month($('#monthpicker_enddate'), month);
	});
	$("#startdate").monthpicker().bind('monthpicker-change-year', function(e, year){
		dehighlight_months($('#monthpicker_startdate'));
	});
	$("#enddate").monthpicker().bind('monthpicker-change-year', function(e, year){
		dehighlight_months($('#monthpicker_enddate'));
	});
});
