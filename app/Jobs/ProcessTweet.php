<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Queue\SerializesModels;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use App\twitter_feed;

class ProcessTweet implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;
    
    protected $tweet;
    private $client;

    /**
     * Create a new job instance.
     *
     * @return void
     */
    public function __construct($options)
    {
        //
        $this->client = $options['client'];
    	$this->tweet = $options['tweet'];
    	//echo 'handlinig tweet... time: ', time(), PHP_EOL;
    }

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {
    	//die($this->client);
    	ini_set('display_errors',1);
    	error_reporting(E_ALL);
    	
    	
    	$tweet = @json_decode($this->tweet,true);
    	
    	if(is_array($tweet) && count($tweet) && isset($tweet['text']) && !empty($tweet['text']))
    	{
    		echo 'handlinig ', $this->client,' tweet ID ',$tweet['id_str'], PHP_EOL;
    		
    		$tweet_text = isset($tweet['text']) ? $tweet['text'] : null;
    		$user_id = isset($tweet['user']['id_str']) ? $tweet['user']['id_str'] : null;
    		$user_screen_name = isset($tweet['user']['screen_name']) ? $tweet['user']['screen_name'] : null;
    		$tweet_link ="www.google.com";//isset($tweet[])
    		$tweet_created_at = isset($tweet['created_at']) ? $tweet['created_at'] : null;
    		$client_id = $this->client;
    		$user_location = isset($tweet['user']['location']) ? $tweet['user']['location'] : "-1";
    		$user_language = isset($tweet['user']['lang']) ? $tweet['user']['lang'] : "-1";
    		$user_timezone = isset($tweet['user']['time_zone']) ? $tweet['user']['time_zone'] : "-1";
    		$user_time_offset = isset($tweet['user']['utc_offset']) ? $tweet['user']['utc_offset'] : "-1";
    		$coordinates = isset($tweet['coordinates']['coordinates']) ? $tweet['coordinates']['coordinates'] : "-1";
    		$country = isset($tweet['place']['country']) ? $tweet['place']['country'] : "-1";
    		$place_name = isset($tweet['place']['full_name']) ? $tweet['place']['full_name'] : "-1";
    	
    	
    		$data = [
    			'tweet_id' => $tweet['id_str'],
    			'tweet_text' => $tweet_text,
    			'tweet_link' => $tweet_link,
    			'source_id' => $user_id,
    			'source_screen_name' => $user_screen_name,
    			'tweet_created_at' => $tweet_created_at,
    			'client_id' => $client_id,
    			'location' => $user_location,
    			'language' => $user_language,
    			'timezone' => $user_timezone,
    			'utc_offset' => $user_time_offset,
    			'coordinates' => $coordinates,
    			'country' => $country,
    			'location_name' => $place_name
    		];

    		try{
    			twitter_feed::create($data);
    		}
    		catch(\Exception $e){
    			print_r($e->getMessage());
    		}
    	
    		
    	}else{
    		echo 'Failed... ',PHP_EOL;
    	}
    }
}
