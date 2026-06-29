manualBtn.classList.toggle("active", data.mode === "manual");
autoBtn.classList.toggle("active", data.mode === "auto");

updateControls(data.mode);
