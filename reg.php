<!DOCTYPE html>
<html>

<head>
<meta content="text/html; charset=utf-8" httpequiv="Content-Type">
<title>WePython</title>
<link rel="stylesheet" href="css/style2.css" type="text/css">
</head>

<body >
<div style="width: 600px; margin: 0 auto; background-color: #3a3a3a; padding:10px 300px 592px 300px;">

<?php
	//Данные для подключения к серверу MySQL
	$servername = "localhost";
	$username = "root";
	$password = "";
	// Вводим название базы данных
	$dbname = "register_form";
	//Созданиие подключения
	$conn = mysqli_connect($servername, $username, $password,
	$dbname);
	mysql_select_db('register_form');
	//Проверка кодировки utf8 
	mysql_query('SET NAMES utf8') or die ("не удалось установить
	кодировку");
	//Проверка соединения с БД
	if (!$conn) {
	 die("Подключение не выполнено: " . mysqli_connect_error());
	}
	//Строка с текстом sql запроса для таблицы
	$sql = "INSERT INTO register_data (fio, ph_number, email,dateBirth, sex, status_edu,city)
	VALUES ('".$_POST['fio']."','".$_POST['ph_number']."',
	'".$_POST['email']."','".$_POST['dateBirth']."',
	'".$_POST['sex']."','".$_POST['status_edu']."',
	'".$_POST['city']."')" ;
	
	// mysqli_query($conn, $sql) - выполнение sql запроса
	//Проверка статуса выполнения sql запроса
	if (mysqli_query($conn, $sql)) {
	echo '<h2 style="color:#f79754; text-align: left; font: 60px Bebas;">Запись успешно добавлена</h2>';
	echo '<div style="color:#f79754; text-align: left; font: 60px Bebas;">'. "<a href='index.html'>На главную</a>". '</div>';
	} else {
	 echo '<div style="color:#ffffff; text-align: left; font: px Bebas;">'."Ошибка добавления записи: " . $sql . "<br>" . mysqli_error($conn).'</div>';
	}
	//Закрытие соединения
	mysqli_close($conn);
	?>
	
	<?php
	echo '<h2 style="color:#ffffff; text-align: center; font: 45px Bebas;">Ваши данные:</h2>';
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">ФИО: '.$_POST['fio'].'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">Номер телефона: '. $_POST['ph_number'] .'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">EMAIL: '.$_POST['email'] .'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">Дата рождения: '.$_POST['dateBirth'] .'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">Пол: '.$_POST['sex'] .'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">Образование: '.$_POST['status_edu'] .'</div>';
	echo "<br>";
	echo '<div style="color:#ffffff; text-align: left; font: 30px Bebas;">Город: '.$_POST['city'] .'</div>';
	?>
	
</body>
</html>