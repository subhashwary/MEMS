function startAuto(){

    sendCycleConfig()

    .then(() => {

        return fetch('/auto/start', {
            method:'POST'
        });

    })

    .then(res => res.json())

    .then(data => {

        console.log(data);

        alert("ESS Cycle Started");

    });
}
