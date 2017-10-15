/*
    Created by Rohan Joshi
    Date: 05/29/2016
*/
var questionsPrepared = [];
var array = [
        {hero: "Spiritbreaker", quote: "Your spirit, like your life, is broken!"},
        {hero: "Spiritbreaker", quote: "Ran you down!"},
        {hero: "Spiritbreaker", quote:"I run rampant!"},
        {hero: "Spiritbreaker", quote: "Broke your back"},
        {hero: "Faceless Void", quote: "I have seen the future, you are not in it"},
        {hero: "Faceless Void", quote: "Then we meet, mace to face!"},
        {hero: "Faceless Void", quote: "Time is the cruelest cut"},
        {hero: "Clinkz", quote: "My spark isnt as dead as it may seem"},
        {hero: "Chen", quote: "God taketh whom he loveth best"},
        {hero: "Lifestealer", quote: "What you call righteousness, I call foolishness"},
        {hero: "Omniknight", quote: "Knowledge is peace"},
        {hero: "Death Prophet", quote: "And I was starting to enjoy being dead again"},
        {hero: "Undead", quote: "Where go the living, the dead soon follow"},
        {hero: "Witch Doctor", quote: "Prevention beats a cure"},
        {hero: "Necrophos", quote: "You plagued me long enough"},
        {hero: "Morphling", quote: "Did you see me waving?"},
        {hero: "Earth Spirit", quote: "Life's wheel goes round and round"},
        {hero: "Bane", quote: "If I cannot have you, no one will"},
        {hero: "Rubick", quote: "I am no thief, I merely borrow!"},
        {hero: "Techies", quote: "Explosives are only as dangerous as the person who builds them"},
        {hero: "Arc Warden", quote: "Life is a cycle that knows no end"},
        {hero: "Tinker", quote: "My brains and your brawn, we'll make an excellent team"},
        {hero: "Wraith King", quote: "Soon perhaps, I might choose a queen"},
        {hero: "Enigma", quote: "We are all connected on a deeper plane of existence"},
        {hero: "Bounty Hunter", quote: "Just business, nothing personal"},
        {hero: "Bounty Hunter", quote: "It was business before, but now it is personal!"},
        {hero: "Phantom Assasin", quote: "There's more of me, but less to see!"},
        {hero: "Queen of Pain", quote: "They say pain is all in the mind, but they're wrong.  Its in my hands"},
        {hero: "Clockwerk", quote: "A good defense is the best armour.  A good armour is also a good armour"},
        {hero: "Alchemist", quote: "Failure is also another kind of success.  The wrong kind"},
        {hero: "Chen", quote: "The sword teaches lessons that cannot be unlearned"}
    ];
    
console.log("The database contains " + array.length + " quotes");
/*for(i = 0 ; i < array.length; i++){
    console.log(array[i].hero + " " + array[i].quote);
}*/


// quiz maker engine
/*
    v1
    - Duplication in questions and options not handled
    - Hardcoded upper and lower bounds for random selection
    - JSON array not in its own schema file, in the code.  Needs to be kept
    in its own seperate file
    - Need to hide the JSON data and the javascript output
    - The "'" character is auto-treated with an escape slash, need to make sure
    that does not happen.
*/
function quizEngine(){
    var randomQuote = Math.floor(Math.random() * (30 - 0 + 1)) + 0;
    //console.log("===============================================");
    //console.log(randomQuote);
    console.log("Question ready:");
    var question = {question: array[randomQuote].quote, answer: array[randomQuote].hero};
    console.log(question);
    //console.log(array[randomQuote].hero + " = " + array[randomQuote].quote);
    
    console.log("===============================================");
    console.log("Building choices");
    
    var heroes = [];
    var currentHero = "";
    for(j = 0; j< array.length; j++){
        var newHero = array[j].hero;
        if(currentHero == newHero){
            // nothing
        }else{
            var flag=false;
            for(k=0;k<heroes.length;k++){
                if(heroes[k] == newHero){
                    flag = true;
                }
            }
            if(!flag){
                heroes.push(newHero);   
                //console.log("found new hero " + newHero);
                currentHero = array[j].hero;   
            }
            //console.log("duped! :P");
        }
    }
    //console.log(heroes);
    
    console.log("===============================================");
    
    var options = [array[randomQuote].hero];
    for(m=0;m<3;m++){
        var randomHeroOption = Math.floor(Math.random() * (23 - 0 + 1)) + 0;
        
        options.push(heroes[randomHeroOption]);
    }
    
    console.log(shuffle(options));
    questionsPrepared.push({
        question: question, options: options
    });
    
        
}

function shuffle(a) {
    var j, x, i;
    for (i = a.length; i; i -= 1) {
        j = Math.floor(Math.random() * i);
        x = a[i - 1];
        a[i - 1] = a[j];
        a[j] = x;
    }
    return a;
}

function mainFunction(){
    for(n=0;n<3;n++){
        console.log("---------------------------------------------------------");
        console.log("----------------QUESTION " + (n + 1));
        quizEngine();       
        console.log("---------------------------------------------------------");
    }
    console.log(questionsPrepared);
    document.getElementById("question1").innerHTML = questionsPrepared[0].question.question;
    document.getElementById("options1").innerHTML = questionsPrepared[0].options;
    document.getElementById("question2").innerHTML = questionsPrepared[1].question.question;
    document.getElementById("options2").innerHTML = questionsPrepared[1].options;
    document.getElementById("question3").innerHTML = questionsPrepared[2].question.question;
    document.getElementById("options3").innerHTML = questionsPrepared[2].options;
}

mainFunction();
// end of quiz maker engine