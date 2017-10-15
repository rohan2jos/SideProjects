<?php
	$host = "localhost";
	$user = "root";
	$pass = "root";
	$db = "cart";
	//$prodId = POST_get['id'];
	//'insert into order values prodId prodName'
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);

	$id=intval($_GET['id']);
	$rate=$_POST['rating'];
	echo "<script type='text/javascript'>alert('$rate');</script>";
	$theUser=intval($_GET['user']);
	if(isset($_GET['action']) && $_GET['action']=="add" && $rate != 0){ 
    	mysql_query("insert into ProductRating (rating, userid, productid) values ({$rate}, {$theUser}, {$id})");
    	mysql_query("delete from OrderDetials where productid = {$id}");
    }
 

	$result = mysql_query("select * from OrderDetials where userid = {$theUser}");

?>

<html>
<head>
	<title>Rate</title>
</head>
<body>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
            <div>
                <ul class="nav navbar-nav">
                    <li><a href="Mobiles.php?user=<? echo $theUser ?>">Mobiles</a></li>
                    <li><a href="Laptops.php?user=<? echo $theUser ?>">Laptops</a></li>
                    <li><a href="index2.php?user=<? echo $theUser ?>">Televisions</a></li>
                    <li><a href="productType.php?user=<? echo $theUser ?>">Categories</a></li>
                </ul>
            </div> <!-- end of div for page list -->
        </div> <!-- End of container in navbar -->
    </div> <!-- End of navbar -->
    <br />
    <br />
    <br />
    <br />
	<div id="mainDiv" align="center" height:100%;">
	<h1>Here is your order history</h1>
	<h4>You may submit a rating for a product that you have previously purchased here<h4>
	<br />
	<table class="table table-hover">
		<tr>
			<th>name</th>
			<th>orderdate</th>
			<th>cost</th>
			<th>quantity</th>
			<th>rating</th>
		</tr>
		<?php
			while($product=mysql_fetch_assoc($result)){
		?>

			<tr> 
				<?php 
					$tempName = $product['productid'];
					$queryName = mysql_query("select name as n from Product where id = $tempName");
					$tempArr = mysql_fetch_assoc($queryName);
					$finName = $tempArr['n'];
				?>
                <td><?php echo $finName ?></td>
                <td><?php echo $product['orderdate'] ?></td> 
                <td><?php echo $product['totalamount'] ?>$</td> 
                <td><?php echo $product['quantity'] ?> units</td> 
            	<td><form method="post" action="rate.php?action=add&id=<? echo $tempName ?>&user=<? echo $theUser ?>"><input type="text" name="rating" placeholder="between 1 - 5"></input><input type="submit" name="submit" ></input></form></td>
            </tr> 
         <?php   
         }
		?>
	</table> 
	<br />
	<div id = "finDiv" style="background-image:url(black_bg.png); height: 50%; width: 100%;">
	</div>
	<br />
	<br />
</div>
<!-- Footer -->
</body>
</html>