!#/usr/bin/node
function printMessage(){
	const argumentsNumber = arguments.length;

	if( argumentsNumber === 0) {
		console.log("No argument");
	}else if(argumentsNumber === 1){
		console.log("Argument found");
	}else{
		console.log("Arguments found");
	}
}
printMessage('Lucy')
