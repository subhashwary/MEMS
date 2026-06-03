<div class="ess-box instrument-box">

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
