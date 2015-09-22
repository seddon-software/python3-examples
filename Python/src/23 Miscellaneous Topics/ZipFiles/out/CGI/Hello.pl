#! C:/Perl/bin/perl.exe
############################################################
#
#                Hello - HTML generation
#
############################################################

# invoke using a URL of the form
# http://admin:7001/CGI/cgi-bin/Hello.pl
# http://localhost:80/cgi-bin/Hello.pl

print <<MYPAGE;
Content-type: text/html

<HTML>
        <HEAD>
        <TITLE>Hello World</TITLE>
        </HEAD>
        <BODY>
        <H1>Greetings</H1>
        </BODY>
</HTML>

MYPAGE
