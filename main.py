<!DOCTYPE html>
<html>
<head>
    <title>MEMS Pressure Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            background: #f4f7fb;
        }
        .header {
            background: #1f2937;
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
        }
        .container {
            padding: 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        button {
            padding: 10px 15px;
            margin-right: 10px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .btn-primary { background: #3b82f6; color: white; }
        .btn-danger { background: #ef4444; color: white; }
        .cycle {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        .cycle.bottom {
            justify-content: center;
        }
        .box {
            background: #e0f2fe;
            padding: 15px 20px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
        }
        .wide-box {
            grid-column: span 2;   /* takes 2 columns width */
        }
        .arrow {
            margin: 0 10px;
            font-size: 20px;
            font-weight: bold;
        }
        .sub-header {
            background: #374151;
            color: #e5e7eb;
            text-align: center;
            padding: 8px;
            font-size: 16px;
            letter-spacing: 1px;
        }
        .ess-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 180px;
            gap: 20px;
        }
        .small-box {
            height: 120px;
            font-size: 14px;
        }
        /* Big left box */
        .large {
            grid-row: span 2;
        }
        /* Right side grid */
        .ess-right {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .ess-box {
            background: #e0f2fe;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-weight: bold;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;   /* move content to top */
            align-items: center;
            padding-top: 15px;             /* control how much up */
        }
        .big-value {
            font-size: 28px;
            margin-top: 10px;
        }
        .label {
            font-size: 14px;
            color: #374151;
        }
        /* Top Banner */
        .top-banner {
            background: #cbd5e1;
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            text-align: center;
        }
        .banner-content h1 {
            margin: 0;
            font-size: 28px;
            font-weight: bold;
        }
        .banner-content h2 {
            margin: 5px 0;
            font-size: 20px;
        }
        .banner-content p {
            margin: 0;
            font-size: 18px;
        }
        /* Title Section */
        .title-section {
            text-align: center;
            margin: 20px 0;
        }
        .title-section h2 {
            margin: 0;
            font-size: 26px;
            font-weight: bold;
        }
        .title-section p {
            margin: 5px 0;
            font-size: 18px;
            color: gray;
        }
        /* MEMS Header */
        .mems-header {
            background: linear-gradient(to right, #1f2937, #334155);
            color: white;
            text-align: center;
            padding: 12px;
            font-size: 22px;
            font-weight: bold;
        }
        .manual-box {
            grid-column: 3;
            height: 80px;
            padding: 18px;
            width: 120px;
            max-width: 180px;
            justify-self: center;   /* center inside grid cell */
            margin: 0 auto;         /* extra safety centering */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        /* ESS Line */
        .ess-line {
            background: #e5e7eb;
            text-align: center;
            padding: 12px;
            font-size: 18px;
            margin: 10px;
            border-radius: 8px;
            letter-spacing: 1px;
        }
        .header {
            background: linear-gradient(to right, #1f2937, #334155);
            color: white;
            text-align: center;
            padding: 12px;
            font-size: 22px;
            font-weight: bold;
            margin: 10px;
            border-radius: 8px;
        }
.top-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #cbd5e1;
    padding: 15px 20px;
    border-radius: 10px;
    margin: 10px;
    gap: 20px;
}
.banner-text {
    flex: 1;
    text-align: center;
}
.logo {
    flex-shrink: 0;
}
.top-label-box {
    text-align: center;
    font-size: 14px;        /* bigger text */
    font-weight: bold;
    color: white;
    background: #3b82f6;
    border-radius: 8px;
    padding: 6px 14px;      /* bigger box */
    min-width: 70px;        /* consistent width */
    margin: 0 auto -10px auto; /* center + closer to box */
}
/* Center Text */
.banner-text {
    text-align: center;
    flex: 1;
}
.banner-text h1 {
    margin: 0;
    font-size: 30px;   /* Centre for Nano Science and Engineering */
    font-weight: bold;
}
.banner-text h2 {
    margin: 5px 0;
    font-size: 24px;   /* Indian Institute of Science */
    font-weight: 600;
}
.banner-text p {
    margin: 0;
    font-size: 20px;   /* Bangalore, 560012 */
    font-weight: 500;
}
#chart {
    height: 350px !important;
}
/* Logos */
.logo img {
    width: 100px;   /* try 80–120px */
    height: auto;
}
/* Left & Right spacing */
.logo.left {
    margin-right: 10px;
}
.logo.right {
    margin-left: 10px;
}
.mode-row {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    margin: 3px 0;
}
.mode-btn {
    width: 30px;
    height: 30px;
    margin-right: 8px;
    border: none;
    border-radius: 6px;
    color: white;
    font-weight: bold;
    cursor: pointer;
}
.mode-btn {
    width: 30px;
    height: 30px;
    margin-right: 8px;
    border: none;
    border-radius: 6px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    background: #ef4444; /* default = OFF (red) */
}
.control-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
    margin-top: 10px;
}
.control-btn {
    padding: 6px 10px;
    font-size: 12px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    color: white;
    background: #3b82f6;
}
.control-btn:hover {
    background: #2563eb;
}
/* ON state */
.active {
    background: #10b981 !important; /* green */
    outline: 3px solid #1f2937;
}
.active-manual {
    outline: 3px solid #1f2937;
    background: #10b981 !important; /* green */
}
.active-auto {
    outline: 3px solid #1f2937;
    background: #ef4444 !important; /* red */
}
.instrument-box {
    width: 100%;
    min-height: 420px;
    display: flex;
    flex-direction: column;
    align-items: center;

    padding: 25px;
    box-sizing: border-box;
}
.psu-box {
    grid-column: 1;
}
.dmm-box {
    grid-column: 2;
    width:100%;
    max-width: none;
}
.ps-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;  /* 2 buttons per row */
    gap: 8px;
    margin-top: 15px;
    width: 50%;
    justify-items: center;
}
.ps-control {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 15px;
    width: 100%;
}
.ps-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}
.ps-row input {
    width: 100px;
    padding: 5px;
    border-radius: 6px;
    border: 1px solid #ccc;
    text-align: center;
}
.ps-row-top {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 10px;
}
.ps-item input {
    width: 120px;
    padding: 5px;
    text-align: center;
    border-radius: 6px;
    border: 1px solid #ccc;
}
.ps-row-units {
    display: flex;
    justify-content: center;
    gap: 110px;   /* aligns V and A under inputs */
    margin-top: 5px;
    font-weight: bold;
    color: #374151;
}
.ps-row-bottom {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 15px;
}
.start-btn {
    background: #10b981;
    color: white;
    width: 100px;
}
.stop-btn {
    background: #ef4444;
    color: white;
    width: 100px;
}
.ps-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
}
.dmm-title {
    font-size: 20px;        /* bigger text */
    font-weight: bold;
    margin-top: -10px;      /* move upward */
    margin-bottom: 30px;
    color: #111827;
    letter-spacing: 0.5px;
}
.dmm-row {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    margin-top: 10px;
}
.dmm-row input {
    width: 120px;
    padding: 5px;
    text-align: center;
    border-radius: 6px;
    border: 1px solid #ccc;
}
.unit-label {
    font-size: 14px;
    font-weight: bold;
    color: #374151;
}
.dmm-bottom {
    display: flex;
    gap: 15px;
    margin-top: 15px;
}
.instrument-label {
    font-size: 14px;
    color: #374151;
    font-weight: bold;
}
.instrument-inline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 10px;
}
.inline-group {
    display: flex;
    align-items: center;
    gap: 8px;
}
.inline-group input {
    width: 80px;
    padding: 6px;
    text-align: center;
    border-radius: 6px;
    border: 1px solid #ccc;
}
.channel-row {
    display: flex;
    justify-content: space-between;
    width: 80%;
    margin-bottom: 10px;
    font-weight: bold;
    color: #1f2937;
}
.instrument-inline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 5px;
}
.inline-group {
    display: flex;
    align-items: center;
    gap: 8px;
}
.inline-group input {
    width: 80px;
    padding: 6px;
    text-align: center;
    border-radius: 6px;
    border: 1px solid #ccc;
}
.ps-grid-clean {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px 20px;
    width: 90%;
    margin-top: 5px;
    text-align: center;
}
.ps-head {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
    text-align: center;
}
.ps-label {
    font-size: 14px;
    color: #374151;
    font-weight: 600;
}
.ps-input {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
}
.ps-input input {
    width: 80px;
    padding: 6px;
    text-align: center;
    border-radius: 6px;
    border: 1px solid #ccc;
}
.instrument-row input {
    width: 100px;
    height: 32px;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 6px;
}
.psu-row {
    display: grid;
    grid-template-columns: 140px 100px 60px;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin: 10px 0;
}
.status-box .card {
    width: 100%;
}
.ess-status-box .card {
    width: 100%;
}
.psu-row input {
    width: 100px;
    height: 32px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 6px;
}
.instrument-row {
    display: grid;
    grid-template-columns: 140px 280px 60px;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin: 10px 0;
}
.dmm-display {
    width: 280px;
    height: 70px;
    background: black;
    color: #00ff66;
    font-size: 42px;
    font-family: "Courier New", monospace;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    border: 3px solid #1f2937;
    letter-spacing: 2px;
    box-shadow:
        inset 0 0 10px rgba(0,255,100,0.3),
        0 0 8px rgba(0,255,100,0.2);
}
.ess-idle {
    color: gray;
    font-weight: bold;
}
.ess-delay {
    color: blue;
    font-weight: bold;
}
.ess-on {
    color: green;
    font-weight: bold;
}
.ess-off {
    color: orange;
    font-weight: bold;
}
.ess-complete {
    color: darkgreen;
    font-weight: bold;
}
.ess-stop {
    color: red;
    font-weight: bold;
}
.status-box {
    min-height: 420px;
    justify-content: flex-start;
    align-items: flex-start;
    text-align: left;
}
.ess-status-box {
    min-height: 420px;

    align-items: stretch;

    text-align: left;
}
    </style>
