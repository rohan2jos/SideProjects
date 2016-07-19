var mongodb = require('mongodb');

var uri = "mongodb://localhost:27017/sample2"

mongodb.connect(uri, function(err, db){
    if(err){
        console.log("Error in connecting to the db.  Error is: " + err);
        process.exit(1);
    }
    
    // we have now connected to the database
    
    var doc = {
        name: "Star Wars: A New Hope",
        year: "1977",
        director: "George Lucas"
    }
    
    // we will now insert this into the db
    db.collection('movies').insert(doc, function(err, docs){
        if(err){
            console.log("There was an error in inserting the doc into the db, error: " + err);
            process.exit(1);
        }
        
        // lets search for something that has the year 1977
        
        var toFind = {year: "1977"};
        
        db.collection('movies').find(toFind).toArray(function(err, docs){
            if(err){
                console.log("There was an error in retrieving from the database, error: " + err);
                process.exit(1);
            }
            
            console.log("=====Data Found=====");
            docs.forEach(function(oneDoc){
                console.log(JSON.stringify(oneDoc));
            });
        });
    });
});

//
//
//mongodb.connect(uri, function(err, db){
//    if(err){
//        console.log("There was an issue in the connection to the database");
//        process.exit(1);
//    }
//    else{
//        console.log("The database connection was successful");
//        
//        db.collection('sample').insert({name:"rohan"}, function(err, result){
//            if(err){
//                console.log("There was an error in the insertion ");
//                process.exit(1);
//            }else{
//                console.log("The data was inserted successfully!");
//            }
//            
//            
//            db.collection('sample').find().toArray(function(err, docs){
//                if(err){
//                    console.log("There was an error in showing the data");
//                    process.exit(1);
//                }
//                console.log("=====DATA FOUND=====");
//                docs.forEach(function(doc){
//                    console.log(JSON.stringify(doc));
//                });
//                process.exit(0);
//            });
//            
//        });
//    }
//});

