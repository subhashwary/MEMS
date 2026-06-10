// Simulated data (replace with API)
setInterval(() => {
    fetch('/data')
        .then(res => res.json())
        .then(data => {

            // PRESSURE
            document.getElementById('pressure').innerText = data.pressure;

            document.getElementById("essState")
            .innerText = data.ess_state;

            document.getElementById("cycleCount")
            .innerText =
                "Cycle " + data.current_cycle;

            // DMM REAL-TIME DISPLAY
            const voltage = parseFloat(data.dmm_voltage || 0);

            document.getElementById('dmmVoltage').innerText =
                voltage.toFixed(3).padStart(6, '0');

            // MODE SYNC (IMPORTANT)
            if (data.mode === "manual") {
                manualBtn.classList.add("active");
                autoBtn.classList.remove("active");
            } else {
                autoBtn.classList.add("active");
                manualBtn.classList.remove("active");
            }

            // STATUS
            let statusEl = document.getElementById('status');
            if (data.pressure < 50) {
                statusEl.innerText = "NORMAL";
                statusEl.className = "status normal";
            } else if (data.pressure < 80) {
                statusEl.innerText = "WARNING";
                statusEl.className = "status warning";
            } else {
                statusEl.innerText = "CRITICAL";
                statusEl.className = "status critical";
            }

            // GRAPH
            dataPoints.push(data.pressure);
            labels.push(new Date().toLocaleTimeString());

            if (dataPoints.length > 50) {
                dataPoints.shift();
                labels.shift();
            }

            if (data.mode === "auto") {
                dmmStartBtn.disabled = true;
                dmmStopBtn.disabled = true;
                dmmStartBtn.style.opacity = 0.5;
                dmmStopBtn.style.opacity = 0.5;
            } else {
                dmmStartBtn.disabled = false;
                dmmStopBtn.disabled = false;
                dmmStartBtn.style.opacity = 1;
                dmmStopBtn.style.opacity = 1;
            }

            chart.update();
        });

}, 1500);

