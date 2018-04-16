<?php

use App\twitter_feed;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/feed', function () {
	$feeds=twitter_feed::where([
			['created_at','>',date("Y-m-d")],
			['client_id','=','2']
	])->get();
	//$feeds=twitter_feed::where('client_id','=','2')->get();
	echo "<table>";
	foreach($feeds as $feed)
	{
		echo "<tr>";
		echo "<td>".$feed->tweet_text."</td>";
		echo "<td>".$feed->tweet_created_at."</td>";
		echo "<td>".$feed->source_screen_name."</td>";
		echo "<td>".$feed->client_id."</td>";
		echo "<td>".$feed->created_at."</td>";
		echo "</tr>";
	}
	echo "</table>";
// 	var_dump($feeds);die();
// 	$feed=twitter_feed::find('1348');
// 	return $feed->tweet_text;
    //return view('welcome');
});

Auth::routes();

Route::get('/', 'HomeController@index')->name('home');
