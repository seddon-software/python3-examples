#! /bin/perl
##########################################################
#
#	Populate Database
#
##########################################################

use strict;
use DBI;

my $connection = ConnectToDatabase();
open(TESTDATA, "Phones.txt") || die "can't open Phones.txt";
my @data = <TESTDATA>;

foreach my $entry (@data)
{
  my ($first, $last, $phone) = split(/\s+/, $entry);  
  my $SQL = "INSERT INTO PHONES_TABLE " .
            " (FIRST_NAME, LAST_NAME, PHONE_NUMBER)" .
            " VALUES ($first, $last, $phone)";
  $connection->do($SQL);
}
$connection->disconnect();
print "PhoneTable populated ...";
1;


sub ConnectToDatabase {
  my $host = "localhost";
  my $port = "1521";
  my $sid = "xe";
  my $user = "java";
  my $passwd = "oracle";
  my $dbh = DBI->connect("dbi:Oracle:host=$host;port=$port;sid=$sid", 
         $user, $passwd, { RaiseError => 1, AutoCommit => 0 }
         ) ||
		 warn "No database connection $DBI::errstr ";
  return $dbh;
}
