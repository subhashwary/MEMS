function stopAuto() {

    fetch('/mode', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            mode: 'manual'
        })

    })
    .then(res => res.json())
    .then(data => {

        console.log(data);

        alert("ESS Cycle Stopped");

    });

}
