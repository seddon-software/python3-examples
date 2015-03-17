#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	ErrorHandling.pl
#
############################################################

  use strict;
  use DBI;
  use Carp;


  my %options = ( PrintError => 0,	# don't warn()
		  RaiseError => 1 );	# do die();

  my $connectString="server=LNT_TRAIN11;database=pubs2";

  my $database = DBI->connect("dbi:Sybase:$connectString",
			      "train10", 
			      "train10",
			      \%options);


# a statement that works
  my $SQL = "SELECT au_fname, au_lname FROM authors";
  my $statement = $database->prepare($SQL);
  $statement->execute();

  while( my($firstName, $lastName) = $statement->fetchrow() ){
    printf("%-16s%-16s\n", $firstName, $lastName);
  }

# now for a statement that fails
  $SQL = "SELECT dummy, au_lname FROM authors";
  $statement = $database->prepare($SQL);
  $statement->execute();

  $statement->finish();
  $database->disconnect();

