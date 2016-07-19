<html>
<head>
	<title>MVC</title>
</head>
<body>

<h1>TABLE</h2>
<hr/>
<table>
% for (team,points) in c.data:
    <tr>
     <td>${team}</td>
     <td>${points}</td>
    </tr>
% endfor
</table>

<a href="index">Start again</a>
</body>
</html>

