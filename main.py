let labels = [];

let pressureData = [];
let dmmData = [];
let psuVoltageData = [];
let psuCurrentData = [];

let essData = [];
let modeData = [];
let cycleData = [];

const chart = new Chart(ctx, {
    type: 'line',

    data: {
        labels: labels,

        datasets: [

            {
                label: 'Pressure (kPa)',
                data: pressureData,
                borderWidth: 2,
                yAxisID: 'y'
            },

            {
                label: 'DMM Voltage (V)',
                data: dmmData,
                borderWidth: 2,
                yAxisID: 'y'
            },

            {
                label: 'PSU Voltage (V)',
                data: psuVoltageData,
                borderWidth: 2,
                yAxisID: 'y'
            },

            {
                label: 'PSU Current (A)',
                data: psuCurrentData,
                borderWidth: 2,
                yAxisID: 'y1'
            },

            {
                label: 'ESS State',
                data: essData,
                stepped: true,
                borderWidth: 3,
                yAxisID: 'y2'
            },

            {
                label: 'Mode',
                data: modeData,
                stepped: true,
                borderWidth: 3,
                yAxisID: 'y2'
            },

            {
                label: 'Cycle',
                data: cycleData,
                borderWidth: 2,
                yAxisID: 'y3'
            }
        ]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {

            y: {
                type: 'linear',
                position: 'left',
                title: {
                    display: true,
                    text: 'Voltage / Pressure'
                }
            },

            y1: {
                type: 'linear',
                position: 'right',
                title: {
                    display: true,
                    text: 'Current (A)'
                },

                grid: {
                    drawOnChartArea: false
                }
            },

            y2: {
                min: 0,
                max: 2,

                position: 'right',

                title: {
                    display: true,
                    text: 'State'
                },

                grid: {
                    drawOnChartArea: false
                }
            },

            y3: {
                position: 'right',

                title: {
                    display: true,
                    text: 'Cycle'
                },

                grid: {
                    drawOnChartArea: false
                }
            }
        }
    }
});
