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
