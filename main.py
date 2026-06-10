if (data.mode === "auto") {

    psuSendBtn.disabled = true;
    psuOnBtn.disabled = true;
    psuOffBtn.disabled = true;

    psuSendBtn.style.opacity = 0.5;
    psuOnBtn.style.opacity = 0.5;
    psuOffBtn.style.opacity = 0.5;

}
else {

    psuSendBtn.disabled = false;
    psuOnBtn.disabled = false;
    psuOffBtn.disabled = false;

    psuSendBtn.style.opacity = 1;
    psuOnBtn.style.opacity = 1;
    psuOffBtn.style.opacity = 1;
}
