#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	Update.pl
#
############################################################

  use strict;
  use DBI;

  my $connection = ConnectToDatabase();
  my $SQL = "UPDATE phone_table "        .
            "SET phone_number = '321' "  .
            "WHERE last_name = 'Younger'";
  $connection->do($SQL);
  $connection->disconnect();

############################################################

sub ConnectToDatabase {
  my $host = "localhost";
  my $port = "1521";
  my $sid = "XE";
  my $user = "perluser";
  my $passwd = "password";

  my $dsn = "dbi:Oracle:host=$host;sid=$sid;port=$port";
  my $dbh = DBI->connect($dsn, $user, $passwd, 
                         { RaiseError => 1, AutoCommit => 1 }
                        ) || warn "No database connection $DBI::errstr ";
  return $dbh;
}
