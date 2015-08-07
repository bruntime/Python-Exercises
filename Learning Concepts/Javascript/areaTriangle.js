function calculate() {
	var side1 = document.getElementById("side1").value;
	var side2 = document.getElementById("side2").value;
	var angle = document.getElementById("angle").value;
	var calcAngle = Math.sin(angle)
	var area = ((side1 * side2)/2) * calcAngle;
	document.getElementById("area").value = area;
	}