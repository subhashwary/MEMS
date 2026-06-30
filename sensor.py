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

        .psu,
        .dmm-box {
            align-self: start;
        }

        .ess-grid {
            align-items: start;
            display:grid;

            grid-template-columns:
                1fr
                1fr
                150px;

            gap:20px;
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
            min-height: 150px;

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
            grid-row: 1;

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

.card canvas {
    width:100% !important;
    height: 400px !important;
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
    height: auto !important;
    min-height: 420px;
    width: 100%;
    
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 25px;
    box-sizing: border-box;
}

.psu-box {
    padding-bottom: 25px;

    grid-column: 1;
    grid-row: 1;
}

.dmm-box {
    grid-column: 2;
    grid-row: 1;

    width:100%;
    max-width: 100%;
}

.ps-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;  /* 2 buttons per row */
    gap: 8px;
    margin-top: 15px;
    width: 50%;
    justify-items: center;
}

.psu-box {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.ps-row-bottom {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 15px;
    width: 100%;
}

.psu-controls {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.ps-control {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
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
    font-size: 24px;        /* bigger text */
    font-weight: bold;
    /* margin-top: -10px;      /* move upward */
    margin-bottom: 20px;
    color: #111827;
    letter-spacing: 0.5px;
    text-align: center;
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

.psu-buttons {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;

    margin-top: 25px;
    padding-bottom: 20px;
    gap: 10px;
}

.psu-onoff {
    display: flex;

    justify-content: center;

    gap: 20px;

    width: 100%;
}

.psu-onoff button {
    width: 100px;
}

#psuSendBtn {
    width: 140px;
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
    min-height: 320px;
    justify-content: flex-start;
    align-items: flex-start;
    text-align: left;
}

.ess-status-box {
    min-height: 320px;

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

<!-- PSU BOX -->
<div class="ess-box instrument-box psu-box">

    <div class="ps-title">DC Power Supply</div>

    <div style="margin-bottom:15px;">
        <select id="psuPortSelect"
            style="padding:8px;border-radius:6px;width:140px;">
            <option>Loading...</option>
        </select>

        <button onclick="connectPSU()" class="control-btn">
            Connect
        </button>
    </div>

    <div class="ps-head">CH1</div>

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

    <div class="psu-buttons">

        <button
            id="psuSendBtn"
            class="control-btn"
            onclick="updatePSU()">
            Send To PSU
        </button>

        <div class="psu-onoff">

            <button
                id="psuOnBtn"
                class="control-btn start-btn"
                onclick="startPSU()">
                ON
            </button>

            <button
                id="psuOffBtn"
                class="control-btn stop-btn"
                onclick="stopPSU()">
                OFF
            </button>

        </div>

    </div>

</div>
<!-- PSU BOX END -->
<!-- DMM BOX -->
<div class="ess-box instrument-box dmm-box">

    <div class="dmm-title">
        Digital Multimeter
    </div>

    <div style="margin-bottom:15px;">

        <select id="comPortSelect"
            style="padding:8px;border-radius:6px;width:140px;">
            <option>Loading...</option>
        </select>

        <button onclick="connectDMM()" class="control-btn">
            Connect
        </button>

    </div>

    <div class="instrument-row">

        <span class="instrument-label">
            Voltage
        </span>

        <div id="dmmVoltage" class="dmm-display">
            000.000
        </div>

        <span>VDC</span>

    </div>

    <div class="ps-row-bottom">

        <button
            id="dmmStartBtn"
            class="control-btn start-btn"
            onclick="startDMM()">
            Start
        </button>

        <button
            id="dmmStopBtn"
            class="control-btn stop-btn"
            onclick="stopDMM()">
            Stop
        </button>

    </div>

</div>
<!-- DMM BOX END -->
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
    style="grid-column: 1; grid-row:2;">

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

    <h3>ESS Status</h3>
    <div id="essState">
        IDLE
    </div>
    <br>
    <div id="cycleCount">
        Cycle 0
    </div>
</div>

<div class="ess-box ess-status-box"
     style="grid-column:2;grid-row:2;">

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

    <span>Seconds</span>
</div>

<div class="instrument-row">
    <span class="instrument-label">ON Time</span>

    <input id="onTime" type="number" value="5">

    <span>Seconds</span>
</div>

<div class="instrument-row">
    <span class="instrument-label">OFF Time</span>

    <input id="offTime" type="number" value="3">

    <span>Seconds</span>
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

</div>

<br>

    <!-- Controls -->
    <div class="card">
        <button class="btn-primary" onclick="resetData()">Reset</button>
        <button class="btn-danger" onclick="downloadCSV()">Download CSV</button>
    </div>

<script>

let labels = [];
let dmmData = [];
let stateData = [];
let eventLabels = [];
let eventMarkers = [];
let previousState = "";

const ctx = document.getElementById('chart').getContext('2d');

const eventLabelPlugin = {

    id: "eventLabels",

    afterDatasetsDraw(chart) {

        const ctx = chart.ctx;

        const meta = chart.getDatasetMeta(0);

        ctx.save();

        ctx.fillStyle = "black";
        ctx.font = "11px Arial";

        meta.data.forEach((point, index) => {

            if(eventLabels[index] !== ""){

                ctx.save();

                ctx.translate(point.x, point.y - 10);

                ctx.rotate(-Math.PI/4);

                ctx.fillText(eventLabels[index],0,0);

                ctx.restore();

            }

        });

        ctx.restore();

    }

};

Chart.register(eventLabelPlugin);

const eventPlugin = {

    id: "eventPlugin",

    afterDatasetsDraw(chart) {

        const ctx = chart.ctx;
        const meta = chart.getDatasetMeta(0);

        ctx.save();

        ctx.font = "12px Arial";
        ctx.textAlign = "center";

        eventMarkers.forEach(marker => {

            const point = meta.data[marker.index];

            if (!point) return;

            const x = point.x;
            const y = point.y;

            // vertical guide line
            ctx.beginPath();
            ctx.strokeStyle = "#666";
            ctx.setLineDash([4,4]);
            ctx.moveTo(x, chart.scales.y.top);
            ctx.lineTo(x, y);
            ctx.stroke();

            ctx.setLineDash([]);

            // title
            ctx.fillStyle = "blue";
            ctx.fillText(marker.title, x, chart.scales.y.top + 15);

            // timestamp
            ctx.fillStyle = "black";
            ctx.fillText(marker.time, x, chart.scales.y.top + 30);

        });

        ctx.restore();

    }

};

Chart.register(eventPlugin);

const chart = new Chart(ctx, {

    type: 'line',

    data: {
        labels: labels,

        datasets: [

            {
                label: 'DMM Voltage (V)',
                data: dmmData,
                borderColor: 'green',
                borderWidth: 2,
                yAxisID: 'y',
                fill: false,
                tension: 0.2
            }
        ]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {

            x: {
                title: {
                    display: true,
                    text: "Timestamp"
                }
            },

            y: {
    title: {
        display: true,
        text: 'Voltage (V)'
    },
    min: 0,
    max: 3
}
        }
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
            updateControls(data.mode);

        // GRAPH
        labels.push(data.timestamp);
        dmmData.push(data.dmm_voltage);
        stateData.push(data.ess_state);

        if (data.ess_state !== previousState) {

            if (data.ess_state.includes("_ON")) {

                eventMarkers.push({
                    index: labels.length - 1,
                    title: `C${data.current_cycle} ON`,
                    time: data.timestamp
                });

            }
            else if (data.ess_state.includes("_OFF")) {

                eventMarkers.push({
                    index: labels.length - 1,
                    title: `C${data.current_cycle} OFF`,
                    time: data.timestamp
                });

            }

            previousState = data.ess_state;
        }

        if (
            stateData.length < 2 ||
            stateData[stateData.length - 1] !== stateData[stateData.length - 2]
        ) {
            eventLabels.push(data.timestamp);
        } else {
            eventLabels.push("");
        }

            if(labels.length > 300) {

                labels.shift();
                dmmData.shift();
                stateData.shift();
                eventLabels.shift();
            }

            eventMarkers = eventMarkers
            .map(m => ({...m,index:m.index-1}))
            .filter(m => m.index >= 0);

            chart.update();
        });

}, 1500);

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

// Reset
function resetData() {

    labels.length = 0;
    dmmData.length = 0;
    stateData.length = 0;
    eventLabels.length = 0;
    eventMarkers.length = 0;

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

const dmmStartBtn =
    document.getElementById("dmmStartBtn");

const dmmStopBtn =
    document.getElementById("dmmStopBtn");

const psuSendBtn =
    document.getElementById("psuSendBtn");

const psuOnBtn =
    document.getElementById("psuOnBtn");

const psuOffBtn =
    document.getElementById("psuOffBtn");

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
    })
    .then(res => res.json())
    .then(data => {

        if(data.error){
            alert(data.error);
            return;
        }

        autoBtn.classList.add("active");
        manualBtn.classList.remove("active");

    });

    })
    .then(() => {
        autoBtn.classList.add("active");
        manualBtn.classList.remove("active");
    });
};

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

        if (ports.length === 0) {

            dmmSelect.innerHTML =
                '<option>No Ports Found</option>';

            psuSelect.innerHTML =
                '<option>No Ports Found</option>';

            return;
        }

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

