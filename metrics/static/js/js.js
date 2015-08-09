/**
 * Created by Sylvestre on 8/9/2015.
 */
$( document ).ready(function() {

    //Initiate Chart's parameter.
    var catalog1 = {
                    "type": "serial",
                    "dataLoader": {
                                    "url": "http://127.0.0.1:8000/CSV/Years/",
                                    "format": "csv",
                                    "delimiter": ",",       // column separator
                                    "useColumnNames": true, // use first row for column names
                                    "skip": 1               // skip header row
                                },
                                "categoryField": "category",
                                "angle": 17,
                                "marginBottom": 18,
                                "plotAreaBorderColor": "#FFFFFF",
                                "plotAreaFillColors": "#0000FF",
                                "startDuration": 0.5,
                                "startEffect": "easeOutSine",
                                "color": "#FFFFFF",
                                "fontFamily": "Abel",
                                "fontSize": 12,
                                "handDrawn": true,
                                "categoryAxis": {
                                    "autoRotateAngle": 45,
                                    "autoRotateCount": 0,
                                    "gridPosition": "start",
                                    "axisColor": "#FFFFFF",
                                    "fontSize": 16,
                                    "gridColor": "#FFFFFF",
                                    "labelOffset": 5,
                                    "tickLength": 7,
                                    "handDrawn": true
                                },
                            "trendLines": [],
                            "graphs": [
                                {
                                    "balloonText": "[[category]] : [[value]]",
                                    "columnWidth": 0.13,
                                    "fillAlphas": 1,
                                    "fillColors": "#FFFFFF",
                                    "fontSize": 0,
                                    "gapPeriod": null,
                                    "id": "AmGraph-1",
                                    "lineColor": "#FFFFFF",
                                    "lineThickness": 0,
                                    "negativeFillAlphas": 0,
                                    "showAllValueLabels": true,
                                    "title": "graph 1",
                                    "topRadius": 0,
                                    "type": "column",
                                    "valueAxis": "ValueAxis-1",
                                    "valueField": "column-1"
                                }
                            ],
                            "guides": [],
                            "valueAxes": [
                                {
                                    "id": "ValueAxis-1",
                                    "autoGridCount": false,
                                    "axisColor": "#FFFFFF",
                                    "title": ""
                                }
                            ],
                            "allLabels": [],
                            "balloon": {},
                            "titles": [],
                            "dataProvider": []
                };

    var catalog2 = {
	"type": "pie",
    "dataLoader": {
                                    "url": "http://127.0.0.1:8000/CSV/Parties/",
                                    "format": "csv",
                                    "delimiter": ",",       // column separator
                                    "useColumnNames": true, // use first row for column names
                                    "skip": 1               // skip header row
                                },
	"balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
	"colors": [
		"#003399",
		"#EE3233",
		"#6C7476"
	],
	"labelTickColor": "#FFFFFF",
	"outlineThickness": 5,
	"titleField": "category",
	"valueField": "column-1",
	"color": "#FFFFFF",
	"fontSize": 14,
	"handDrawn": true,
	"handDrawThickness": 3,
	"theme": "light",
	"allLabels": [],
	"balloon": {},
	"titles": [],
	"dataProvider": []
    };

    //Set DataLoader and div for chart.
    catalog1.dataLoader.url = 'http://127.0.0.1:8000/CSV/Counties/';
    var div1 = "chartdiv2";

    catalog2.dataLoader.url = 'http://127.0.0.1:8000/CSV/Counties/';
    var div2 = "chartdiv3";

    //Chart drawing function.
    function make_chart(dom_id,catalog){
                    AmCharts.makeChart(dom_id, catalog);
    }

    //Draw chart.
    make_chart(div1,catalog1);
    make_chart(div2,catalog2);

    $('#vys').change(function(){

        console.log('You clicked the option!');
        var value = $(this).val();

        console.log(value);

        catalog1.dataLoader.url = "http://127.0.0.1:8000/CSV/Years/" + value;

        make_chart(div1,catalog1);

    });

    $('.vyp').change(function(){

        console.log('You clicked the option!');
        var value = $(this).val();

        console.log(value);

        catalog2.dataLoader.url = "http://127.0.0.1:8000/CSV/Parties/" + value;

        make_chart(div2,catalog2);

    });






});

