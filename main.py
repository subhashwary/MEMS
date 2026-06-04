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
            grid-template-columns: 35% 45% 20%;
            gap: 20px;
            align-items: start;
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

.manual-box {
    grid-column: 3;
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
    width: 90px;
    height: 30px;

    text-align: center;

    border: 1px solid #ccc;
    border-radius: 6px;
}

.instrument-row {
    display: grid;
    grid-template-columns: 130px 100px 50px;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin: 10px 0;
}

.dmm-display {
    width: 260px;
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


<div class="ess-box instrument-box psu-box">

    <div class="ps-title">DC Power Supply</div>

    <div class="ps-head" style="margin-bottom:20px;">
        CH1
    </div>

    <div class="instrument-row">
        <span class="instrument-label">Set Voltage</span>

        <input
            id="psVoltage"
            type="number"
            step="0.01"
            value="2.00">

        <span>Volt</span>
    </div>

    <div class="instrument-row">
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



function updatePSU() {

    fetch('/psu/set', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            voltage:
                document.getElementById("psVoltage").value,

            current:
                document.getElementById("psCurrent").value
        })
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

</script>

</body>
</html>


from flask import Flask, jsonify, request, render_template, send_file
import random
import time
import serial.tools.list_ports

from threading import Lock

serial_lock = Lock()

from instrument import PowerSupply, Multimeter
from logger import initialize_csv, log_data, CSV_FILE

app = Flask(__name__)

# =========================================================
# INITIALIZATION
# =========================================================
initialize_csv()

# Connect to instruments (replace COM ports with your actual ports)
psu = None
dmm = None

try:

    psu = PowerSupply(
        port="COM6",   # replace with actual PSU port
        baudrate=9600,
        timeout=2
    )

    print("================================")
    print("PSU CONNECTED")
    print(psu.idn())
    print("================================")

except Exception as e:

    print("PSU CONNECTION FAILED")
    print(e)

    psu = None

# =========================================================
# GLOBAL SYSTEM STATE
# =========================================================
system_state = {
    "mode": "manual",
    "dmm_running": False,
    "dmm_voltage": 0.0,
    "pressure": 0.0,
    "psu_voltage": 0.0,
    "psu_current": 0.0,
    "cycle_start": time.time(),
    "config": {
        "initial_off": 5,
        "on_time": 5,
        "off_time": 5,
        "cycles": 10
    }
}


# =========================================================
# WEB PAGE
# =========================================================
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/status')
def status():

    return jsonify({
        "psu_connected": psu is not None,
        "dmm_connected": dmm is not None
    })


# =========================================================
# LIVE DATA API
# =========================================================
@app.route('/data')
def data():
    # Simulated pressure reading (replace with real sensor data)
    system_state["pressure"] = round(random.uniform(20, 100), 2)

    # -----------------------------------------------------
    # AUTO MODE LOGIC
    # -----------------------------------------------------
    if system_state["mode"] == "auto":
        cfg = system_state["config"]
        elapsed = time.time() - system_state["cycle_start"]

        cycle_period = cfg["on_time"] + cfg["off_time"]

        if elapsed < cfg["initial_off"]:
            system_state["dmm_running"] = False
        else:
            adjusted = elapsed - cfg["initial_off"]
            position = adjusted % cycle_period
            system_state["dmm_running"] = position < cfg["on_time"]

    # -----------------------------------------------------
    # DMM VOLTAGE READING
    # -----------------------------------------------------
    if system_state["dmm_running"]:
        if dmm:
            try:
                reading = dmm.measure_voltage()

                if isinstance(reading, (int, float)):
                    system_state["dmm_voltage"] = reading
            except Exception as e:
                print("DMM read error:", e)
                system_state["dmm_voltage"] = 0.0
        else:
            # Simulation mode if DMM not connected
            system_state["dmm_voltage"] = round(random.uniform(0, 10), 3)
    else:
        system_state["dmm_voltage"] = 0.0

    # -----------------------------------------------------
    # PSU READINGS
    # -----------------------------------------------------
    if psu:
        try:
            system_state["psu_voltage"] = float(psu.get_voltage())
            system_state["psu_current"] = float(psu.get_current())
        except Exception as e:
            print("PSU read error:", e)

    # -----------------------------------------------------
    # LOG DATA TO CSV
    # -----------------------------------------------------
    log_data(
        system_state["pressure"],
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["psu_current"],
        system_state["mode"]
    )

    return jsonify(system_state)


# =========================================================
# MODE CONTROL
# =========================================================
@app.route('/mode', methods=['POST'])
def set_mode():
    mode = request.json.get("mode")

    if mode in ["manual", "auto"]:
        system_state["mode"] = mode
        system_state["cycle_start"] = time.time()
        return jsonify({"status": f"{mode} mode activated"})

    return jsonify({"error": "Invalid mode"}), 400


# =========================================================
# DMM CONTROL
# =========================================================
@app.route('/dmm/start', methods=['POST'])
def start_dmm():
    if system_state["mode"] != "manual":
        return jsonify({"error": "Auto mode active"}), 403

    system_state["dmm_running"] = True
    return jsonify({"status": "DMM started"})


@app.route('/dmm/stop', methods=['POST'])
def stop_dmm():
    if system_state["mode"] != "manual":
        return jsonify({"error": "Auto mode active"}), 403

    system_state["dmm_running"] = False
    return jsonify({"status": "DMM stopped"})


# =========================================================
# POWER SUPPLY CONTROL
# =========================================================
@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:

        psu.set_voltage(voltage)
        psu.set_current(current)

        psu.output_on()

        system_state["dmm_running"] = True

        return jsonify({
            "status": "PSU started",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    if psu:
        try:
            psu.output_off()

            system_state["dmm_running"] = False
            system_state["dmm_voltage"] = 0.0

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"status": "PSU stopped"})

# =========================================================
# NEW ROUTE
# =========================================================
@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 5))
    current = float(data.get("current", 0.1))

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:
        psu.set_voltage(voltage)
        psu.set_current(current)

        return jsonify({
            "status": "Values Set",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =========================================================
# SAVE AUTO MODE CONFIGURATION
# =========================================================
@app.route('/config', methods=['POST'])
def save_config():
    data = request.json or {}

    system_state["config"] = {
        "initial_off": int(data.get("initial_off", 5)),
        "on_time": int(data.get("on_time", 5)),
        "off_time": int(data.get("off_time", 5)),
        "cycles": int(data.get("cycles", 10))
    }

    system_state["cycle_start"] = time.time()

    return jsonify({
        "status": "Configuration saved",
        "config": system_state["config"]
    })


# =========================================================
# DOWNLOAD CSV
# =========================================================
@app.route('/download')
def download():
    return send_file(CSV_FILE, as_attachment=True)


# =========================================================
# GET INSTRUMENT IDS
# =========================================================
@app.route('/id')
def get_ids():
    return jsonify({
        "psu_id": psu.idn() if psu else "Not Connected",
        "dmm_id": dmm.idn() if dmm else "Not Connected"
    })


# =========================================================
# GET AVAILABLE COM PORTS
# =========================================================
@app.route('/ports')
def get_ports():

    ports = serial.tools.list_ports.comports()

    port_list = []

    for port in ports:
        port_list.append({
            "device": port.device,
            "description": port.description
        })

    return jsonify(port_list)



# =========================================================
# CONNECT DMM
# =========================================================
@app.route('/connect_dmm', methods=['POST'])
def connect_dmm():

    global dmm

    data = request.json

    com_port = data.get("port")

    BAUDRATES = [9600, 19200, 38400, 57600, 115200]

    # -----------------------------------------
    # CLOSE OLD CONNECTION FIRST
    # -----------------------------------------
    try:
        if dmm:
            dmm.close()
            dmm = None
    except:
        pass

    # -----------------------------------------
    # TRY DIFFERENT BAUDRATES
    # -----------------------------------------
    for baud in BAUDRATES:

        test_dmm = None

        try:

            print(f"\nTrying baudrate: {baud}")

            test_dmm = Multimeter(
                port=com_port,
                baudrate=baud,
                timeout=2
            )

            # give instrument time
            time.sleep(1)

            response = test_dmm.idn()

            print("RAW ID RESPONSE:", response)

            # ---------------------------------
            # VALID RESPONSE CHECK
            # ---------------------------------
            if response and len(response) > 3:

                dmm = test_dmm

                print("\n================================")
                print("DMM CONNECTED SUCCESSFULLY")
                print("PORT:", com_port)
                print("BAUDRATE:", baud)
                print("DMM ID:", response)
                print("================================\n")

                return jsonify({
                    "status": "connected",
                    "id": response,
                    "baudrate": baud
                })

            else:

                print("Invalid response")

                test_dmm.close()

        except Exception as e:

            print(f"FAILED at {baud}: {e}")

            # IMPORTANT
            try:
                if test_dmm:
                    test_dmm.close()
            except:
                pass

    # -----------------------------------------
    # IF ALL BAUDRATES FAIL
    # -----------------------------------------
    dmm = None

    return jsonify({
        "status": "error",
        "message": "Could not connect to DMM"
    }), 500


# =========================================================
# MAIN
# =========================================================
if __name__ == '__main__':
    app.run(
    debug=False,
    threaded=True
)



import serial
import time

ports = ["COM5", "COM6", "COM11", "COM12"]

for port in ports:
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=2)
        time.sleep(1)

        ser.write(b"*IDN?\n")
        time.sleep(0.5)

        response = ser.readline().decode(errors='ignore').strip()

        print(f"{port}: {response if response else 'No response'}")
        ser.close()

    except Exception as e:
        print(f"{port}: Not available ({e})")


import serial
import time

from threading import Lock

serial_lock = Lock()

class SCPIInstrument:

    def __init__(self, port, baudrate=115200, timeout=2):

        self.port = port

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

        time.sleep(1)

    # -------------------------------------------------
    # WRITE COMMAND
    # -------------------------------------------------
    def write(self, cmd):

        if not cmd.endswith("\n"):
            cmd += "\n"

        self.ser.write(cmd.encode())

    # -------------------------------------------------
    # QUERY COMMAND
    # -------------------------------------------------
    def query(self, cmd):

        with serial_lock:

            try:
                # Clear old data
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()

                # Add newline automatically
                if not cmd.endswith("\n"):
                    cmd += "\n"

                # Send command
                self.ser.write(cmd.encode())

                # Wait for full response
                time.sleep(0.3)

                # Read response
                response = self.ser.readline().decode(
                    errors='ignore'
                ).strip()

                print(f"SCPI QUERY [{cmd.strip()}] -> {response}")

                return response

            except Exception as e:

                print("SCPI Query Error:", e)

                return "ERROR"

    # -------------------------------------------------
    # CLOSE PORT
    # -------------------------------------------------
    def close(self):

        if self.ser.is_open:
            self.ser.close()


# =====================================================
# POWER SUPPLY CLASS
# =====================================================

class PowerSupply(SCPIInstrument):

    def idn(self):
        return self.query("*IDN?")

    def set_voltage(self, voltage):
        self.write(f"VSET1:{voltage}")

    def set_current(self, current):
        self.write(f"ISET1:{current}")

    def get_voltage(self):
        return self.query("VOUT1?")

    def get_current(self):
        return self.query("IOUT1?")

    def output_on(self):
        self.write("OUT1")

    def output_off(self):
        self.write("OUT0")


# =====================================================
# MULTIMETER CLASS
# =====================================================

class Multimeter(SCPIInstrument):

    def idn(self):

        return self.query("*IDN?")

    def measure_voltage(self):

        try:
            with serial_lock:

                # Clear old garbage data
                self.ser.reset_input_buffer()

                # Send command
                self.ser.write(b"MEAS:VOLT:DC?\n")

                # Small wait for full response
                time.sleep(0.2)

                # Read full line
                response = self.ser.readline().decode(errors='ignore').strip()

                print("RAW RESPONSE:", response)

                # Clean unwanted characters
                response = response.replace('\r', '').replace('\n', '')

                # Reject incomplete scientific notation
                if response.endswith('E') or response.endswith('+') or response.endswith('-'):
                    raise ValueError(f"Incomplete reading: {response}")

                value = float(response)

                return round(value, 4)

        except Exception as e:

            print("Measurement Error:", e)

            return None


from instrument import Multimeter

print("Connecting to COM3...")

dmm = Multimeter("COM3")

print("DMM ID:")
print(dmm.idn())


from instrument import Multimeter
import time

dmm = Multimeter("COM3")

print("Connected:")
print(dmm.idn())

print("\nReading voltage...\n")

while True:

    voltage = dmm.measure_voltage()

    print("Voltage =", voltage)

    time.sleep(1)


import pyvisa

rm = pyvisa.ResourceManager()

for resource in rm.list_resources():
    try:
        inst = rm.open_resource(resource)
        print(resource, "->", inst.query("*IDN?"))
    except:
        pass


import serial.tools.list_ports

print("\nAvailable COM Ports:\n")

ports = serial.tools.list_ports.comports()

if len(ports) == 0:
    print("No COM ports detected.")

else:
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"HWID: {port.hwid}")
        print("-" * 40)


import csv
import os
from datetime import datetime

CSV_FILE = "sensor_data.csv"


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Timestamp",
                "Pressure_kPa",
                "DMM_Voltage",
                "PSU_Voltage",
                "PSU_Current",
                "Mode"
            ])


def log_data(pressure, dmm_voltage, psu_voltage, psu_current, mode):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pressure,
            dmm_voltage,
            psu_voltage,
            psu_current,
            mode
        ])

