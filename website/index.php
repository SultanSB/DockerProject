<!DOCTYPE html>
<html lang="en">
<head>
   <title>Book Service</title>
</head>
<body>
   <h1>Welcome to the Book Collection</h1>
   <ul>
       <?php
           // Fetch JSON from the Flask Books service
           $json = file_get_contents('http://books-service'); // Update service name if different
           $obj = json_decode($json);
           $books = $obj->books; // Access the "books" property
           foreach ($books as $book){
               echo "<li>$book</li>";
           }
       ?>
   </ul>
</body>
</html>
