<!DOCTYPE html>
<html>
<head>
    <title>Verkefni 4</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <%
    nafn = ''
    braut = ''
    for nemandi in bekkur['nemendur']:
        if nemandi['kt'] == kt:
            nafn = nemandi['nafn']
            braut = nemandi['braut']
        end
    end
    %>

    <img src="/static/{{kt}}.jpg">

    <div class="h2block">
    <h2>Kt: {{kt}}</h2>
    <h2>Nafn:{{nafn}} </h2>
    <h2>Braut: {{braut}}</h2>
    </div>
    <br>
    <a href="javascript:history.back()">Til baka</a>

</body>
</html>