<?php 

    $host = "localhost";
    $user = "root";
    $pass = "root";
    $db = "cart";
    //$prodId = POST_get['id'];
    //'insert into order values prodId prodName'
    mysql_connect($host, $user, $pass);
    mysql_select_db($db);
    $theUser = intval($_GET['user']);
    if(isset($_GET['action']) && $_GET['action']=="add"){ 
          

        $id=intval($_GET['id']);
        $price=intval($_GET['price']);
        $checkQuant = mysql_query("select p.stock from Product p where p.id = {$id}");
        $rowTemp = mysql_fetch_assoc($checkQuant);
        $queryCheck = mysql_query("select count(*) as count from OrderDetials where productid = {$id}");
        $rowCheck = mysql_fetch_assoc($queryCheck);
        $temp = $rowCheck['count'];
        if($rowTemp['stock'] >= 1){
            if($temp > 0){
                mysql_query("update OrderDetials set quantity = quantity + 1 where productid = {$id}");
                mysql_query("update Product set stock = stock - 1 where id = {$id}");
                echo "<script type='text/javascript'>alert('Added to cart!');</script>";
            }
            else{
            mysql_query("insert into OrderDetials (userid, productid, quantity, orderdate, totalamount) values ({$theUser}, {$id}, 1, CURDATE(), {$price})");
            mysql_query("update Product set stock = stock - 1 where id = {$id}"); 
            echo "<script type='text/javascript'>alert('Added to cart!');</script>";
            }
        }else{
            $message="This product is not in stock, please check back later!!";
        }                
        }  
  
?> 
<html>
<head>
    <title>Mobiles</title>
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
            <div>
                <ul class="nav navbar-nav">
                    <li class="active"><a href="Mobiles.php?user=<? echo $theUser ?>">Mobiles</a></li>
                    <li><a href="Laptops.php?user=<? echo $theUser ?>">Laptops</a></li>
                    <li><a href="index2.php?user=<? echo $theUser ?>">Televisions</a></li>
                    <li><a href="productType.php?user=<? echo $theUser ?>">Categories</a></li>
                </ul>
            </div> <!-- end of div for page list -->
        </div> <!-- End of container in navbar -->
    </div> <!-- End of navbar -->
    <br />
    <br />
    <div id="mainDiv">
    <h1><center>Mobiles we have<center></h1> 
    <br />
    <?php 
        if(isset($message)){ 
            echo "<h2><center>$message<center></h2>"; 
        } 
    ?> 
    <div id="tableDiv">
    <table class="table table-hover" style="width:100%"> 
        <tr> 
            <th>About</th>
            <th>Name</th> 
            <th>Model</th> 
            <th>Price</th> 
            <th>Quantity Available</th>
            <th>Average Rating</th>
            <th>Action</th> 
        </tr> 
          
        <?php 
          
            $sql="select * from Product p where p.producttypeid = '2'"; 
            $query=mysql_query($sql); 
             
            while ($row=mysql_fetch_array($query)) { 
                $tempProd = $row['id'];
                $fetchRate = mysql_query("select AVG(rating) as avg from ProductRating where productid = {$tempProd}");
                $rateRes = mysql_fetch_array($fetchRate);
        ?> 
            <tr> 
                <td style= "width:30%"><?php echo $row['description']?></td>
                <td><?php echo $row['name'] ?></td> 
                <td><?php echo $row['modelno'] ?></td> 
                <td><?php echo $row['price'] ?>$</td> 
                <td><?php echo $row['stock'] ?> units</td> 
                <td><?php echo $rateRes['avg']?></td>
                <td><a href="Mobiles.php?page=products&action=add&id=<?php echo $row['id']?>&price=<? echo $row['price'] ?>&user=<? echo $theUser ?>">Add to cart</a></td> 
            </tr> 
        <?php 
                  
            } 
          
        ?>     
    </table>
</div> <!-- end of table div -->
    <br />
    <br />
    <div id = "finDiv" style="background-image:url(black_bg.png); height: 50%; width: 100%;" align="center" style="height:auto">
        <?php echo $row['description'] ?>
        <br />
        <br />
        <br />
        <br />
        <a href="cart.php?user=<? echo $theUser ?>"><h3 style="color:white">Go To Cart</h3></a>
    </div>
</div><!-- end of main div -->
</body>
</html>