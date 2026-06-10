if (data.mode === "auto") {

    // DMM
    dmmStartBtn.disabled = true;
    dmmStopBtn.disabled = true;

    dmmStartBtn.style.opacity = 0.5;
    dmmStopBtn.style.opacity = 0.5;

    // PSU
    psuSendBtn.disabled = true;
    psuOnBtn.disabled = true;
    psuOffBtn.disabled = true;

    psuSendBtn.style.opacity = 0.5;
    psuOnBtn.style.opacity = 0.5;
    psuOffBtn.style.opacity = 0.5;

    // Inputs
    voltageInput.disabled = true;
    currentInput.disabled = true;

}
else {

    // DMM
    dmmStartBtn.disabled = false;
    dmmStopBtn.disabled = false;

    dmmStartBtn.style.opacity = 1;
    dmmStopBtn.style.opacity = 1;

    // PSU
    psuSendBtn.disabled = false;
    psuOnBtn.disabled = false;
    psuOffBtn.disabled = false;

    psuSendBtn.style.opacity = 1;
    psuOnBtn.style.opacity = 1;
    psuOffBtn.style.opacity = 1;

    // Inputs
    voltageInput.disabled = false;
    currentInput.disabled = false;
}
