setInterval(() => {

    fetch('/status')

    .then(res => res.json())

    .then(data => {

        document.getElementById("psuStatus")
        .innerText =
            data.psu_connected ? "🟢" : "🔴";

        document.getElementById("dmmStatus")
        .innerText =
            data.dmm_connected ? "🟢" : "🔴";
    });

},1000);
