var firstFunction = function(callback){
	console.log("hello, first function");
	callback();
}

var secondFunction = function(callback){
	console.log("hello, second function");
	callback();
}

var thirdFunction = function(callback){
	console.log("hello, third function");

	// we must ensure that if nothing is passed as callback to this particular function,
	// then we handle that case
	if(callback){
		callback();
	}
}

// node is asyn, and hence we make maximum use of callbacks to ensure that
// the callbacks are controlled
firstFunction(function(){
	secondFunction(function(){
		thirdFunction();
	});
});