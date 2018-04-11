<?php
	$od=scandir(".");
	foreach ($od as $key => $value) {
		if(preg_match('/json/i', $value)){
			$m[]=$value;
		}
	}
	echo json_encode($m);
	file_put_contents('all.json', json_encode($m));