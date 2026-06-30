const voltageValue = Number(data.dmm_voltage);

dmmData.push(
    Number.isFinite(voltageValue)
        ? voltageValue
        : null
);
