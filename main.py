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
