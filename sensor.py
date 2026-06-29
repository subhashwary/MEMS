function updateControls(mode) {

    const auto = mode === "auto";

    // DMM
    dmmStartBtn.disabled = auto;
    dmmStopBtn.disabled = auto;

    dmmStartBtn.style.opacity = auto ? 0.5 : 1;
    dmmStopBtn.style.opacity = auto ? 0.5 : 1;

    // PSU
    psuSendBtn.disabled = auto;
    psuOnBtn.disabled = auto;
    psuOffBtn.disabled = auto;

    psuSendBtn.style.opacity = auto ? 0.5 : 1;
    psuOnBtn.style.opacity = auto ? 0.5 : 1;
    psuOffBtn.style.opacity = auto ? 0.5 : 1;

    // Inputs
    voltageInput.disabled = auto;
    currentInput.disabled = auto;
}
