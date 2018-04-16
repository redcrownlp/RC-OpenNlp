<?php 

namespace App\Providers;

use App\TwitterStream;
use Phirehose;

class TwitterStreamProvider
{
	public function getStreamProvider($twitter_access_token, $twitter_access_token_secret, $filter = Phirehose::METHOD_FILTER){
		return new TwitterStream($twitter_access_token, $twitter_access_token_secret, $filter);
	}
	
}

