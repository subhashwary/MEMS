function updatePSU() {

    fetch('/psu/set', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            voltage:
                document.getElementById("psVoltage").value,

            current:
                document.getElementById("psCurrent").value
        })
    });
}
