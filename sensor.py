eventMarkers = eventMarkers
    .map(m => ({...m,index:m.index-1}))
    .filter(m => m.index >= 0);
