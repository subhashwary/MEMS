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
