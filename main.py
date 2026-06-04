// ============================================
// LOAD AVAILABLE COM PORTS
// ============================================

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
                `${port.device} - ${port.description};

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
