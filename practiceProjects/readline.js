// this is to use the libraries
// readline takes the user input so that we can do something with it
var readline = require("readline");

// not quite like OOP, but we are kind of creating an object we can stick into the readline
// this is created with the parameters stdin and stdout
// process is the default environment for node
rl = readline.createInterface(process.stdin, process.stdout);



// We can ask readline to behave the way we want, and one way is the symbol or whatever we
// want to show at the terminal
rl.setPrompt("$");

// we invoke the prompt with this
rl.prompt();

var commands = {
	ls:function(){
		console.log(list);
	},
	add:function(){
		var item = words.join(' ');
		list.push(item);
		console.log(item + " added");
	},
	rm:function(item){
		console.log("removing " + item);
		console.log("located at " + list.indexOf(item));
		list.splice(list.indexOf(item), 1);
	},
	exit:function(){
		console.log("bye!");
		process.exit(0);
	}
};

var list = [];
// We now want to do something with what the user just entered
// to do this, we use the on()
// this will wait for the user input, and respond with whatever the user inputted
rl.on('line', function(line){

	// split on space, so we get the separated list of words that the user is typing in the console
	words = line.split(' '),
	// The first word is the command, so we shift the array and reconstruct the array without the first element,
	// while storing the first word as the command
	command = words.shift();

	// the args are the words that we typed, so join() will combine them without the array
	argsStr = words.join();

	// as declared above, the commands are described in the array of functions
	// we simply pass the command and the arguments, and if the command matches one of the commands decalared above,
	// it will go into the function definition corresponding to that particular command
	commands[command](argsStr);

	rl.prompt();
});