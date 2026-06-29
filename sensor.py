const eventPlugin = {

    id: "eventPlugin",

    afterDatasetsDraw(chart) {

        const ctx = chart.ctx;
        const meta = chart.getDatasetMeta(0);

        ctx.save();

        ctx.font = "12px Arial";
        ctx.textAlign = "center";

        eventMarkers.forEach(marker => {

            const point = meta.data[marker.index];

            if (!point) return;

            const x = point.x;
            const y = point.y;

            // vertical guide line
            ctx.beginPath();
            ctx.strokeStyle = "#666";
            ctx.setLineDash([4,4]);
            ctx.moveTo(x, chart.scales.y.top);
            ctx.lineTo(x, y);
            ctx.stroke();

            ctx.setLineDash([]);

            // title
            ctx.fillStyle = "blue";
            ctx.fillText(marker.title, x, chart.scales.y.top + 15);

            // timestamp
            ctx.fillStyle = "black";
            ctx.fillText(marker.time, x, chart.scales.y.top + 30);

        });

        ctx.restore();

    }

};

Chart.register(eventPlugin);
