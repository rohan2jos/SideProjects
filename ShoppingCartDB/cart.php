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
	$theUser=intval($_GET['user']);
	if(isset($_GET['action']) && $_GET['action']=="remove"){ 
    	$justQuerying = mysql_query("select quantity as q from OrderDetials where productid = $id");
    	$tempQuant = mysql_fetch_assoc($justQuerying);
    	$quantMinusOne = $tempQuant['q'] - 1;
    	if($quantMinusOne == 0){
    		mysql_query("delete from OrderDetials where productid = $id");
    		mysql_query("update Product set stock = stock + 1 where id = {$id}");
    	}
    	else{
    		mysql_query("update OrderDetials set quantity = quantity - 1 where productid = $id");
    		mysql_query("update Product set stock = stock + 1 where id = {$id}");
    	}

    }

	if(isset($_GET['action']) && $_GET['action'] == "checkout" && isset($_POST['cvv'])){

		$payment = $_POST['paymentInfo'];
		$cvv = $_POST['cvv'];
	//$sql = "SELECT * FROM LoginCredentials WHERE username='".$username."' AND password='".$password."' LIMIT 1";
		$sql = "SELECT * FROM PaymentInfo l where userid = '".$theUser."' AND cardnumber='".$payment."' AND cvv ='".$cvv."'";
		$res = mysql_query($sql);
		$resultId = mysql_fetch_assoc($res);
		if(mysql_num_rows($res) == 1){
			//echo "<script type='text/javascript'>alert('Perfect!');</script>";
			header("Location: rate.php?page=Category&user=$theUser");
			$_POST['id'];
			exit();
		}else{
			echo "invalid payment credentials, please try again";
			exit();
		}
	}
 

	$result = mysql_query("select * from OrderDetials where userid = {$theUser}");
	$totalAmount = mysql_query("select sum(totalamount * quantity) as fintotal from OrderDetials where userid = {$theUser}");
	$rowTemp = mysql_fetch_assoc($totalAmount);
	$FinSum = $rowTemp['fintotal'];

?>

<html>
<head>
	<title>Cart</title>
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
	<h1>Here is your cart</h1>
	<br />
	<table class="table table-hover">
		<tr>
			<th>name</th>
			<th>orderdate</th>
			<th>cost</th>
			<th>quantity</th>
			<th>action</th>
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
                <td><a href="cart.php?page=products&action=remove&id=<?php echo $product['productid']?>&price=<? echo $product['totalamount'] ?>&user=<? echo $theUser?>">remove from cart</a></td> 
            </tr> 
         <?php   
         }
		?>
	</table> 
	<br />

	<div id = "finDiv" style="background-image:url(black_bg.png); height: 50%; width: 100%;">
		<br />
		<br />
		<h3 style="color:white">Total amount :: $<? echo $FinSum ?></h3>
		<br/>
		<br />
		<h3 style="color:yellow">Quick Checkout</h3>
		<br />
		<br />
		<form method="post" action="cart.php?page=products&action=checkout&user=<? echo $theUser?>">
			<input type="text" name="paymentInfo" placeholder="Enter you Card info"></input>
			<input type="text" name="cvv" placeholder="Enter the CVV"></input>
			<input type="submit" id="completeProcess" class="btn btn-success" value="Complete Checkout"></input>
		</form>
	</div>
	<br />
	<br />
</div>
<!-- Footer -->
</body>
</html>