</head>
<body>
    <!-- Top Banner -->
<div class="top-banner">
    <div class="logo left">
        <img src="/static/images/cense.png" alt="CeNSE">
    </div>
    <div class="banner-text">
        <h1>Centre for Nano Science and Engineering</h1>
        <h2>Indian Institute of Science</h2>
        <p>Bangalore, 560012</p>
    </div>
    <div class="logo right">
        <img src="/static/images/IISc.png" alt="IISc">
    </div>
</div>
<!-- MEMS Header -->
<div class="mems-header">
    MEMS Pressure Transducer
</div>
<div class="mems-header">
    Environmental Stress Screening (ESS) Cycle Test
</div>
<div class="card">
    <div class="ess-grid">
<div class="ess-box instrument-box psu-box">
    <div class="ps-title">DC Power Supply</div>
<div style="margin-bottom:15px;">
    <select id="psuPortSelect"
        style="
        padding:8px;
        border-radius:6px;
        width:140px;
    ">
        <option>Loading...</option>
    </select>
    <button onclick="connectPSU()" class="control-btn">
        Connect
    </button>
</div>
    <div class="ps-head" style="margin-bottom:20px;">
        CH1
    </div>
    <div class="psu-row">
        <span class="instrument-label">Set Voltage</span>
        <input
            id="psVoltage"
            type="number"
            step="0.01"
            value="2.00">
        <span>Volt</span>
    </div>
    <div class="psu-row">
        <span class="instrument-label">Set Current</span>
        <input
            id="psCurrent"
            type="number"
            step="0.01"
            value="0.20">
        <span>Amp</span>
    </div>
