#! /ms/dist/perl5/bin/perl -w
############################################################
#
#	PreparedStatement.pl
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

  my $SQL = "SELECT * FROM phones WHERE lname = ? AND fname = ?";

  my $statement = $database->prepare($SQL);
  $statement->execute("Green", "Fred");

  while(my $data = $statement->fetch() ){
    print "@$data \n";
  }

  $statement->finish();
  $database->disconnect();
