#!/usr/bin/perl
package Check_add_mem;
use strict;
use DBI;
use CGI;
use HTML::Template;

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});


sub check_id
{
	my $id = shift;
	$query = $conn->prepare("select m_id from member");
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

sub check_username
{
	my $username = shift;
	$query = $conn->prepare("select username from users");
	$query->execute();
	while(my @op = $query->fetchrow_array())
	{
		if (grep {$_ eq $username} @op)
		{
			return 1;
		}
	}
	return 0;
}

sub check_username_id
{
	my ($username, $id) = @_;
	$query = $conn->prepare("select username from users where m_id = '$id'");
	$query->execute();
	while(my @op = $query->fetchrow_array())
	{
		if (grep {$_ eq $username} @op)
		{
			return 0;
		}
	}
	return 1;
}

sub check_password
{
	my ($password,$username) = @_;
	$query = $conn->prepare("select count(*) from users where username='$username' and password='$password'");
	$query->execute();
	my @op = $query->fetchrow_array();
	return $op[0];
}

1;
