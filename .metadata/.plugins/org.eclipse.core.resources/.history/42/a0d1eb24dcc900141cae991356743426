#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	Select.pl
#
############################################################

  use strict;
  use DBI;
  use Carp;


  my $connectString="server=LNT_TRAIN11;database=pubs2";

  my $database = DBI->connect("dbi:Sybase:$connectString",
			      "train10",
			      "train10") ||
		 confess "No database connection $DBI::errstr ";

  $database->do("USE pubs2");

  my $SQL = "SELECT au_fname, au_lname FROM authors";
  my $statement = $database->prepare($SQL);
  $statement->execute() || confess $DBI::errstr;

  while( my($firstName, $lastName) = $statement->fetchrow() ){
    printf("%-16s%-16s\n", $firstName, $lastName);
  }

  $statement->finish();
  $database->disconnect();

