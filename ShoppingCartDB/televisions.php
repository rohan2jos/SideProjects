<?php
	$host = "localhost";
	$user = "root";
	$pass = "root";
	$db = "cart";
	//$prodId = POST_get['id'];
	//'insert into order values prodId prodName'
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);

	$result = mysql_query("select * from Product p where p.producttypeid = '1'");

?>

<html>
<body>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<div class="container text-center" align="center">
	<h1>Here is a list of Televisions that are available</h1>
	<br />
	<table class="table table-hover">
		<tr>
			<th>about</th>
			<th>name</th>
			<th>model</th>
			<th>price</th>
			<th>action</th>
		</tr>
		<?php
            while ($row=mysql_fetch_array($result)) { 
                  
        ?> 
            <tr> 
                <td style= "width:30%"><?php echo $row['description']?></td>
                <td><?php echo $row['name'] ?></td> 
                <td><?php echo $row['modelno'] ?></td> 
                <td><?php echo $row['price'] ?>$</td> 
                <td><a href="televisions.php?page=products&action=add&id=<?php echo $row['id']?>&price=<? echo $row['price'] ?>">Add to cart</a></td> 
            </tr> 
        <?php 
                  
            } 
          
        ?>  
	</table> 
</div>
<!-- Footer -->
<div class="footer navbar-fixed-bottom text-center" style="background: #ccffee">
	 <h5>A Project by: Rohan, Vignesh, Yen</h5> 
</div>
</body>
</html>