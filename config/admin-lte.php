<?php

return [
	'user-name' => 'tayeb',
	'skin' => 'blue',
	'menu' => [
				'MAIN NAVIGATION',
					['text' => 'Blog','url' => 'admin/blog'],
					['text' => 'Pages','url' => 'admin/pages','icon' => 'file'],
					['text' => 'Show my website','url' => '/','target' => '_blank'],
				'ACCOUNT SETTINGS',
					['text' => 'Profile','route' => 'admin.profile','icon' => 'user'],
					['text' => 'Change Password','route' => 'admin.password','icon' => 'lock']
		],
];
