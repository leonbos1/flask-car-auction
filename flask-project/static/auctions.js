remaining_elements = document.getElementsByClassName("remaining");

//text inside is Remaining time: 4 days, 15:08:04
function updateTimer() {
    Array.from(remaining_elements).forEach(element => {
        if (element.innerText.split(" ").length == 5) {
            let daysRemaining = element.innerText.split(" ")[2];
            let timeRemaining = element.innerText.split(" ")[4];
            let timeRemainingArray = timeRemaining.split(":");
            let seconds = parseInt(timeRemainingArray[2]);
            let minutes = parseInt(timeRemainingArray[1]);
            let hours = parseInt(timeRemainingArray[0]);
            let days = parseInt(daysRemaining);

            if (seconds > 0) {
                seconds -= 1;
            } else if (minutes > 0) {
                minutes -= 1;
                seconds = 59;
            } else if (hours > 0) {
                hours -= 1;
                minutes = 59;
                seconds = 59;
            } else if (days > 0) {
                days -= 1;
                hours = 23;
                minutes = 59;
                seconds = 59;
            } else {
                element.innerText = "Auction is over";
                document.getElementsByClassName("bid")[0].disabled = true;
                return;
            }
            if (seconds < 10) {
                seconds = "0" + seconds;
            }
            if (minutes < 10) {
                minutes = "0" + minutes;
            }
            if (hours < 10) {
                hours = "0" + hours;
            }
            if (days == 1) {
                element.innerHTML = `<strong>Ends in: </strong>${days} day, ${hours}:${minutes}:${seconds}`;
                return;
            }
            element.innerHTML = `<strong>Ends in: </strong>${days} days, ${hours}:${minutes}:${seconds}`;
        }
        else {
            //format is 15:08:04
            let timeRemaining = element.innerText.split(" ")[2];
            let timeRemainingArray = timeRemaining.split(":");
            let seconds = parseInt(timeRemainingArray[2]);
            let minutes = parseInt(timeRemainingArray[1]);
            let hours = parseInt(timeRemainingArray[0]);

            if (seconds > 0) {
                seconds -= 1;
            }
            else if (minutes > 0) {
                minutes -= 1;
                seconds = 59;
            }
            else if (hours > 0) {
                hours -= 1;
                minutes = 59;
                seconds = 59;
            }
            else {
                element.innerText = "Auction is over";
                document.getElementsByClassName("bid")[0].disabled = true;
                return;
            }
            //if seconds is 1 digit, add a 0 in front
            if (seconds < 10) {
                seconds = "0" + seconds;
            }
            if (minutes < 10) {
                minutes = "0" + minutes;
            }
            if (hours < 10) {
                hours = "0" + hours;
            }
            element.innerHTML = `<strong>Ends in: </strong>${hours}:${minutes}:${seconds}`;
        }
    });
}

setInterval(updateTimer, 1000);