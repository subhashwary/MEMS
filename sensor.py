// GRAPH ONLY DURING AUTO MODE

if (data.mode === "auto") {

    labels.push(data.timestamp);
    dmmData.push(data.dmm_voltage);
    stateData.push(data.ess_state);

    if (data.ess_state !== previousState) {

        if (data.ess_state.includes("_ON")) {

            eventMarkers.push({
                index: labels.length - 1,
                title: `C${data.current_cycle} ON`,
                time: data.timestamp
            });

        }
        else if (data.ess_state.includes("_OFF")) {

            eventMarkers.push({
                index: labels.length - 1,
                title: `C${data.current_cycle} OFF`,
                time: data.timestamp
            });

        }

        previousState = data.ess_state;
    }

    if (
        stateData.length < 2 ||
        stateData[stateData.length - 1] !== stateData[stateData.length - 2]
    ) {
        eventLabels.push(data.timestamp);
    } else {
        eventLabels.push("");
    }

    if(labels.length > 300) {
        labels.shift();
        dmmData.shift();
        stateData.shift();
        eventLabels.shift();
    }

    chart.update();
}
