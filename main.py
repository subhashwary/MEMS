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

    .then(async response => {

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message);
        }

        return data;
    })

    .then(data => {

        alert(
            "PSU Connected\n\n" +
            data.id
        );

    })

    .catch(error => {

        alert(
            "PSU Connection Failed\n\n" +
            error.message
        );

        console.error(error);
    });
}
