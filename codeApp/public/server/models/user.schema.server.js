module.exports = function(mongoose) {
    var UserSchema = mongoose.Schema({
        username: String,
        password: String,
        email: String
    }, {collection: 'Users'});

    return UserSchema;
};