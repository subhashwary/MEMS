if(data.event_timestamp !== lastEventTime){

    lastEventTime = data.event_timestamp;

    eventMarkers.push({

        index: sampleNumber - 1,

        title: data.event_name,

        time: data.event_timestamp

    });

}
