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
