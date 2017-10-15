<?php
	$host = "localhost";
	$user = "root";
	$pass = "root";
	$db = "testPHP";
	//$prodId = POST_get['id'];
	//'insert into order values prodId prodName'
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);
	$userid = $_GET['user'];
	$_POST['userid'];
	$result = mysql_query("SELECT * from products");

?>

<html>
<body style="background-image:url(black_bg.png)">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<div align="center">
	<h1 style="color:white;">Categories of products that are available</h1>
	<a href="cart.php?user=<? echo $userid ?>"><h3 style="color:yellow;">Want to go to your cart directly?</h3>
	<br />
	<br />
	<br />
	<a href="index2.php?user=<? echo $userid ?>"><div id="televisionDiv" style="height:400px; margin-bottom:0; background-image:url(tv.jpg)">
		<h1 style="color:white;">TELEVISIONS</h1>
	</div></a>
	<a href="Mobiles.php?user=<? echo $userid ?>"><div id="mobileDiv" style="height:400px; background-image:url(phone.jpg);">
		<h1 style="color:black;">MOBILES</h1>
	</div></a>
	<a href="Laptops.php?user=<? echo $userid?>"><div id="laptopDiv" style="height:400px; background-image:url(laptop.jpg);">
		<h1 style="color:white;">LAPTOPS</h1>
	</div></a>
</div>
</body>
</html>