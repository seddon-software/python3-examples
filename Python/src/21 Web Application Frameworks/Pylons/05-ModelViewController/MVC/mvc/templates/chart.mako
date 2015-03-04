<html>
<head>
	<title>MVC</title>
</head>
<body>

<h1>CHART</h2>
<hr/>
<table>
% for (team,points) in c.data:
	<% s = "" %>
	% for ch in range(int(points)):
		<% s += "X" %>
	% endfor 
    <tr>
     <td>${team}</td>
     <td>${s}</td>
    </tr>
% endfor
</table>

<a href="index">Start again</a>

</body>
</html>

