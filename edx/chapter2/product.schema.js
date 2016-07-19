var mongoose = require('mongoose');

// as there are three types, we will require the Category for the product schema to take shape
// since each product knows the category that it belongs to
var Category = require('./category');

var productSchema = {
    name: {
        type: String,
        required: true
    },
    pictures: [
        {
            type: String,
            match: /^http:\/\//i
        }
    ],
    price: {
        amount: {
            type: Number,
            required: true
        },
        currency: {
            type: String,
            enum: ['USD', 'EUR', 'GBP'],
            required: true
        }
    },
    category: Category.categorySchema
};

// now exporting this schema so it is available for the other files to see
module.exports = new mongoose.Schema(productSchema);
module.exports.productSchema = productSchema;