// CONNECT DMM
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

    manualBtn.classList.toggle("active", data.mode === "manual");
    autoBtn.classList.toggle("active", data.mode === "auto");

    updateControls(data.mode);

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

from flask import Flask, jsonify, request, render_template, send_file
import random
import time
import serial.tools.list_ports
import re

def parse_value(x):
    try:
        if x is None:
            return 0.0
        x = str(x)
        
        # extract number from: "1.998V", "0.700A", "+0.282E+1"
        match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", x)
        return float(match.group()) if match else 0.0
    except:
        return 0.0
    
def send_psu(voltage, current):

    global psu

    if not psu:
        return "PSU not connected"

    try:
        with psu_lock:

            cmd_v = f"VSET1:{voltage:.3f}\r\n"
            cmd_i = f"ISET1:{current:.3f}\r\n"

            psu.write(cmd_v)
            time.sleep(0.1)

            psu.write(cmd_i)
            time.sleep(0.1)

            psu.write("OUT1\r\n")

        return "OK"

    except Exception as e:
        return str(e)

from threading import Lock

serial_lock = Lock()

psu_lock = Lock()
psu_busy = False

from instrument import PowerSupply, Multimeter
from logger import initialize_csv, log_data, CSV_FILE

app = Flask(__name__)

# INITIALIZATION
initialize_csv()

