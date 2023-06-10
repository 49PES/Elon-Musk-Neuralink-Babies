function init(){
    
    // Sample dates and corresponding amount of sleep, exercise, and calorie consumption
    const dates = ['06/08/2023', '06/10/2023'];
    const minutesSpentExercising = [120, 90];
    const minutesSpentSleeping = [500, 630];
    const calories = [1980, 1760];


             
    const calorieData = {
        labels: dates,
        datasets: [
            {
            label: 'Calories Consumed',
            data: calories,
            backgroundColor: 'rgba(192, 75, 192, 0.2)', 
            borderColor: 'rgba(192, 75, 192, 1)', 
            borderWidth: 1, 
            },
        ],
        };
    
        
    const ctxCalories = document.getElementById('calories').getContext('2d');
    new Chart(ctxCalories, {
    type: 'bar',
    data: calorieData,
    options: {
        scales: {
        y: {
            beginAtZero: true, 
        },
        },
    },
    });



    const sleepData = {
        labels: dates,
        datasets: [
            {
            label: 'Minutes Spent Sleeping',
            data: minutesSpentSleeping,
            backgroundColor: 'rgba(192, 192, 75, 0.2)', 
            borderColor: 'rgba(192, 192, 75, 1)', 
            borderWidth: 1, 
            },
        ],
        };
    
        
    const ctxSleep = document.getElementById('sleep').getContext('2d');
    new Chart(ctxSleep, {
    type: 'bar',
    data: sleepData,
    options: {
        scales: {
        y: {
            beginAtZero: true, 
        },
        },
    },
    });
   
    const exerciseData = {
        labels: dates,
        datasets: [
            {
            label: 'Minutes Spent Exercising',
            data: minutesSpentExercising,
            backgroundColor: 'rgba(75, 192, 192, 0.2)', 
            borderColor: 'rgba(75, 192, 192, 1)', 
            borderWidth: 1, 
            },
        ],
        };
    
        
    const ctxExercise = document.getElementById('exercise').getContext('2d');
    new Chart(ctxExercise, {
    type: 'bar',
    data: exerciseData,
    options: {
        scales: {
        y: {
            beginAtZero: true, 
        },
        },
    },
    });
    
}