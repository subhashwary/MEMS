const eventLabelPlugin = {

    id: "eventLabels",

    afterDatasetsDraw(chart) {

        const ctx = chart.ctx;

        const meta = chart.getDatasetMeta(0);

        ctx.save();

        ctx.fillStyle = "black";
        ctx.font = "11px Arial";

        meta.data.forEach((point, index) => {

            if(eventLabels[index] !== ""){

                ctx.save();

                ctx.translate(point.x, point.y - 10);

                ctx.rotate(-Math.PI/4);

                ctx.fillText(eventLabels[index],0,0);

                ctx.restore();

            }

        });

        ctx.restore();

    }

};

Chart.register(eventLabelPlugin);
