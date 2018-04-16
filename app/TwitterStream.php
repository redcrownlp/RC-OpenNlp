<?php namespace App;

use OauthPhirehose;
use App\Jobs\ProcessTweet;
use Illuminate\Foundation\Bus\DispatchesJobs;

class TwitterStream extends OauthPhirehose
{
	use DispatchesJobs;
	
	private $client;
	
	/**
	 * Enqueue each status
	 *
	 * @param string $status
	 */
	public function enqueueStatus($status)
	{
		// modify status and inject client;
// 		$statusArray = json_decode($status, true);
// 		$statusArray['client'] = $this->client;
// 		$status = json_encode($statusArray);
		$this->dispatch(new ProcessTweet([
				'tweet'=>$status,
				'client'=>$this->client
				
		]));
	}
	
	public function setClient($client){
		$this->client = $client;
		return $this;
	}
}