# Connect to instruments (replace COM ports with your actual ports)
psu = None

dmm = None

# GLOBAL SYSTEM STATE
system_state = {
    "mode": "manual",
    "dmm_running": False,
    "dmm_voltage": 0.0,
    "pressure": 0.0,

    "psu_voltage": 0.0,
    "psu_current": 0.0,
    "psu_output": False,

    "cycle_start": time.time(),

    # 🔴 ADD THIS LINE
    "last_psu_read": 0,
    "ess_state": "IDLE",

    "current_cycle": 0,

    "auto_running": False,

    "cycle_event": "Waiting",

    "config": {
        "initial_off": 5,
        "on_time": 5,
        "off_time": 5,
        "cycles": 10
    }
}

# WEB PAGE
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():

    return jsonify({

        "psu_connected": psu is not None,

        "dmm_connected": dmm is not None,

        "mode": system_state["mode"],

        "current_cycle":
            system_state["current_cycle"],

        "ess_state":
            system_state["ess_state"],

        "cycle_event":
            system_state["cycle_event"],

        "psu_output": system_state["psu_output"],

        "auto_running": system_state["auto_running"],

        "voltage": system_state["psu_voltage"],

        "current": system_state["psu_current"]

    })

@app.route('/connect_psu', methods=['POST'])
def connect_psu():

    global psu

    data = request.json
    com_port = data.get("port")

    with psu_lock:

        # Close previous PSU connection if any
        try:
            if psu:
                psu.close()
        except:
            pass

        try:

            psu = None
            response = ""

            # Try common baud rates
            for baud in [9600, 19200, 38400, 57600]:

                try:

                    print(f"\nTrying PSU baudrate: {baud}")

                    candidate = PowerSupply(
                        port=com_port,
                        baudrate=baud,
                        # timeout=2
                    )

                    idn  = candidate.query("*IDN?")
                    vset = candidate.query("VSET1?")
                    iset = candidate.query("ISET1?")

                    print("IDN  =", idn)
                    print("VSET =", vset)
                    print("ISET =", iset)

                    if (
                        not vset
                        or not iset
                        or vset == "ERROR"
                        or iset == "ERROR"
                    ):
                        print("No PSU response")
                        candidate.close()
                        continue

                    try:

                        candidate.write("VSET1:2.00")
                        time.sleep(0.5)

                        candidate.write("ISET1:0.10")
                        time.sleep(0.5)

                        check_v = candidate.query("VSET1?")
                        check_i = candidate.query("ISET1?")

                        print("VERIFY V =", check_v)
                        print("VERIFY I =", check_i)

                        print("PORT =", com_port)
                        print("BAUD =", baud)
                        print("OPEN =", candidate.ser.is_open)

                        psu = candidate

                        system_state["psu_output"] = False
                        system_state["psu_voltage"] = 0.0
                        system_state["psu_current"] = 0.0

                        print("\n================================")
                        print("PSU CONNECTED SUCCESSFULLY")
                        print("PORT:", com_port)
                        print("BAUDRATE:", baud)
                        print("================================\n")

                        return jsonify({
                            "status": "connected",
                            "baudrate": baud,
                            "id": f"PSU Connected @ {baud}"
                        })

                    except Exception as e:

                        print("PSU TEST FAILED:", e)

                        candidate.close()

                except Exception as e:

                    print(f"Failed at {baud}: {e}")

            # If all baud rates fail
            psu = None

            return jsonify({
                "status": "error",
                "message": "No response from PSU on any baud rate"
            }), 500

        except Exception as e:

            psu = None

            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500

