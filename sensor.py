let labels = [];
let dmmData = [];
let stateData = [];

let backgroundColors = [];

const ctx = document.getElementById('chart').getContext('2d');


// ===============================
// ESS Background Plugin
// ===============================
const essPlugin = {

    id: "essBackground",

    beforeDraw(chart) {

        const ctx = chart.ctx;

        const xAxis = chart.scales.x;
        const yAxis = chart.scales.y;

        ctx.save();

        for (let i = 0; i < stateData.length - 1; i++) {

            let color = null;

            if (stateData[i].includes("_ON"))
                color = "rgba(0,255,0,0.10)";

            else if (stateData[i].includes("_OFF"))
                color = "rgba(255,0,0,0.10)";

            if (color) {

                const x1 = xAxis.getPixelForValue(i);
                const x2 = xAxis.getPixelForValue(i + 1);

                ctx.fillStyle = color;

                ctx.fillRect(
                    x1,
                    yAxis.top,
                    x2 - x1,
                    yAxis.bottom - yAxis.top
                );
            }
        }

        ctx.restore();
    }
};

Chart.register(essPlugin);

// ===============================

const chart = new Chart(ctx, {
