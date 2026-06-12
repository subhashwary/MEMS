fetch('/ports')
.then(res => {

    if(!res.ok){
        throw new Error("Failed to load ports");
    }

    return res.json();
})
.then(...)
.catch(err => {

    console.error(err);

    document.getElementById("comPortSelect").innerHTML =
        "<option>No Ports</option>";

    document.getElementById("psuPortSelect").innerHTML =
        "<option>No Ports</option>";
});
