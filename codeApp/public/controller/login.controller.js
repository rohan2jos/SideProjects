angular.module("codeApp").controller("loginController", function($scope, $rootScope, $location){

	$scope.login = login;	

	console.log("welcome to the login controller");
	$scope.msg = "Please enter the login credentials";

	
	function login(){
		console.log("you just clicked on the login function");
		console.log("the username is " + $scope.user.username + " and the password is " + $scope.user.password);


		
		$scope.users = [{username: "rohan", password: "rohan"}, {username: "bob", password: "bob"}, {username: "fred", password: "fred"}];


		console.log("validating ...");
		for(i = 0; i<$scope.users.length; i++){
			console.log("checking for " + $scope.users[i].username);
			if($scope.users[i].username == $scope.user.username && $scope.users[i].password == $scope.user.password){
				console.log("Welcome, " + $scope.user.username);
                $rootScope.currentUser = $scope.users[i];
                console.log("login controller sets the rootscope user as " + $rootScope.currentUser.username);
                $location.url("/home");
				break;
			}
		}

	}

})
