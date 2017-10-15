<?php
	
	$host = "localhost";
	$user = "root";
	$pass = "root";
	$db = "cart";
	mysql_connect($host, $user, $pass);
	mysql_select_db($db); 

	if(isset($_POST['username'])){

		$username = $_POST['username'];
		$password = $_POST['password'];
		//$sql = "SELECT * FROM LoginCredentials WHERE username='".$username."' AND password='".$password."' LIMIT 1";
		$sql = "SELECT l.id FROM LoginCredentials l where l.loginid = '".$username."' AND l.password='".$password."'";
		$res = mysql_query($sql);
		$resultId = mysql_fetch_assoc($res);
		$theUser = $resultId['id'];
		if(mysql_num_rows($res) == 1){
			header("Location: productType.php?page=Category&user=$theUser");
			$_POST['id'];
			exit();
		}else{
			echo "invalid login credentials, please try again";
			exit();
		}
	}

?>

<html>
	<body>
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
		<div class="jumbotron vertical-center" align="center">
			<h1>Online Electronics Store</h1>
			<h3>Login to your account</h3>
		  <div id="mainContainer" class="container text-center container-fluid" align="center">
		    <form method="post" action="login.php">
		    <input type="text" name="username" placeholder="enter your username"/></br></br>
		    <input type="password" name="password" placeholder="enter your password"/></br></br>
		    <input type="submit" name="submit" class="btn btn-info" value="Log in" /><br /><br />
		    </form>
		  <div>
		</div>
		<div id="secondContainer" class="container text-center container-fluid" align="center">
			<h2 class="margin">We are an online shopping store for electronics</h2>
			<h2 class="margin">CS 5200, Prof. Kenneth Baclawski</h2></br></br>
		</div>
	</body>
		<!-- Footer -->
		<div class="footer navbar-fixed-bottom navbar-inverse" style="background: #ccffee">
 		 <h5>A Project by: Rohan, Vignesh, Yen</h5> 
		</div>
		<div class="Container text-center">
			<h4>This is an electronics store project that contains MySQL as the backend database</h4>
			<h4>The front end coding has been done in HTML, BOOTSTRAP, CSS and PHP</h4>
		</div>
	
</html>