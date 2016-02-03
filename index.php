<?php
$cookieLinks = file('cookieurls.txt');
echo $cookieLinks[array_rand($cookieLinks)];
?>