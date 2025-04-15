<?php
// Ganti IP berikut dengan IP dari Pico W kamu
$pico_ip = "192.168.22.212"; // Contoh

if (isset($_POST['relay'])) {
	$relay_status = $_POST['relay']; // 'on' atau 'off'
	$url = "http://$pico_ip/relay=$relay_status";

	$response = file_get_contents($url); // Kirim perintah
	echo "<h3>Respon dari perangkat: $response</h3>";
	echo "<a href='index.php'>Kembali</a>";
} else {
	echo "Perintah tidak ditemukan.";
}
