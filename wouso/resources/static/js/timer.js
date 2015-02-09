/** Convertor
*/
function seconds2time( seconds )
{
	seconds = seconds % 3600;
	minute = Math.floor(seconds / 60);
	secunde = seconds % 60;
	if (minute < 10)
		minute ='0' + minute;
	if (secunde < 10)
		secunde = '0' + secunde;

	return minute + ':' + secunde;
}

function update(timerid, formid) {
	text = seconds2time(seconds);
	seconds = seconds - 1;
	$('#' + timerid).html(text);
	if(seconds >= 0) {
		if (seconds < 30)
			$('#' + timerid).addClass('wrong');
		setTimeout( "update('" + timerid + "','" + formid + "')", 1000);
	}
	else
		$('#' + formid).submit();
}

var StartTimer = function StartTimer(timerID, formID, time_seconds) {

	var node = document.getElementById(timerID);
	var form = document.getElementById(formID);

	function updateTimer() {
		time_seconds -= 1;
		node.textContent = seconds2time(time_seconds);

		if (time_seconds <= 30) {
			node.setAttribute('data-warning', 'true');
		}

		if (time_seconds <= 0) {
			form.submit();
			clearInterval(timer);
		}
	}

	var timer = setInterval(updateTimer, 1000);
};
