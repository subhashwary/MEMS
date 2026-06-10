function stopAuto(){

    fetch('/auto/stop', {

        method:'POST'

    })

    .then(res => res.json())

    .then(data => {

        console.log(data);

        alert("ESS Cycle Stopped");

    });
}
