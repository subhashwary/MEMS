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

                ctx.fillStyle = color;

                const x1 = xAxis.getPixelForValue(i);

                const x2 = xAxis.getPixelForValue(i + 1);

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
