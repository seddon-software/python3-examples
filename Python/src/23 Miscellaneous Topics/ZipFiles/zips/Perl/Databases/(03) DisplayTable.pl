#! /bin/perl
##########################################################
#
#	Display Table
#
##########################################################

use DBI;

my $connection = ConnectToDatabase();

my $statement = $connection->prepare("SELECT * FROM PHONE_TABLE");
$statement->execute();

while(($first, $last, $phone) = $statement->fetchrow_array)
{
  printf("%-10s%-10s%4i\n", $first, $last, $phone);
  1;
}


$statement->finish();
$connection->disconnect();


sub ConnectToDatabase {
  my $host = "localhost";
  my $port = "1521";
  my $sid = "XE";
  my $user = "perluser";
  my $passwd = "password";

  my $dsn = "dbi:Oracle:host=$host;sid=$sid;port=$port";
  my $dbh = DBI->connect($dsn, $user, $passwd, 
                         { RaiseError => 1, AutoCommit => 0 }
                        ) || warn "No database connection $DBI::errstr ";
  return $dbh;
}