@app.route('/psu_test')
def psu_test():

    global psu

    if not psu:
        return jsonify({"error": "PSU not connected"})

    try:

        with psu_lock:

            print("SETTING VOLTAGE...")
            psu.write("VSET1:2.00")
            time.sleep(1)

            print("SETTING CURRENT...")
            psu.write("ISET1:0.10")
            time.sleep(1)

            print("OUTPUT ON...")
            psu.write("OUT1")
            time.sleep(1)

            vset = psu.query("VSET1?")
            iset = psu.query("ISET1?")

            try:
                vout = psu.query("VOUT1?")
            except:
                vout = "N/A"

            try:
                iout = psu.query("IOUT1?")
            except:
                iout = "N/A"

            result = {
                "VSET1": vset,
                "ISET1": iset,
                "VOUT1": vout,
                "IOUT1": iout
            }

            print(result)

            return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

@app.route('/psu_debug')
def psu_debug():

    global psu

    if not psu:
        return jsonify({"error": "No PSU"})

    try:

        result = {
            "VSET1": psu.query("VSET1?"),
            "ISET1": psu.query("ISET1?"),
            "VOUT1": psu.query("VOUT1?"),
            "IOUT1": psu.query("IOUT1?")
        }

        print(result)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

# LIVE DATA API
@app.route('/data')
def data():

    global psu_busy, psu

    # Simulated pressure reading
    # system_state["pressure"] = pressure_from_sensor

    # AUTO MODE LOGIC
    if (
        system_state["mode"] == "auto"
        and system_state["auto_running"]
    ):
        print("AUTO LOOP RUNNING")

        cfg = system_state["config"]

        elapsed = time.time() - system_state["cycle_start"]

        initial_delay = cfg["initial_off"]
        on_time = cfg["on_time"]
        off_time = cfg["off_time"]
        cycles = cfg["cycles"]

        cycle_period = on_time + off_time

        if elapsed < initial_delay:

            system_state["ess_state"] = "INITIAL_DELAY"
            system_state["cycle_event"] = "Waiting Initial Delay"
            system_state["current_cycle"] = 0
            system_state["dmm_running"] = False

            if system_state["psu_output"]:
                try:
                    with psu_lock:
                        psu.write("OUT0")
                except:
                    pass

                system_state["psu_output"] = False

        else:

            adjusted = elapsed - initial_delay

            print("AUTO STARTED")
            print("elapsed =", elapsed)
            print("adjusted =", adjusted)

            completed_cycles = int(
                adjusted // cycle_period
            )

            if completed_cycles >= cycles:

                system_state["auto_running"] = False
                system_state["mode"] = "manual"

                system_state["ess_state"] = "COMPLETE"
                system_state["cycle_event"] = "ESS Completed"

                if psu and system_state["psu_output"]:
                    try:
                        with psu_lock:
                            psu.write("OUT0")
                    except:
                        pass

                    system_state["psu_output"] = False

            else:

                cycle_no = completed_cycles + 1

                position = adjusted % cycle_period

                print("cycle_no =", cycle_no)
                print("position =", position)

                system_state["current_cycle"] = cycle_no

                if position < on_time:

                    system_state["ess_state"] = f"CYCLE_{cycle_no}_ON"
                    system_state["cycle_event"] = f"Cycle {cycle_no} ON"
                    system_state["dmm_running"] = True

                    if psu and not system_state["psu_output"]:
                        try:
                            with psu_lock:
                                psu.write("OUT1")
                            
                            print("PSU ON")
                            system_state["psu_output"] = True

                        except Exception as e:
                            print("PSU ON ERROR:", e)

                else:

                    system_state["ess_state"] = f"CYCLE_{cycle_no}_OFF"
                    system_state["cycle_event"] = f"Cycle {cycle_no} OFF"
                    system_state["dmm_running"] = False

                    if psu and system_state["psu_output"]:
                        try:
                            with psu_lock:
                                psu.write("OUT0")

                            print("PSU OFF")
                            system_state["psu_output"] = False

                        except Exception as e:
                            print("PSU OFF ERROR:", e)

    # DMM READING
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
            system_state["dmm_voltage"] = round(random.uniform(0, 10), 3)
    else:
        system_state["dmm_voltage"] = 0.0

    # PSU READINGS (FIXED LOCATION)
    PSU_READ_INTERVAL = 1

    last_psu_read = system_state.get("last_psu_read", 0)

    if (
        psu
        and not psu_busy
        and (time.time() - last_psu_read > PSU_READ_INTERVAL)
    ):

        try:

            with psu_lock:

                if system_state["psu_output"]:

                    v = psu.query("VOUT1?")
                    i = psu.query("IOUT1?")

                else:

                    v = "0"
                    i = "0"

            print("PSU V =", v)
            print("PSU I =", i)

            if not v or not i:

                print("WARNING: PSU returned empty response")

            else:

                system_state["psu_voltage"] = parse_value(v)
                system_state["psu_current"] = parse_value(i)

                system_state["last_psu_read"] = time.time()

        except Exception as e:

            print("PSU read error:", e)

            try:
                psu.close()
            except:
                pass

            psu = None

    # LOG DATA
    log_data(
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["mode"],
        system_state["ess_state"],
        system_state["current_cycle"],
        system_state["cycle_event"]
    )

    return jsonify({

        **system_state,

        "timestamp": time.strftime("%H:%M:%S"),

        "mode_numeric":
            1 if system_state["mode"] == "auto" else 0,

        "ess_numeric":
            2 if "ON" in system_state["ess_state"]
            else 1 if system_state["ess_state"] == "INITIAL_DELAY"
            else 0
    })

