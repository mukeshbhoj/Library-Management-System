#!/usr/bin/perl
package Check_add_book;
use strict;
use DBI;
use CGI;
use HTML::Template;
use List::Util 'max';

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});


sub check_id{
	my $id = shift;
	$query = $conn->prepare("select group_id from book_info");
	$query->execute();
	while(my @op = $query->fetchrow_array()){
		if (grep {$_ eq $id} @op){
			return 1;
		}
	}
	return 0;
}

sub check_bid{
	my $id = shift;
	$query = $conn->prepare("select book_id from book");
	$query->execute();
	while(my @op = $query->fetchrow_array()){
		if (grep {$_ eq $id} @op){
			return 1;
		}
	}
	return 0;
}

sub new_bid{
	$query = $conn->prepare("select max(group_id) from book_info");
	$query->execute();
	my @arr = $query->fetchrow();
	return $arr[0]+1;
}


sub check_issued{

	my $id = shift;
	$query = $conn->prepare("select count(*) from issue_book where book_id = '$id' and return_by = '0'");
	$query->execute();
	my @op = $query->fetchrow_array();
	return $op[0];
}


1;
