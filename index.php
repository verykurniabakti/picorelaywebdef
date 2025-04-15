<!DOCTYPE html>
<html>

<head>
	<title>Kontrol Relay IoT</title>
	<style>
		body {
			font-family: Arial;
			text-align: center;
			margin-top: 50px;
		}

		.button {
			padding: 20px 40px;
			font-size: 20px;
			margin: 10px;
		}
	</style>
</head>

<body>
	<h1>Kontrol Relay via Browser</h1>
	<form method="POST" action="send_command.php">
		<button class="button" name="relay" value="on">Hidupkan Relay</button>
		<button class="button" name="relay" value="off">Matikan Relay</button>
	</form>
</body>

</html>