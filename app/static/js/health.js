// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['line']});


// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

var getHealthInfo = function(){

    console.log(data);
    drawSleep(data,"Sleep Stats");
    drawCalories(data,"Calories Stats");
    drawExercise(data,"Exercise Stats");
    };

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(getHealthInfo);

function drawCalories(input,title) {
    console.log(input)
    var data_table = new google.visualization.DataTable();
    data_table.addColumn('string', 'Date');
    data_table.addColumn('number', '# of Calories Consumed');

    const calories = input.map(subArray => [subArray[0], subArray[2]]);

    data_table.addRows(calories);

    var options = {
        chart: {
          title: title,
        },
        width: 600,
        height: 350
      };
      console.log(calories);
      var chart = new google.charts.Line(document.getElementById('calories_div'));

      chart.draw(data_table, google.charts.Line.convertOptions(options));
}

function drawSleep(input,title) {
  console.log(input)
  var data_table = new google.visualization.DataTable();
  data_table.addColumn('string', 'Date');
  data_table.addColumn('number', '# of Minutes of Sleep');

  const sleep = input.map(subArray => [subArray[0], subArray[1]]);

  data_table.addRows(sleep);

  var options = {
      chart: {
        title: title,
      },
      width: 600,
      height: 350
    };

    var chart = new google.charts.Line(document.getElementById('sleep_div'));
    console.log(sleep);
    chart.draw(data_table, google.charts.Line.convertOptions(options));
}

function drawExercise(input,title) {
  console.log(input)
  var data_table = new google.visualization.DataTable();
  data_table.addColumn('string', 'Date');
  data_table.addColumn('number', '# of Hours of Exercise');

  const exercise = input.map(subArray => [subArray[0], subArray[3]]);

  data_table.addRows(exercise);

  var options = {
      chart: {
        title: title,
      },
      width: 600,
      height: 350
    };

    var chart = new google.charts.Line(document.getElementById('exercise_div'));

    chart.draw(data_table, google.charts.Line.convertOptions(options));
}