<?php
	$host = "localhost";
	$user = "root";
	$pass = "root";
	$db = "testPHP";
	//$prodId = POST_get['id'];
	//'insert into order values prodId prodName'
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);

	$result = mysql_query("SELECT * from products");

?>

<html>
<body>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<div class="container text-center" align="center">
	<h1>Here is a list of products that are available</h1>
	<table class="table table-hover">
		<tr>
			<th>id</th>
			<th>name</th>
		</tr>
		<?php
			while($product=mysql_fetch_assoc($result)){
				echo "<tr>";
				echo "<td>".$product['id']."</td>";
				echo "<td>".$product['name']."</td>";
				//echo "<td><input type=submit class=btn btn-info value=Add to cart></input></td>";
				echo "<td><a href=products.php?page=products&action=add&id=".$product['id'].">Add to cart</a></td>";
				echo "</tr>";
			}// end of while
		?>
	</table> 
</div>
<!-- Footer -->
<div class="footer navbar-fixed-bottom text-center" style="background: #ccffee">
	 <h5>A Project by: Rohan, Vignesh, Yen</h5> 
</div>
</body>
</html>