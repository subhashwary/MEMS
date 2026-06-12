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
