<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class twitter_feed extends Model
{
    //
	protected $fillable = [
			'tweet_id',
			'tweet_text',
			'tweet_link',
			'source_screen_name',
			'source_id',
			'tweet_created_at',
			'client_id',
			'location',
			'language',
			'timezone',
			'utc_offset',
			'coordinates',
			'country',
			'location_name'
	];
}
