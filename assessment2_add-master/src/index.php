<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
	"string" => "",
	"answer" => 0
);
try {
$x = $_REQUEST['x'];
$y = $_REQUEST['y'];

if (is_numeric($x)) {
	if (is_numeric($y)) {
    $answer=add($x,$y);
		$output['answer']=$answer;
	}
	else {
	    $output['error'] = true;
	}
} else {
    $output['error'] = true;
}

$output['string']=$x."+".$y."=".$answer;
}

catch(Exception $e) {
$output['error'] = true;
}

echo json_encode($output);

exit();