<div class="ps-row-bottom">
    <button
        class="control-btn"
        onclick="updatePSU()">
        Send To PSU
    </button>
</div>
<div class="ess-box instrument-box ess-status-box"
     style="grid-column:2;">

<div class="ps-row-bottom">
    <button
        class="control-btn start-btn"
        onclick="startPSU()">
        ON
    </button>
    <button
        class="control-btn stop-btn"
        onclick="stopPSU()">
        OFF
    </button>
</div>
</div>
<div class="ess-box instrument-box dmm-box">
    <div class="dmm-title">Digital Multimeter</div>
<div style="margin-bottom:15px;">
    <select id="comPortSelect" style="
        padding:8px;
        border-radius:6px;
        width:140px;
    ">
        <option>Loading...</option>
    </select>
    <button onclick="connectDMM()" class="control-btn">
        Connect
    </button>
</div>
    <div class="instrument-row">
        <span class="instrument-label">Voltage</span>
        <div id="dmmVoltage" class="dmm-display">
            000.0000
        </div>
        <span>VDC</span>
    </div>
    <div class="ps-row-bottom">
        <button class="control-btn start-btn" onclick="startDMM()">Start</button>
        <button class="control-btn stop-btn" onclick="stopDMM()">Stop</button>
    </div>
</div>
        <!-- NEW SMALL BOX -->
<div class="ess-box small-box manual-box">
    <div class="mode-row">
        <button class="mode-btn" id="manualBtn"></button>
        <span class="label">Manual</span>
    </div>
    <div class="mode-row">
        <button class="mode-btn" id="autoBtn"></button>
        <span class="label">Auto</span>
    </div>
