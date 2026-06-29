if (data.ess_state !== previousState) {

    if (data.ess_state.includes("_ON")) {

        eventMarkers.push({
            index: labels.length - 1,
            title: `Cycle ${data.current_cycle} ON`,
            time: data.timestamp
        });

    }
    else if (data.ess_state.includes("_OFF")) {

        eventMarkers.push({
            index: labels.length - 1,
            title: `Cycle ${data.current_cycle} OFF`,
            time: data.timestamp
        });

    }

    previousState = data.ess_state;
}
