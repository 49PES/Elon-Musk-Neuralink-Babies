// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['line']});

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

var getHealthInfo = function(){

    console.log(data);

    dates = data.map(d => d[0]);
    sleep = data.map(d => d[1]);
    calories = data.map(d => d[2]);
    exercise = data.map(d => d[3]);


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
    data_table.addColumn('number', 'Time Slept (in minutes)');
    data_table.addColumn('number', '# of Calories Consumed');
    data_table.addColumn('number', 'Hours of Physical Activity');
    
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