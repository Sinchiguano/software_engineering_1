// var x = "Hello World!";

// var message="first global"


// function a() {
// 	var message="inside a";
// 	console.log(message)
// }
// a();



var names =["pepe","carlos","juan"];


// var myObj={
// 	name: "juanito",
// 	course: "HTML",
// 	platform: "coursera", 
// };


// for (var i  in myObj){
// 	myObj[i]
// }

// for (var name in names){
// console.log("hello "+names[name]);
// }



//closures

function makeMultiplier(multiplier) {
	function b(){
		console.log("multiplier " + multiplier);
	}
	b()



	return (
		function (x){
			return multiplier*x;
		}
		);
}


var doubleAll=makeMultiplier(2);
console.log(doubleAll(10));