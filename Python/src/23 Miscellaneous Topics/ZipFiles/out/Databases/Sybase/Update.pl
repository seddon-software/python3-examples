#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	Update.pl
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

  my $SQL = "UPDATE phones SET phone = '123' WHERE lname = 'Younger'";
  $database->do($SQL);

  DisplayResults();
  $database->disconnect();

############################################################

  sub DisplayResults() {
    my $SQL = "SELECT * FROM phones";
    my $statement = $database->prepare($SQL);
    $statement->execute();

    while( my($firstName, $lastName, $phone) = $statement->fetchrow() ){
      printf("%-16s%-16s%-16s\n", $firstName, $lastName, $phone);
    }

    $statement->finish();
  }

