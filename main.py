function sendCycleConfig() {

    const config = {

        initial_off:
            document.getElementById(
                "initialDelay"
            ).value,

        on_time:
            document.getElementById(
                "onTime"
            ).value,

        off_time:
            document.getElementById(
                "offTime"
            ).value,

        cycles:
            document.getElementById(
                "cycleCountInput"
            ).value
    };

    return fetch('/config', {

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify(config)
    });
}
