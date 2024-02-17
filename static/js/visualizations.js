$(document).ready(function() {
    fetch('/graph_data')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            construct_graph_bar(data.bar_graph);
            construct_line_graph(data.line_graph);
            construct_radar_graph(data.radar_graph);
        })
        .catch(error => console.error(error));

    
})

function construct_graph_bar(data) {
    // Create Chart.js chart
    const counts = data

      
      const ctx = document.getElementById("bar_graph").getContext("2d");
      const chart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Popular", "Not Popular"],
          datasets: [
            {
              label: "Count",
              data: [data.true, data.false],
              backgroundColor: ["#5bc0de", "#d9534f"],
              borderColor: ["#5bc0de", "#d9534f"],
              borderWidth: 1
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: "Count of Popular and Unpopular songs",
            fontSize: 18,
            fontColor: "#333"
          },
          legend: {
            display: false
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  fontColor: "#333"
                },
                gridLines: {
                  color: "#eee",
                  zeroLineColor: "#eee",
                  display: true
                }
              }
            ],
            xAxes: [
              {
                barPercentage: 0.5, // Set the bar width to 50% of the available space
                ticks: {
                  fontColor: "#333"
                },
                gridLines: {
                  display: false
                }
              }
            ]
          }
        }
      });
      


    // Render the chart on the canvas
    chart.update();
}

function construct_line_graph(data) {

    // Define options for the chart
    const options = {
    scales: {
        yAxes: [{
        ticks: {
            beginAtZero: true
        }
        }]
    }
    };

    // Create a chart instance
    const ctx = document.getElementById('line_graph').getContext('2d');
    const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Object.keys(data.total),
        datasets: [{
        label: 'Total',
        data: Object.values(data.total),
        borderColor: 'red'
        }, {
        label: 'Explicit',
        data: Object.values(data.explicit),
        borderColor: 'green'
        }, {
        label: 'Non-Explicit',
        data: Object.values(data.non_explicit),
        borderColor: 'blue'
        }]
    },
    options: options
    });
}


function construct_radar_graph(data) {

    labels = data.labels
    data1 = data.features
    data2 = data.features_all
    
    data = {
        labels: labels,
        datasets: [{
                label: 'Data 1',
                data: data1,
                fill: true,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)',
                pointBackgroundColor: 'rgb(255, 99, 132)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(255, 99, 132)'
            }, {
                label: 'Data 2',
                data: data2,
                fill: true,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)',
                pointBackgroundColor: 'rgb(54, 162, 235)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(54, 162, 235)'
            }
        ]
    }

    const config = {
        type: 'radar',
        data: data,
        options: {
            elements: {
                line: {
                    borderWidth: 2
                }
            }
        },
    };

    const ctx = document.getElementById('radar_graph').getContext('2d');

    const chart = new Chart(ctx, config);
    
    chart.update();

}

