#! /bin/perl -w
############################################################
#
#	Select.pl
#
############################################################

  use strict;
  use DBI;

  my $connection = ConnectToDatabase();
  my $SQL = "select FIRST_NAME, LAST_NAME, PHONE_NUMBER from PHONE_TABLE";
  my $statement = $connection->prepare($SQL);
  $statement->execute() || warn $DBI::errstr;
  
  # Declare columns
  my ($firstName, $lastName, $phoneNumber);  
  $statement->bind_columns(undef, \$firstName, \$lastName, \$phoneNumber);

  # Fetch rows from DB
  while($statement->fetch()) {
    printf("%-16s%-16s%-16s\n", $firstName, $lastName, $phoneNumber);
    1;
  }
  $statement->finish();
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
                         { RaiseError => 1, AutoCommit => 0 }
                        ) || warn "No database connection $DBI::errstr ";
  return $dbh;
}
