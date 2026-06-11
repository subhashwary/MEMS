
loadPorts();

// ============================================
// CONNECT DMM
// ============================================

function connectDMM() {

    const port =
        document.getElementById('comPortSelect').value;

    fetch('/connect_dmm', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            port: port
        })

    })
    .then(res => res.json())
    .then(data => {

        if (data.status === "connected") {

            alert(
                "DMM Connected:\n" + data.id
            );

        } else {

            alert(
                "Connection Failed:\n" + data.message
            );
        }
    });
}

function updatePSU() {

    fetch('/psu/set', {

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({

            voltage:
                document.getElementById("psVoltage").value,

            current:
                document.getElementById("psCurrent").value
        })

    })
    .then(res => res.json())
    .then(data => {

        console.log(data);

        alert("PSU Updated");

    });
}

function startPSU() {

    const voltage =
        document.getElementById("psVoltage").value;

    const current =
        document.getElementById("psCurrent").value;

    fetch('/psu/start', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            voltage: voltage,
            current: current
        })
    })
    .then(res => res.json())
    .then(data => {

        console.log(data);

        if(data.error){
            alert(data.error);
        }
    });
}

function stopPSU() {

    fetch('/psu/stop', {
        method: 'POST'
    })
    .then(res => res.json())
    .then(data => {

        console.log(data);

        if(data.error){
            alert(data.error);
        }
    });
}

function startAuto(){

    fetch('/mode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mode: 'auto'
        })
    });

    }

    .then(res => res.json())

    .then(data => {

        console.log(data);

        alert("ESS Cycle Started");

    });
}

fetch('/mode', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        mode: 'manual'
    })
});


    .then(res => res.json())

    .then(data => {

        console.log(data);

        alert("ESS Cycle Stopped");

    });
}

setInterval(() => {

    fetch('/status')
    .then(res => res.json())
    .then(data => {

        if (data.mode === "manual") {

            manualBtn.classList.add("active");
            autoBtn.classList.remove("active");

        }
        else {

            autoBtn.classList.add("active");
            manualBtn.classList.remove("active");

        }

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

</script>
