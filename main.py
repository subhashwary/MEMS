function connectPSU() {

    const port =
        document.getElementById("psuPortSelect").value;

    fetch('/connect_psu', {

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

        if(data.status === "connected") {

            alert(
                "PSU Connected\n\n" +
                data.id
            );

        } else {

            alert(
                "Connection Failed\n\n" +
                data.message
            );
        }
    });
}
