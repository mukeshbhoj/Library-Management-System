#!/usr/bin/perl
package Check_add_book;
use strict;
use DBI;
use CGI;
use HTML::Template;

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});


sub check_id
{
	my $id = shift;
	$query = $conn->prepare("select group_id from book_info");
	$query->execute();
	while(my @op = $query->fetchrow_array())
	{
		if (grep {$_ eq $id} @op)
		{
			return 1;
		}
	}
	return 0;
}

sub check_bid
{
	my $id = shift;
	$query = $conn->prepare("select book_id from book");
	$query->execute();
	while(my @op = $query->fetchrow_array())
	{
		if (grep {$_ eq $id} @op)
		{
			return 1;
		}
	}
	return 0;
}

1;
