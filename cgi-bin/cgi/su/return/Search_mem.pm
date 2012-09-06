#!/usr/bin/perl
package Search_mem;
use strict;
use DBI;
use CGI;
use HTML::Template;

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

sub search_id
{
	my $id = shift;
	$query = $conn->prepare("select m.*,u.username,u.password from member m,users u  where m.m_id = u.m_id and m.m_id = '$id'");
	$query->execute();
	my @op = $query->fetchrow_array();
	return @op;
}
sub search_mem
{
	my $mid = shift;
	my @loop_data = ();
	$query = $conn->prepare("select m.*,u.username,u.password from member m,users u  where m.m_id = u.m_id and m.m_id = '$mid'");
	$query->execute();
	my @op = $query->fetchrow_array();
	my %row_data;
	my($id1,$name,$birthdate,$address,$city,$state,$sex,$phno,$joindate,$usertype,$max_book_allow,$username,$password) = @op;

	$row_data{id}=$id1;
	$row_data{name}=$name;
	$row_data{birthdate}=$birthdate;
	$row_data{address}=$address;
	$row_data{city}=$city;
	$row_data{state}=$state;
	$row_data{sex}=$sex;
	$row_data{phno}=$phno;
	$row_data{joindate}=$joindate;
	$row_data{usertype}=$usertype;
	$row_data{username}=$username;
	$row_data{password}=$password;
	push(@loop_data,\%row_data);
	return @loop_data;
}

sub search_all_mem
{
	my @loop_data = ();
	$query = $conn->prepare("select m.*,u.* from member m,users u  where m.m_id = u.m_id order by m.m_id");
	$query->execute();
	
	while(my @op = $query->fetchrow_array())
	{
	my %row_data;
	my($id,$name,$birthdate,$address,$city,$state,$sex,$phno,$joindate,$usertype,$max_book_allow,$username,$password) = @op;

	$row_data{id}=$id;
	$row_data{name}=$name;
	$row_data{birthdate}=$birthdate;
	$row_data{address}=$address;
	$row_data{city}=$city;
	$row_data{state}=$state;
	$row_data{sex}=$sex;
	$row_data{phno}=$phno;
	$row_data{joindate}=$joindate;
	$row_data{usertype}=$usertype;
	$row_data{username}=$username;
	$row_data{password}=$password;
	push(@loop_data,\%row_data);
	}
	return @loop_data;
}

1;

