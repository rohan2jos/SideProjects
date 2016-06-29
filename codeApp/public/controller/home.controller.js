/*
    Created by rohan2jos
    06/28/2016
*/

// we will now create the controller : homeController.
// The best practice is to put the controller in an IIFE, but for the sake of understandability and
// readability, we will use the plain javascript method

angular.module("codeApp").controller('homeController', function(){
    console.log("welcome to the home controller, you have now wired up the app successfully, start coding!");
});

/*
app.controller('aboutController', function($scope){
    console.log("welcome to the about controller");
    $scope.title = "tempAbout";
});*/
