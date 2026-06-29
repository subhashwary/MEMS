const chart = new Chart(ctx, {

    type: 'line',

    data: {
        labels: labels,

        datasets: [

            {
                label: 'DMM Voltage (V)',
                data: dmmData,
                borderColor: 'green',
                borderWidth: 2,
                yAxisID: 'y',
                fill: false,
                tension: 0.2
            },

            {
                label: 'PSU Output',
                data: psuStateData,
                stepped: true,
                borderColor: 'red',
                borderWidth: 2,
                pointRadius: 0,
                yAxisID: 'y1'
            }

        ]
    },
