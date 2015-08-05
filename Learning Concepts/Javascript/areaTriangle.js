function calculate() {
	var side1 = document.getElementById("side1").value;
	var side2 = document.getElementById("side2").value;
	var side3 = document.getElementById("side3").value;
	var area = (side1 * side2 * side3);
	document.getElementById("area").innerHTML = area
	alert area
}