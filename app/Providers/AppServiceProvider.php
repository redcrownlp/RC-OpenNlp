<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

use Phirehose;
use App\TwitterStream;
use Illuminate\Console\Command;
use App\Providers\TwitterStreamProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    	    	
    	
    	
   
    	$this->app->bind('App\Providers\TwitterStreamProvider', function ($app) {
//     		$twitter_access_token = "20970930-3tmenpfIwRyonWRDKvpylFbosn3R0li97MjIC3vdE";
//     		$twitter_access_token_secret = "YxXbMiKsfCzBxPwrIygkEOrJHX15HfSERtfgF8dapkZ8x";
//            die(print_r(get_class_methods($app)));
    		return new TwitterStreamProvider();
//     		return new TwitterStream($twitter_access_token, $twitter_access_token_secret, Phirehose::METHOD_FILTER);
//     		return 'Hani';TwitterStream::class;
    	});
    	
    }
}
