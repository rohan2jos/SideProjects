angular.module("codeApp").controller("loginController", function($scope){

	$scope.login = login;	

	console.log("welcome to the login controller");
	$scope.msg = "Please enter the login credentials";

	
	function login(){
		console.log("you just clicked on the login function");
		console.log("the username is " + $scope.user.username + " and the password is " + $scope.user.password);
	}

})
