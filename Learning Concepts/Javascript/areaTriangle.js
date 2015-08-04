function checkNum() {
	var check_num = document.getElementById('side').value;
	if (typeof check_num === 'number') {
	alert('Value must be a number');
	return false;
	}
	else{
	return true;
	}
}