</div>
<!-- ROW 3 -->
<div class="ess-box instrument-box status-box" 
    style="grid-column: 1;">
    <div class="card">
    <h3>System Status</h3>
    <div>
        PSU Connection:
        <span id="psuStatus">🔴</span>
    </div>
    <br>
    <div>
        DMM Connection:
        <span id="dmmStatus">🔴</span>
    </div>
    <br>
    <div>
        PSU Output:
        <span id="psuOutputStatus">🔴</span>
    </div>
    <br>
    <div>
        Auto Mode:
        <span id="autoStatus">🔴</span>
    </div>
</div>
    <h3>ESS Status</h3>
    <div id="essState">
        IDLE
    </div>
    <br>
    <div id="cycleCount">
        Cycle 0
    </div>
</div>
<div class="card">
    <h3>Current Event</h3>
    <div id="cycleEvent">
        Waiting...
    </div>
    <div style="font-size:20px;font-weight:bold;margin-bottom:10px;">
        Time Delay
    </div>
    <div class="instrument-row">
        <span class="instrument-label">Initial Delay</span>
        <input id="initialDelay" type="number" value="10">
        <span>Initial OFF</span>
    </div>
    <div class="instrument-row">
        <span class="instrument-label">ON Time</span>
        <input id="onTime" type="number" value="5">
        <span>ON Time</span>
    </div>
    <div class="instrument-row">
        <span class="instrument-label">OFF Time</span>
<input id="offTime" type="number" value="3">
        <span>OFF Time</span>
    </div>
    <div class="instrument-row">
        <span class="instrument-label">No. of Cycles</span>
<input id="cycleCountInput" type="number" value="4">
        <span>No. of Cycles</span>
    </div>
</div>
    </div>
</div>
<div class="container">
        <div class="card">
        <canvas id="chart"></canvas>
    </div>
    <div class="card">
</div>
<br>
    <!-- Controls -->
    <div class="card">
        <button class="btn-primary" onclick="resetData()">Reset</button>
        <button class="btn-danger" onclick="downloadCSV()">Download CSV</button>
    </div>
</div>
<script>
let dataPoints = [];
let labels = [];
const ctx = document.getElementById('chart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Pressure (kPa)',
            data: dataPoints,
            borderWidth: 2,
            fill: false
        }]
    }
});
// Simulated data (replace with API)
setInterval(() => {
    fetch('/data')
        .then(res => res.json())
        .then(data => {
            // PRESSURE
            // document.getElementById('pressure').innerText = data.pressure;
            document.getElementById("essState")
            .innerText = data.ess_state;
            const essEl =
                document.getElementById("essState");
            essEl.className = "";
            if(data.ess_state === "INITIAL_DELAY")
            {
                essEl.classList.add("ess-delay");
            }
            else if(data.ess_state.includes("_ON"))
            {
                essEl.classList.add("ess-on");
            }
            else if(data.ess_state.includes("_OFF"))
            {
                essEl.classList.add("ess-off");
            }
            else if(data.ess_state === "COMPLETE")
            {
                essEl.classList.add("ess-complete");
            }
            else if(data.ess_state === "STOPPED")
            {
                essEl.classList.add("ess-stop");
            }
            else
            {
                essEl.classList.add("ess-idle");
            }
            document.getElementById("cycleCount")
            .innerText =
                "Cycle " + data.current_cycle;
            document.getElementById("cycleEvent")
            .innerText =
                data.cycle_event;
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
            // GRAPH
            dataPoints.push(data.pressure);
            labels.push(new Date().toLocaleTimeString());

            if (dataPoints.length > 50) {
                dataPoints.shift();
                labels.shift();
            }
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
            chart.update();
        });
}, 1500);
// Reset
function resetData() {
    dataPoints = [];
    labels = [];
    chart.data.labels = labels;
    chart.data.datasets[0].data = dataPoints;
    chart.update();
}
function connectPSU() {
    const port =
        document.getElementById("psuPortSelect").value;
    fetch('/connect_psu', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            port: port
        })
    })
    .then(async response => {
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.message);
        }
        return data;
    })
    .then(data => {
        alert(
            "PSU Connected\n\n" +
            data.id
        );
    })
    .catch(error => {
        alert(
            "PSU Connection Failed\n\n" +
            error.message
        );
        console.error(error);
    });
}
// Download CSV
function downloadCSV() {
    window.location.href = "/download";
}
const manualBtn = document.getElementById("manualBtn");
const autoBtn = document.getElementById("autoBtn");
const dmmStartBtn = document.querySelector(".dmm-box .start-btn");
const dmmStopBtn = document.querySelector(".dmm-box .stop-btn");
const psuSendBtn =
    document.querySelector('.psu-box .control-btn');
