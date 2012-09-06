#!/usr/bin/perl
package Search_mem;
use strict;
use DBI;
use CGI;
use HTML::Template;

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

sub search_id{
	my $username = shift;
	$query = $conn->prepare("select m.m_id from member m,users u  where m.m_id = u.m_id and u.username = '$username'");
	$query->execute();
	my @op = $query->fetchrow_array();
	return $op[0];
}


1;

