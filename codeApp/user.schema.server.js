module.exports = function(mongoose){
    var UserSchema = mongoose.schema({
        username: String,
        password: String,
        email: String
    },{collection: 'Users'});
    
    return UserSchema;
}