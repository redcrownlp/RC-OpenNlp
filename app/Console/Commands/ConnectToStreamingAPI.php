<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\TwitterStream;
use App\client;
use App\client_keyword;
use App\Providers\TwitterStreamProvider;

use Phirehose;

class ConnectToStreamingAPI extends Command
{
	
	const TWITTER_CONFIG = [
			
	'levant' => [
			'twitter_access_token' =>'',
			'twitter_access_token_secret' => '',
			'twitter_consumer_key' => '',
			'twitter_consumer_secret' => '',
	],
		
			
	];
	/**
	* The name and signature of the console command.
	*
	* @var string
	*/
	protected $signature = 'twitter:stream {client}';
	
	/**
	 * The console command description.
	 *
	 * @var string
	 */
	protected $description = 'Connect to the Twitter Streaming API';
	
	protected $twitterStream;
	protected $twitterStreamProvider;

    /**
     * Create a new command instance.
     *
     * @return void
     */
	public function __construct(TwitterStreamProvider $twitterStreamProvider)
    {
    	parent::__construct();    	
        $this->twitterStreamProvider = $twitterStreamProvider;

    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
    	// read command arguments
    	// set argument to class
    	$client = strtolower($this->argument('client'));
    	if(!array_key_exists($client, self::TWITTER_CONFIG)){
    		throw new \RuntimeException('Client '.$client.' is not configured');
    	}
    	
    	$twitter_consumer_key = self::TWITTER_CONFIG[$client]['twitter_consumer_key'];
    	$twitter_consumer_secret = self::TWITTER_CONFIG[$client]['twitter_consumer_secret'];
    	$twitter_access_token = self::TWITTER_CONFIG[$client]['twitter_access_token'];			    		
    	$twitter_access_token_secret = self::TWITTER_CONFIG[$client]['twitter_access_token_secret'];
    	
    	
    	
    	
    	$this->twitterStream = $this->twitterStreamProvider->getStreamProvider($twitter_access_token, $twitter_access_token_secret,Phirehose::METHOD_FILTER);
    	
    	$client_id=client::where('client_name',$client)->first();
//     	//die(var_dump($client_id));
//     	echo $client_id->id;
    	$client_keywords=client_keyword::where('client_id',$client_id->id)->first();

//     	echo $client_keywords->client_keywords;
//     	die();
    	
    	$this->twitterStream->setClient($client_id->id);
        //
        echo __NAMESPACE__,__FUNCTION__,PHP_EOL;
       
    	
    	//$this->twitterStream->
    	$this->twitterStream->consumerKey = $twitter_consumer_key;
    	$this->twitterStream->consumerSecret = $twitter_consumer_secret;
    	$this->twitterStream->setTrack(array($client_keywords->client_keywords));
    	$this->twitterStream->consume();
    }
}
