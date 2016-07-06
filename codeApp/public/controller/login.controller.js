angular.module("codeApp").controller("loginController", function($scope, $rootScope, $location, UserService){

	$scope.login = login;	

	console.log("welcome to the login controller");
	$scope.msg = "Please enter the login credentials";


    
    // new login function that will call the service and that will send the request to the 
    // backend
    function login(){
        UserService.login($scope.user.username, $scope.user.password)
            .then(function(res){
                if(res.data !== null){
                    console.log("setting rootscope current user as " + res.data);
                    UserService.setCurrentUser(res.data);
                    $location.url("/home");
                }else{
                    alert("The credentials were wrong, please enter the credentials again");
                }
        });
    }
    
    // old function for login that was validating the array in the front end
    
//	function login(){
//		console.log("you just clicked on the login function");
//		console.log("the username is " + $scope.user.username + " and the password is " + $scope.user.password);
//
//        
//        // commenting out code to make sure that it works
//        // leaving commented code here temporarily so that it can be easily reverted in case of error
////
////		
////		$scope.users = [{username: "rohan", password: "rohan"}, {username: "bob", password: "bob"}, {username: "fred", password: "fred"}];
//
//
//		console.log("validating ...");
//		for(i = 0; i<$scope.users.length; i++){
//			console.log("checking for " + $scope.users[i].username);
//			if($scope.users[i].username == $scope.user.username && $scope.users[i].password == $scope.user.password){
//				console.log("Welcome, " + $scope.user.username);
//                $rootScope.currentUser = $scope.users[i];
//                console.log("login controller sets the rootscope user as " + $rootScope.currentUser.username);
//                $location.url("/home");
//                UserService.test();
//				break;
//			}
//		}
//
//	}

})
