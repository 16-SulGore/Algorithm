const HOUR = 3600;
const MINUTE = 60;

String.prototype.toSecond = function() {
    const [hh, mm, ss] = this.split(':').map((str) => parseInt(str));
    if((hh && mm && ss) === undefined) return 0;
    
    return hh * HOUR + mm * MINUTE + ss;
}

Number.prototype.toTime = function() {
    let time = this;
    const hh = Math.floor(time / HOUR);
    time -= hh * HOUR;
    const mm = Math.floor(time / MINUTE);
    time -= mm * MINUTE
    return [hh, mm, time]
        .map((e) => e.toString().padStart(2, '0'))
        .join(':');
}

function solution(playTime, advTime, logs) {
    const [end, adv] = [playTime, advTime].map((str) => str.toSecond());
    const timeline = Array.from(Array(end + 1), () => 0);

    logs.forEach((log) => {
        const [start, end] = log.split('-').map((str) => str.toSecond());
        timeline[start] += 1;
        timeline[end] -= 1;
    });
    
    for(let i = 1, prev = timeline[0]; i < end; i++) {
        timeline[i] += prev;
        prev = timeline[i];
        timeline[i] += timeline[i - 1];
    }
    
    let result = 0;
    let maximum = timeline[adv];
    for(let i = adv + 1; i < end; i++){
        const total = timeline[i] - timeline[i - adv];
        if(total > maximum) {
            result = i - adv + 1;
            maximum = total;
        }
    }    
    
    return result.toTime();
}