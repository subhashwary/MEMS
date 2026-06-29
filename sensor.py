y: {
    title: {
        display: true,
        text: 'Voltage (V)'
    },
    min: 0,
    max: 3
},

y1: {
    position: 'right',
    min: 0,
    max: 1,

    ticks: {
        callback: value => value ? "ON" : "OFF"
    },

    grid: {
        drawOnChartArea: false
    }
}
