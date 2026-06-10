manualBtn.onclick = () => {

    fetch('/auto/stop', {
        method: 'POST'
    });

    manualBtn.classList.add("active");
    autoBtn.classList.remove("active");
};
