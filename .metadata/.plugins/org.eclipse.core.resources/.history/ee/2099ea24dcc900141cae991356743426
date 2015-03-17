############################################################
#
#	StoredProcedures.pl
#
############################################################

  use strict;
  use DBI;

  my $connection = ConnectToDatabase();
  my ($newSalary, $statement);
  
  $statement = $connection->prepare(
    q{
        BEGIN
            IncreaseSalary(:theName, :Increase, :NewSalary);
        END;
    });
  
  $statement->bind_param(":theName", 'Charles');
  $statement->bind_param(":Increase", 10.5);
  $statement->bind_param_inout(":NewSalary", \$newSalary, 8);
  $statement->execute();

  print "$newSalary \n";

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
                         { RaiseError => 1, AutoCommit => 1 }
                        ) || warn "No database connection $DBI::errstr ";
  return $dbh;
}
  