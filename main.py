autoBtn.onclick = () => {

    sendCycleConfig()

    .then(() => {

        return fetch('/auto/start', {
            method: 'POST'
        });

    })

    .then(() => {

        autoBtn.classList.add("active");
        manualBtn.classList.remove("active");

    });
};
