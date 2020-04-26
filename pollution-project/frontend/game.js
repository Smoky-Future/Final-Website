
var Health = 100;
//this links to our backend
var cur_pollution = 200;
var travel_cnt = 0;
var failed_chance = 0;

function Hunt(){
	//cur_pollution =
	//calc chance of failure
	if((Math.random()*10000)%100 >= failed_chance){
		document.getElementById("log").innerHTML = "You stopped and hunt some worms (+5 Health)";
		Health = Health + 5;
		set_pol();
		Display_bird(1);

		return;
	}
	//take more damage if failed
	document.getElementById("log").innerHTML = "Heavy smog blocks your site. You can hardly breathe...";
	lose_health(10);
	if(Health <= 0){
		Defeat();
		return;
	}
	set_pol();
	Display_bird(0);
	return;
}

function Travel(){
	// failed_chance = (Math.random()*100000)%100-30;

	if((Math.random()*10000)%100 >= failed_chance){
		travel_cnt ++; 
		document.getElementById("log").innerHTML = "You flew a while before you rest (+1 Progress)";
		lose_health(15);
		set_pol();
		Display_bird(0);
		//lose health here?
		if(travel_cnt == 10){
			Success();
			return;
		}
		return;
	}
	//sub this with data
	document.getElementById("log").innerHTML = "Smogs are too thick and you crashed on a tree!";
	lose_health(10);
	if(Health <= 0){
		Defeat();
		return;
	}
	set_pol();
	Display_bird(0);
	return;
}

function Defeat(){
	document.getElementById('birdpic').src='bird_lose.png';
	document.getElementById("log").innerHTML = "You are too tired... to carry on ...";
	document.getElementById("gboard").innerHTML = "<a href \"\" type=\"button\" class=\"btn btn-primary button\">Try Again</a>";
	//jump to defeat.html?
	return;
}

function Success(){
	document.getElementById('birdpic').src='bird_win.png';
	document.getElementById("log").innerHTML = "You arrived your destination ... The smoke clears and you realized the clear sky is back again.";
	document.getElementById("gboard").innerHTML = "<a href \"\" type=\"button\" class=\"btn btn-primary button\">Learn More About Air Pollution</a>"; 
	return;
	//jump to success.html?
}

function set_pol(){
	//temporary, for testing purpose
	cur_pollution = parseInt((Math.random()*1000),10)%100;
	failed_chance = cur_pollution-10;
	return;
}

function lose_health(r){
	Health = parseInt(Health - cur_pollution/r, 10);
	return;
}

function Display_bird(state){
	//changes health and 
	document.getElementById("health").innerHTML = "<span class= \"badge badge-primary health\">Health</span>"+Health+"<span class=\"badge badge-primary pollution\">Pollution</span>"+ cur_pollution;
	if (state == 1){ //eat
		document.getElementById('birdpic').src='bird_eat.png';
	}
	else if (state == 2){ //win
		document.getElementById('birdpic').src='bird_win.png';
		return;
	}
	else if (Health > 75){
		document.getElementById('birdpic').src='bird_start.png';
	} 
	else if (Health > 50){
		document.getElementById('birdpic').src='bird_hurt.png';
	}
	else {
		document.getElementById('birdpic').src='bird_dying.png';
	}

	return;
}