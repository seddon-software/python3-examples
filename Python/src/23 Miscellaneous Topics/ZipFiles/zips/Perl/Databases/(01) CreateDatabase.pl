#! /bin/perl
##########################################################
#
#	Create Database
#
##########################################################

use strict;
use DBI;

my $CREATE_SQL = 'CREATE TABLE "PHONES_TABLE" ( 
                  "FIRST_NAME"   VARCHAR2(20 BYTE) NOT NULL ENABLE, 
                  "LAST_NAME"    VARCHAR2(20 BYTE) NOT NULL ENABLE, 
                  "PHONE_NUMBER" VARCHAR2(20 BYTE) NOT NULL ENABLE
                 )'; 

my $connection = ConnectToDatabase();
$connection->do('DROP TABLE "PHONES_TABLE"');
$connection->do($CREATE_SQL) || confess $DBI::errstr;
$connection->disconnect();
print "PhoneTable created";
1;


sub ConnectToDatabase {
  my $host = 'localhost';
  my $port = '1521';
  my $sid = 'XE';
  my $user = "java";
  my $passwd = "oracle";

  my $dsn = "dbi:Oracle:host=$host;" .
                       "sid =$sid;".
                       "port=$port";
  my $dbh = DBI->connect($dsn, $user, $passwd, 
                         { RaiseError => 1,
                           AutoCommit => 0 
                         }
                        ) 
     or warn "No database connection $DBI::errstr ";
  return $dbh;
}
