<?php
$cookieLinks = file('cookieurls.txt');
$theChosenOne = $cookieLinks[array_rand($cookieLinks)];

	if(isset($_GET['image'])){
		switch(strtolower(substr(strrchr(basename($theChosenOne),"."),1))) {
		    case "gif": $ctype="image/gif"; break;
		    case "png": $ctype="image/png"; break;
		    case "jpeg":$ctype="image/jpeg"; break;
		    case "jpg": $ctype="image/jpeg"; break;
		    default:
		}

		header('Content-type: ' . $ctype);
		readfile($theChosenOne);
	}else{
		echo $theChosenOne;
	}
?>