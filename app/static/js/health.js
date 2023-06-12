// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['line']});

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

var getHealthInfo = function(){
    console.log(data);
    title = "Health Statistics";
    //console.log(title);
    drawChart(data,title);
    };

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(getHealthInfo);

function drawChart(input,title) {

    // Create the data table.
    var data_table = new google.visualization.DataTable();
    data_table.addColumn('string', 'Date');
    data_table.addColumn('number', 'Time Slept (in minutes');
    data_table.addColumn('number', 'Calories Consumed');
    data_table.addColumn('number', 'Time Spent Undergoing Physical Activity');
    
    data_table.addRows(input);

    var options = {
        chart: {
          title: title,
        },
        width: 900,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('chart_div'));

      chart.draw(data_table, google.charts.Line.convertOptions(options));
}