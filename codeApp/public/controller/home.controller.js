/*
    Created by rohan2jos
    06/28/2016
*/

app.controller('homeController', function(){
    console.log("welcome to the home controller, you have now wired up the app successfully, start coding!");
});

app.controller('aboutController', function($scope){
    console.log("welcome to the about controller");
    $scope.title = "tempAbout";
});