# MODE CONTROL
@app.route('/mode', methods=['POST'])
def set_mode():

    mode = request.json.get("mode")

    print("MODE REQUEST =", mode)

    if mode == "manual":

        system_state["mode"] = "manual"
        system_state["auto_running"] = False

        return jsonify({"status":"manual mode"})

    elif mode == "auto":

        if not psu:
            return jsonify({
                "error": "Connect PSU first"
            }), 400

        if not dmm:
            return jsonify({
                "error": "Connect DMM first"
            }), 400

        system_state["mode"] = "auto"
        system_state["auto_running"] = True

        system_state["cycle_start"] = time.time()

        system_state["current_cycle"] = 0

        system_state["ess_state"] = "INITIAL_DELAY"

        system_state["cycle_event"] = "Starting ESS"

        return jsonify({
            "status": "auto mode"
        })

    return jsonify({"error":"Invalid mode"}),400

# DMM CONTROL
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

# POWER SUPPLY CONTROL
@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu, psu_busy

    if system_state["mode"] == "auto":
        return jsonify({
            "error": "Manual PSU control disabled in AUTO mode"
        }), 403

    if not psu:
        return jsonify({"error":"PSU not connected"}),500

    try:
        psu_busy = True

        data = request.json or {}

        voltage = float(data.get("voltage",0))
        current = float(data.get("current",0))

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            psu.write("OUT1")
            time.sleep(0.5)

        system_state["psu_output"] = True
        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        return jsonify({"status":"started"})

    except Exception as e:

        return jsonify({"error":str(e)}),500

    finally:

        psu_busy = False

