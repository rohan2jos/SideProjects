// public/core.js
var scotchTodo = angular.module('scotchTodo', []);

function mainController($scope, $http) {
    $scope.formData = {};

    // when landing on the page, get all todos and show them
    $http.get('/api/todos')
        .success(function(data) {
            $scope.todos = data;
            console.log(data);
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });

    // when submitting the add form, send the text to the node API
    $scope.createTodo = function() {
        console.log("clicked create! " + $scope.formData);
        $http.post('/api/todos', $scope.formData)
            .success(function(data) {
                $scope.formData = {}; // clear the form so our user is ready to enter another
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log("error in createion");
                console.log('Error: ' + data);
            });
    };

    // delete a todo after checking it
    $scope.deleteTodo = function(todo_id) {
        console.log("clicked delete for " + todo_id);
        $http.delete('/api/todos/' + todo_id)
            .success(function(data) {
                $scope.todos = data;
                console.log(data);
            })
            .error(function(err) {
                console.log('Error: ' + err);
            });
    };

}
