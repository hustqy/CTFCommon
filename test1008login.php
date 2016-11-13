<head>
<meta charset="utf-8" />
</head>
<!-- <?php

	include 'common.php';

	$requset = array_merge($_GET, $_POST, $_SESSION, $_COOKIE);

	class db

	{

		public $where;

		function __wakeup()

		{

			if(!empty($this->where))

			{

				$this->select($this->where);

			}

		}



		function select($where)

		{

			$sql = mysql_query('select * from user where '.$where);

			return @mysql_fetch_array($sql);

		}

	}



	if(isset($requset['token']))

	{

		$login = unserialize(gzuncompress(base64_decode($requset['token'])));

		$db = new db();

		$row = $db->select('user=\''.mysql_real_escape_string($login['user']).'\'');

		if($login['user'] === 'ichunqiu')

		{

			echo $flag;

		}else if($row['pass'] !== $login['pass']){

			echo 'unserialize injection!!';

		}else{

			echo "(â¯âµâ¡â²)â¯ï¸µâ´ââ´ ";

		}

	}else{

		header('Location: index.php?error=1');

	}



?> -->(â¯âµâ¡â²)â¯ï¸µâ´ââ´