const psuOnBtn =
    document.querySelector('.psu-box .start-btn');
const psuOffBtn =
    document.querySelector('.psu-box .stop-btn');
const voltageInput =
    document.getElementById("psVoltage");
const currentInput =
    document.getElementById("psCurrent");
// default state (optional)
manualBtn.classList.add("active"); // Manual ON
manualBtn.onclick = () => {
    fetch('/mode', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({
            mode:'manual'
        })
    });
    manualBtn.classList.add("active");
    autoBtn.classList.remove("active");
};
autoBtn.onclick = () => {
    sendCycleConfig()
    .then(() => {
        fetch('/mode', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                mode:'auto'
            })
        });
    })
    .then(() => {
        autoBtn.classList.add("active");
        manualBtn.classList.remove("active");
    });
};
let voltOn = false;
let ampOn = false;
function startDMM() {
    fetch('/dmm/start', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        if (data.error) alert(data.error);
    });
}
function stopDMM() {
    fetch('/dmm/stop', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        if (data.error) alert(data.error);
    });
}
function sendCycleConfig() {
    const config = {
        initial_off:
            document.getElementById(
                "initialDelay"
            ).value,
        on_time:
            document.getElementById(
                "onTime"
            ).value,
        off_time:
            document.getElementById(
                "offTime"
            ).value,
        cycles:
            document.getElementById(
                "cycleCountInput"
            ).value
    };
    return fetch('/config', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(config)
    });
}
function loadPorts() {
    fetch('/ports')
    .then(res => res.json())
    .then(ports => {
        const dmmSelect =
            document.getElementById('comPortSelect');
        const psuSelect =
            document.getElementById('psuPortSelect');
        dmmSelect.innerHTML = '';
        psuSelect.innerHTML = '';
        ports.forEach(port => {
            const option1 =
                document.createElement('option');
            option1.value = port.device;
            option1.text =
                `${port.device} - ${port.description}`;
            dmmSelect.appendChild(option1);
            const option2 =
                document.createElement('option');
            option2.value = port.device;
            option2.text =
                `${port.device} - ${port.description}`;
            psuSelect.appendChild(option2);
        });
    });
}
loadPorts();
function connectDMM() {
    const port =
        document.getElementById('comPortSelect').value;
    fetch('/connect_dmm', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            port: port
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "connected") {
            alert(
                "DMM Connected:\n" + data.id
            );
        } else {
            alert(
                "Connection Failed:\n" + data.message
            );
        }
    });
}
function updatePSU() {
    fetch('/psu/set', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            voltage:
                document.getElementById("psVoltage").value,
            current:
                document.getElementById("psCurrent").value
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        alert("PSU Updated");
    });
}
function startPSU() {
    const voltage =
        document.getElementById("psVoltage").value;
    const current =
        document.getElementById("psCurrent").value;
    fetch('/psu/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            voltage: voltage,
            current: current
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        if(data.error){
            alert(data.error);
        }
    });
}
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
function startAuto() {
    fetch('/mode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mode: 'auto'
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        alert("ESS Cycle Started");
    });
}
function stopAuto() {
    fetch('/mode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mode: 'manual'
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        alert("ESS Cycle Stopped");
    });
}
setInterval(() => {
    fetch('/status')
    .then(res => res.json())
    .then(data => {
        if (data.mode === "manual") {
            manualBtn.classList.add("active");
            autoBtn.classList.remove("active");
        }
        else {
            autoBtn.classList.add("active");
            manualBtn.classList.remove("active");
        }
        document.getElementById("psuStatus")
        .innerText =
            data.psu_connected
            ? "🟢 Connected"
            : "🔴 Disconnected";
        document.getElementById("dmmStatus")
        .innerText =
            data.dmm_connected
            ? "🟢 Connected"
            : "🔴 Disconnected";
        document.getElementById("psuOutputStatus")
        .innerText =
            data.psu_output
            ? "🟢 ON"
            : "🔴 OFF";
        document.getElementById("autoStatus")
        .innerText =
            data.auto_running
            ? "🟢 RUNNING"
            : "🔴 IDLE";
    });
}, 1000);
</script>
</body>
</html>
