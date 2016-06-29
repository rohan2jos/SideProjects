/*
    Created by rohan2jos
    06/28/2016
*/

// we will now create the controller : homeController.
// The best practice is to put the controller in an IIFE, but for the sake of understandability and
// readability, we will use the plain javascript method

angular.module("codeApp").controller('homeController', function($scope){
	console.log("welcome to the home controller, you have now wired up the app successfully, start coding!");

	// creating an array to display in the homepage

	$scope.products = 
			[
			{name: "kosal",
			author: "some author 1",
			image: "img1.jpg"},
			{name: "kosal2",
			author: "some author 2",
			image: "img2.jpg"},
			{name: "kosal3",
			author: "some author 3",
			image: "img3.jpg"},
			{name: "kosal4",
			author: "some author 4",
			image: "img4.jpg"},
			{name: "kosal5",
			author: "some author 5",
			image: "img5.jpg"},
			{name: "kosal6",
			author: "some author 6",
			image: "img6.jpg"}
			]
});

/*
app.controller('aboutController', function($scope){
    console.log("welcome to the about controller");
    $scope.title = "tempAbout";

	// creat

});*/
