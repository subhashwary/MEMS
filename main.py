setInterval(() => {

    fetch('/status')

    .then(res => res.json())

    .then(data => {

        document.getElementById("psuStatus")
        .innerText =
            data.psu_connected
            ? "🟢 Connected"
            : "🔴 Disconnected";

        document.getElementById("dmmStatus")
        .innerText =
            data.dmm_connected
            ? "🟢 Connected"
            : "🔴 Disconnected";

        document.getElementById("psuOutputStatus")
        .innerText =
            data.psu_output
            ? "🟢 ON"
            : "🔴 OFF";

        document.getElementById("autoStatus")
        .innerText =
            data.auto_running
            ? "🟢 RUNNING"
            : "🔴 IDLE";

    });

}, 1000);
