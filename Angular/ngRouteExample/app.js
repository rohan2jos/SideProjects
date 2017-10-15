var sampleApp = angular.module('sampleApp', []);

sampleApp.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/AddNewOrder', {
        templateUrl: 'add_order.html',
        controller: 'AddOrderController'
    }).when('/ShowOrders', {
        templateUrl: 'show_orders.html',
        controller: 'ShowOrdersController'
    }).otherwise({
        redirectTo: '/AddNewOrder'
    });
}]);

sampleApp.controller('AddOrderController', function($scope){
    console.log("You made it to the controller");
    $scope.message = "Welcome to the add order page";
});

sampleApp.controller('ShowOrdersController', function($scope){
    console.log("You made it to the show orders page");
    $scope.message = "Welcome to the show orders page"
});