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

        .value {
            font-size: 40px;
            font-weight: bold;
        }

        .unit {
            font-size: 18px;
            color: gray;
        }

        .status {
            padding: 8px 16px;
            border-radius: 20px;
            display: inline-block;
            color: white;
            font-weight: bold;
        }

        .normal { background: #10b981; }
        .warning { background: #f59e0b; }
        .critical { background: #ef4444; }

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
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            justify-content: space-between;
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
    width: 80%;   /* instead of 480px */
    max-width: 480px;
    height: 200px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;
    padding: 25px;
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
    font-size: 20px;        /* bigger text */
    font-weight: bold;
    margin-top: -10px;      /* moves it upward */
    margin-bottom: 30px;    /* spacing below */
    color: #111827;
}

.dmm-title {
    font-size: 20px;        /* bigger text */
    font-weight: bold;
    margin-top: -10px;      /* move upward */
    margin-bottom: 30px;
    color: #111827;
    letter-spacing: 0.5px;
}

.dmm-title {
    font-size: 20px;
    font-weight: bold;
    margin-top: -10px;
    margin-bottom: 30px;
    color: #111827;
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

.ess-box.instrument-box:nth-child(2) {
    margin-top: -20px;   /* moves DMM upward */
}

.instrument-row {
    display: grid;
    grid-template-columns: 140px 1fr 140px;
    align-items: center;
    gap: 10px;
    width: 100%;
    margin: 6px 0;
}

.instrument-row input {
    width: 100%;
    padding: 6px;
    border-radius: 6px;
    border: 1px solid #ccc;
    text-align: center;
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
    font-weight: bold;
    font-size: 16px;
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

.dmm-display {
    width: 180px;
    height: 55px;

    background: black;
    color: #00ff66;

    font-size: 32px;
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

            <!-- TOP LABELS -->
            <div class="top-label-box">COM6</div>
            <div></div>
            <div class="top-label-box">COM5</div>

<div class="ess-box instrument-box">

    <div class="ps-title">DC Power Supply</div>

    <!-- CHANNEL LABELS -->
<div class="ps-grid-clean">

    <!-- Row 1 -->
    <div class="ps-head">CH1</div>
    <div class="ps-head">CH2</div>

    <!-- Row 2 -->
    <div class="ps-label">Voltage</div>
    <div class="ps-label">Current</div>

    <!-- Row 3 -->
    <div class="ps-input">
        <input type="number">
        <span>Volt</span>
    </div>

    <div class="ps-input">
        <input type="number">
        <span>Amp</span>
    </div>

</div>

    <div class="ps-row-bottom">
        <button class="control-btn start-btn">Start</button>
        <button class="control-btn stop-btn">Stop</button>
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

<div class="ess-box instrument-box" style="grid-column: 2;">
    <div style="font-size:20px;font-weight:bold;margin-bottom:10px;">
        Time Delay
    </div>

    <div class="instrument-row">
        <span class="instrument-label">Voltage 1</span>
        <input type="number" placeholder="000">
        <span>Initial OFF</span>
    </div>

    <div class="instrument-row">
        <span class="instrument-label">Voltage 2</span>
        <input type="number" placeholder="000">
        <span>ON Time</span>
    </div>

    <div class="instrument-row">
        <span class="instrument-label">Voltage 3</span>
        <input type="number" placeholder="000">
        <span>OFF Time</span>
    </div>

    <div class="instrument-row">
        <span class="instrument-label">Voltage 4</span>
        <input type="number" placeholder="000">
        <span>No. of Cycles</span>
    </div>
</div>

        <!-- Empty placeholder (keeps grid aligned) -->
        <div></div>

    </div>
</div>

<div class="container">

    <!-- Live Value -->
    <div class="card">
        <div>Current Pressure</div>
        <div class="value" id="pressure">0</div>
        <div class="unit">kPa</div>
        <br>
        <div id="status" class="status normal">NORMAL</div>
    </div>

    <!-- Chart -->
    <div class="card">
        <canvas id="chart"></canvas>
    </div>

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
            document.getElementById('pressure').innerText = data.pressure;

            // DMM REAL-TIME DISPLAY
            const voltage = parseFloat(data.dmm_voltage || 0);

            document.getElementById('dmmVoltage').innerText =
                voltage.toFixed(6);


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

// Reset
function resetData() {
    dataPoints = [];
    labels = [];
    chart.data.labels = labels;
    chart.data.datasets[0].data = dataPoints;
    chart.update();
}

// Download CSV
function downloadCSV() {
    window.location.href = "/download";
}

const manualBtn = document.getElementById("manualBtn");
const autoBtn = document.getElementById("autoBtn");

const dmmStartBtn = document.querySelector(".dmm-box .start-btn");
const dmmStopBtn = document.querySelector(".dmm-box .stop-btn");

// default state (optional)
manualBtn.classList.add("active"); // Manual ON

manualBtn.onclick = () => {
    fetch('/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: "manual" })
    });

    manualBtn.classList.add("active");
    autoBtn.classList.remove("active");
};

autoBtn.onclick = () => {
    fetch('/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: "auto" })
    });

    autoBtn.classList.add("active");
    manualBtn.classList.remove("active");
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
        t1: document.querySelectorAll("input")[2].value,
        t2: document.querySelectorAll("input")[3].value,
        t3: document.querySelectorAll("input")[4].value,
        cycles: document.querySelectorAll("input")[5].value
    };

    fetch('/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(config)
    });
}

// ============================================
// LOAD AVAILABLE COM PORTS
// ============================================

function loadPorts() {

    fetch('/ports')
    .then(res => res.json())
    .then(ports => {

        const select = document.getElementById('comPortSelect');

        select.innerHTML = '';

        ports.forEach(port => {

            const option = document.createElement('option');

            option.value = port.device;

            option.text =
                `${port.device} - ${port.description}`;

            select.appendChild(option);
        });
    });
}

loadPorts();

// ============================================
// CONNECT DMM
// ============================================

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



</script>

</body>
</html>