@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    global psu, psu_busy

    if system_state["mode"] == "auto":
        return jsonify({
            "error": "Manual PSU control disabled in AUTO mode"
        }), 403

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    try:

        psu_busy = True

        with psu_lock:

            psu.write("OUT0")
            time.sleep(0.5)

        system_state["psu_output"] = False
        system_state["psu_voltage"] = 0.0
        system_state["psu_current"] = 0.0

        return jsonify({
            "status": "stopped"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        psu_busy = False

# NEW ROUTE
@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu, psu_busy

    if system_state["mode"] == "auto":
        return jsonify({
            "error": "PSU settings locked in AUTO mode"
        }), 403

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:

        psu_busy = True

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            #psu.write("OUT1")
            #time.sleep(0.1)

        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        return jsonify({
            "status": "updated"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
    
    finally:
        psu_busy = False

# SAVE AUTO MODE CONFIGURATION
@app.route('/config', methods=['POST'])
def save_config():

    data = request.json or {}

    initial_off = max(1, int(data.get("initial_off", 5)))
    on_time = max(1, int(data.get("on_time", 5)))
    off_time = max(1, int(data.get("off_time", 5)))
    cycles = max(1, int(data.get("cycles", 10)))

    system_state["config"] = {
        "initial_off": initial_off,
        "on_time": on_time,
        "off_time": off_time,
        "cycles": cycles
    }
    
    system_state["cycle_start"] = time.time()

    return jsonify({
        "status": "Configuration saved",
        "config": system_state["config"]
    })

# DOWNLOAD CSV
@app.route('/download')
def download():
    return send_file(CSV_FILE, as_attachment=True)

# RESET SYSTEM
@app.route('/reset', methods=['POST'])
def reset():

    global system_state

    system_state["mode"] = "manual"
    system_state["auto_running"] = False
    system_state["dmm_running"] = False

    system_state["current_cycle"] = 0
    system_state["cycle_event"] = "Waiting"
    system_state["ess_state"] = "IDLE"

    system_state["dmm_voltage"] = 0.0
    system_state["psu_voltage"] = 0.0
    system_state["psu_current"] = 0.0
    system_state["pressure"] = 0.0

    system_state["cycle_start"] = time.time()

    # Erase old CSV and create fresh one
    initialize_csv()

    return jsonify({
        "status": "reset complete"
    })

# GET INSTRUMENT IDS
@app.route('/id')
def get_ids():
    return jsonify({
        "psu_id": psu.idn() if psu else "Not Connected",
        "dmm_id": dmm.idn() if dmm else "Not Connected"
    })

@app.route('/psu_raw')
def psu_raw():

    global psu

    if not psu:
        return "No PSU"

    cmds = [
        "VSET1?",
        "ISET1?",
        "STATUS?"
    ]

    for cmd in cmds:
        print(cmd, "=", psu.query(cmd))

    return "Done"

# GET AVAILABLE COM PORTS
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

# CONNECT DMM
@app.route('/connect_dmm', methods=['POST'])
def connect_dmm():

    global dmm

    data = request.json

    com_port = data.get("port")

    BAUDRATES = [9600, 19200, 38400, 57600, 115200]

    # CLOSE OLD CONNECTION FIRST
    try:
        if dmm:
            dmm.close()
            dmm = None
    except:
        pass

    # TRY DIFFERENT BAUDRATES
    for baud in BAUDRATES:

        test_dmm = None

        try:

            print(f"\nTrying baudrate: {baud}")

            test_dmm = Multimeter(
                port=com_port,
                baudrate=baud,
            #   timeout=2
            )

            # give instrument time
            time.sleep(1)

            response = test_dmm.idn()

            print("RAW ID RESPONSE:", response)

            # VALID RESPONSE CHECK
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

    # IF ALL BAUDRATES FAIL
    dmm = None

    return jsonify({
        "status": "error",
        "message": "Could not connect to DMM"
    }), 500

# MAIN
if __name__ == '__main__':
    app.run(
    debug=False,
    threaded=True
)
