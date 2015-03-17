#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	StoredProcedures.pl
#
############################################################

  use strict;
  use DBI;
  use Carp;


  my %options = ( PrintError => 0,	# don't warn()
		  RaiseError => 1 );	# do die();


  my $connectString="server=LNT_TRAIN11;database=Test10";

  my $database = DBI->connect("dbi:Sybase:$connectString",
			      "train10",
			      "train10",
			      \%options);

  my $SQL = "EXEC info \@firstname='Fred', \@lastname='Green'";
  my $statement = $database->prepare($SQL);
  $statement->execute();

  while( my($firstName, $lastName, $phone) = $statement->fetchrow() ){
    printf("%-16s%-16s%-16s\n", $firstName, $lastName, $phone);
  }

  $statement->finish();
  $database->disconnect();
